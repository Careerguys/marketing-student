#!/usr/bin/env python3
"""Controleert de gebouwde site. Draai na elke `python3 build.py`."""
import json, re, sys
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).parent
SITE = "https://marketing-student.nl"
files = sorted(p for p in ROOT.rglob("*.html") if p.name in ("index.html", "404.html") and "assets" not in p.parts)
probs = []
titles, descs = {}, {}


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.heads = []; s.ids = []; s.links = []; s.imgs = []; s.inputs = []; s.labels = set()
        s.in_title = False; s.title = ""; s.ld = []; s.in_ld = False; s.buf = ""; s.summ = []; s.in_sum = False; s.sbuf = ""
        s.faqbody = []; s.in_fb = 0; s.fbuf = ""; s.depth = 0
    def handle_starttag(s, t, a):
        a = dict(a)
        if t in ("h1", "h2", "h3", "h4"): s.heads.append(int(t[1]))
        if "id" in a: s.ids.append(a["id"])
        if t == "a" and "href" in a: s.links.append(a["href"])
        if t == "img": s.imgs.append(a)
        if t in ("input", "textarea", "select") and a.get("type") not in ("hidden", "radio"): s.inputs.append(a)
        if t == "label" and "for" in a: s.labels.add(a["for"])
        if t == "title": s.in_title = True
        if t == "script" and a.get("type") == "application/ld+json": s.in_ld = True; s.buf = ""
        if t == "details" and "mobile-nav__spec" in a.get("class", ""): s.skip_sum = True
        if t == "summary" and not getattr(s, "skip_sum", False): s.in_sum = True; s.sbuf = ""
        if t == "div" and a.get("class") == "faq__body": s.in_fb = 1; s.fbuf = ""
        elif s.in_fb and t == "div": s.in_fb += 1
    def handle_endtag(s, t):
        if t == "title": s.in_title = False
        if t == "script" and s.in_ld: s.in_ld = False; s.ld.append(s.buf)
        if t == "details": s.skip_sum = False
        if t == "summary" and s.in_sum: s.in_sum = False; s.summ.append(s.sbuf.strip())
        if t == "div" and s.in_fb:
            s.in_fb -= 1
            if s.in_fb == 0: s.faqbody.append(re.sub(r"\s+", " ", s.fbuf).strip())
    def handle_data(s, d):
        if s.in_title: s.title += d
        if s.in_ld: s.buf += d
        if s.in_sum: s.sbuf += d
        if s.in_fb: s.fbuf += d


def url_to_file(u):
    u = u.split("#")[0].split("?")[0]
    if u.endswith("/"): return ROOT / u.lstrip("/") / "index.html"
    return ROOT / u.lstrip("/")


all_ids = {}
parsed = {}
for f in files:
    h = f.read_text(encoding="utf-8")
    p = P(); p.feed(h); parsed[f] = (p, h)
    all_ids[f] = set(p.ids)

for f, (p, h) in parsed.items():
    rel = "/" + str(f.relative_to(ROOT)).replace("index.html", "")
    name = rel
    noindex = 'content="noindex' in h
    if p.heads.count(1) != 1: probs.append(f"{name}: {p.heads.count(1)} h1")
    for a, b in zip(p.heads, p.heads[1:]):
        if b > a + 1: probs.append(f"{name}: kopsprong h{a}->h{b}"); break
    if len(p.title) > 60: probs.append(f"{name}: title {len(p.title)} tekens")
    d = re.search(r'name="description" content="([^"]*)"', h).group(1)
    if not 50 <= len(d) <= 160: probs.append(f"{name}: description {len(d)} tekens")
    if not noindex:
        if p.title in titles: probs.append(f"{name}: dubbele title met {titles[p.title]}")
        if d in descs: probs.append(f"{name}: dubbele description met {descs[d]}")
        titles[p.title] = name; descs[d] = name
        can = re.search(r'rel="canonical" href="([^"]+)"', h)
        if not can or can.group(1) != SITE + rel: probs.append(f"{name}: canonical {can.group(1) if can else 'ontbreekt'}")
    dup = {i for i in p.ids if p.ids.count(i) > 1}
    if dup: probs.append(f"{name}: dubbele id's {sorted(dup)[:5]}")
    for l in p.links:
        if l.startswith("#"):
            if l[1:] and l[1:] not in all_ids[f]: probs.append(f"{name}: anker {l} bestaat niet")
        elif l.startswith("/"):
            tf = url_to_file(l)
            if not tf.exists(): probs.append(f"{name}: dode link {l}")
            elif "#" in l and l.split("#")[1] not in all_ids.get(tf, set()): probs.append(f"{name}: anker {l} bestaat niet")
        elif l.startswith("http") and "marketing-student.nl" not in l and "rel=" not in h[h.find(l) - 200:h.find(l) + 200]:
            pass
    for im in p.imgs:
        if "alt" not in im: probs.append(f"{name}: img zonder alt")
        if "width" not in im or "height" not in im: probs.append(f"{name}: img zonder afmetingen")
    for inp in p.inputs:
        if inp.get("name") == "bot-field": continue
        if inp.get("id") not in p.labels: probs.append(f"{name}: invoerveld zonder label {inp.get('id')}")
    txt = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    txt = re.sub(r"<[^>]+>", " ", txt)
    if re.search(r"\[[A-Z][A-Z0-9 .\-/]{2,}\]", txt): probs.append(f"{name}: plaatshouder in tekst")
    if re.search(r"€|\beuro\b|per uur", txt, re.I): probs.append(f"{name}: prijs in tekst")
    for block in p.ld:
        try:
            g = json.loads(block)["@graph"]
        except Exception as e:
            probs.append(f"{name}: JSON-LD ongeldig {e}"); continue
        ids, refs = set(), set()
        def walk(o):
            if isinstance(o, dict):
                if "@id" in o and len(o) > 1: ids.add(o["@id"])
                elif "@id" in o: refs.add(o["@id"])
                for v in o.values(): walk(v)
            elif isinstance(o, list):
                for v in o: walk(v)
        walk(g)
        ext = {r for r in refs - ids if r.endswith("#service") and url_to_file(r.replace(SITE, "").split("#")[0]).exists()}
        for r in refs - ids - ext: probs.append(f"{name}: schema-verwijzing zonder node {r}")
        for n in g:
            if n["@type"] == "FAQPage":
                qs = [q["name"] for q in n["mainEntity"]]; ans = [q["acceptedAnswer"]["text"] for q in n["mainEntity"]]
                if qs != p.summ: probs.append(f"{name}: FAQ-vragen in schema wijken af van pagina")
                if ans != p.faqbody: probs.append(f"{name}: FAQ-antwoorden in schema wijken af van pagina")
            if n["@type"] == "BreadcrumbList":
                last = n["itemListElement"][-1]["item"]
                if last != SITE + rel: probs.append(f"{name}: laatste kruimel {last}")
    if "data-netlify" in h:
        for fm in re.findall(r'<form[^>]*data-netlify[^>]*>', h):
            if 'action="/bedankt/"' not in fm: probs.append(f"{name}: formulier zonder bedankt-actie")

# sitemap, redirects
sm = re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text())
for u in sm:
    if not url_to_file(u.replace(SITE, "")).exists(): probs.append(f"sitemap: {u} bestaat niet")
built = {("/" + str(f.relative_to(ROOT)).replace("index.html", "")) for f in files}
for line in (ROOT / "_redirects").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    src, dst, code = line.split()[:3]
    if src.startswith("http"):  # domeinredirect (netlify.app naar hoofddomein)
        continue
    if code.startswith("301"):
        if not url_to_file(dst).exists(): probs.append(f"redirect: doel {dst} bestaat niet")
        if src in built: probs.append(f"redirect: bron {src} is een bestaande pagina")
print(f"{len(files)} pagina's | {len(sm)} in sitemap | {len(probs)} problemen")
for x in probs: print(" -", x)
sys.exit(1 if probs else 0)
