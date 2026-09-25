#!/usr/bin/env python3
"""Bouwt marketing-student.nl als statische site.

    python3 build.py

Genereert alle HTML, sitemap.xml, robots.txt, _redirects, netlify.toml,
llms.txt en site.webmanifest, en controleert daarna het resultaat.
Bewerk nooit de gegenereerde HTML: pas dit bestand of de databestanden aan.
"""
import datetime
import hashlib
import html
import json
import re
import sys
from pathlib import Path

from artikelen import ARTIKELEN
from diensten_data import D as DIENST, SC as SHOWCASES, PLAT as PLATFORMS
from faq_data import antwoord

ROOT = Path(__file__).parent
SITE = "https://marketing-student.nl"
SITE_NAME = "Marketing Student"
GTM_ID = "GTM-M3KWR76W"  # Tag Manager-container. Leeg = geen tracking en geen cookiebanner.
PHONE = "085-060 8631"
PHONE_HREF = "tel:+31850608631"
EMAIL = "info@marketing-student.nl"
TODAY = datetime.date.today().isoformat()
PUBLISHED = "2026-09-25"  # publicatiedatum kennisbank-artikelen

B = json.loads((ROOT / "brands.json").read_text())


# ---------------------------------------------------------------- iconen
def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{B["icons"][name]}</svg>')


def brand(name):
    col = B["colors"].get(name, "#0f2741")
    return (f'<svg viewBox="0 0 24 24" fill="{col}" aria-hidden="true" focusable="false">{B["paths"][name]}</svg>')


def esc(t):
    return html.escape(t, quote=True)


# ---------------------------------------------------------------- data
SPECS = [
    # slug, label, korte naam, merk of icoon, korte omschrijving, menugroep
    ("seo-specialist-inhuren", "SEO-specialist inhuren", ("icon", "search"), "Zoekwoordonderzoek, on-page SEO en content die rankt.", "Vindbaarheid"),
    ("google-ads-specialist-inhuren", "Google Ads-specialist inhuren", ("brand", "googleads"), "Campagnes opzetten, bijsturen en rapporteren.", "Vindbaarheid"),
    ("social-media-uitbesteden", "Social media uitbesteden", ("brand", "meta"), "Posts plannen, maken en je community beheren.", "Social media en content"),
    ("instagram-uitbesteden", "Instagram uitbesteden", ("brand", "instagram"), "Feed, stories en reels, gepland en gemaakt.", "Social media en content"),
    ("tiktok-uitbesteden", "TikTok uitbesteden", ("brand", "tiktok"), "Korte video's die passen bij het platform.", "Social media en content"),
    ("linkedin-marketing-uitbesteden", "LinkedIn-marketing uitbesteden", ("brand", "linkedin"), "Zakelijke content en advertenties.", "Social media en content"),
    ("contentmarketing-uitbesteden", "Contentmarketing uitbesteden", ("icon", "camera"), "Een content creator voor foto, video en tekst.", "Social media en content"),
    ("huisstijl-laten-maken", "Huisstijl laten maken", ("icon", "pen"), "Logo, huisstijl, tone of voice en merkverhaal.", "Merk en e-mail"),
    ("email-marketing-uitbesteden", "E-mailmarketing uitbesteden", ("icon", "mail"), "Nieuwsbrieven en automatische flows.", "Merk en e-mail"),
    ("wordpress-specialist-inhuren", "WordPress-specialist inhuren", ("brand", "wordpress"), "Pagina's bouwen, onderhouden en versnellen.", "Web en AI"),
    ("shopify-specialist-inhuren", "Shopify-specialist inhuren", ("brand", "shopify"), "Productpagina's en webshopbeheer.", "Web en AI"),
    ("ai-specialist-inhuren", "AI-specialist inhuren", ("brand", "openai"), "AI-tools en workflows in je marketing.", "Web en AI"),
    ("claude-specialist-inhuren", "Claude-specialist inhuren", ("brand", "claude"), "Claude inzetten voor content en processen.", "Web en AI"),
]
SPEC = {s[0]: s for s in SPECS}
GROUPS = ["Vindbaarheid", "Social media en content", "Merk en e-mail", "Web en AI"]
ART = {a["slug"]: a for a in ARTIKELEN}

# Artikelen die bij een dienst horen (alleen bestaande).
REL = {
    "seo-specialist-inhuren": ["wat-doet-een-seo-specialist", "freelance-marketeer-of-marketing-student", "wat-voor-type-marketeers-zijn-er"],
    "social-media-uitbesteden": ["social-media-uitbesteden-waar-let-je-op", "welke-social-media-kiezen", "freelance-marketeer-of-marketing-student"],
    "instagram-uitbesteden": ["social-media-uitbesteden-waar-let-je-op", "welke-social-media-kiezen", "wat-voor-type-marketeers-zijn-er"],
    "tiktok-uitbesteden": ["welke-social-media-kiezen", "social-media-uitbesteden-waar-let-je-op", "wat-voor-type-marketeers-zijn-er"],
    "linkedin-marketing-uitbesteden": ["welke-social-media-kiezen", "social-media-uitbesteden-waar-let-je-op", "wat-doet-een-head-of-marketing"],
    "contentmarketing-uitbesteden": ["social-media-uitbesteden-waar-let-je-op", "welke-social-media-kiezen", "wat-voor-type-marketeers-zijn-er"],
}
REL_DEFAULT = ["freelance-marketeer-of-marketing-student", "wat-voor-type-marketeers-zijn-er", "wat-doet-een-head-of-marketing"]

STEPS = [
    ("Beschrijf je vraag", "Vul het korte formulier in of bel ons. Dat kost je een paar minuten."),
    ("Ontvang een voorstel", "Je krijgt een voorstel met de student die past bij je vraag, en de senior die meekijkt."),
    ("Start", "Kennismaken, toegang tot je tools regelen en aan de slag."),
]
COMPARE = [
    ("Senior controleert het werk", "+Altijd", "-Zelf regelen", "+Ja"),
    ("Contract", "+Geen contract", "Per opdracht", "Wisselt"),
    ("Vervanging als het niet klikt", "+Kosteloos", "-Zelf zoeken", "+Ja"),
    ("Flexibel in uren", "+Vanaf 4 uur per week", "+Ja", "Wisselt"),
    ("Werkt in jouw tools en team", "+Ja", "+Ja", "Wisselt"),
]
COMPARE_SEO = [
    ("Senior SEO controleert", "+Altijd", "-Zelf regelen", "+Ja"),
    ("Contract", "+Geen contract", "Per opdracht", "Wisselt"),
    ("Vervanging als het niet klikt", "+Kosteloos", "-Zelf zoeken", "+Ja"),
    ("Werkt in jouw Search Console", "+Ja", "+Ja", "Wisselt"),
]
FAQ_HOME = ["Wat kost een marketing student?", "Wie begeleidt de student?", "Hoe snel kan een student beginnen?", "Zijn de studenten goed genoeg?",
            "Zit ik vast aan een contract?", "Wat als de student niet bevalt?", "Werken studenten remote of op locatie?"]
HOME_PLATFORMS = [("google", "Google Search Console", "Posities en vindbaarheid"), ("googleads", "Google Ads", "Zoek- en displaycampagnes"),
                  ("meta", "Meta", "Facebook- en Instagram-ads"), ("linkedin", "LinkedIn", "Content en advertenties"),
                  ("tiktok", "TikTok", "Korte video en ads"), ("wordpress", "WordPress", "Pagina's en blogs"),
                  ("shopify", "Shopify", "Webshop en producten"), ("youtube", "YouTube", "Video en advertenties"),
                  ("openai", "ChatGPT", "Content en analyse"), ("claude", "Claude", "AI-workflows")]
HOME_SC = dict(pill="Wat een student voor je doet", t1="Jouw bedrijf", t2="zichtbaar op elk kanaal", vraag="[jouw dienst] in de buurt",
               lead="Een getrainde student werkt aan je vindbaarheid, advertenties en content. Een ervaren marketeer controleert elke stap.",
               sr="Voorbeeld: jouw bedrijf staat bovenaan in Google, in Google Ads, in Google Maps, op Instagram, op LinkedIn en in het antwoord van ChatGPT.",
               links=[("google", "Google"), ("googleads", "Google Ads"), ("meta", "Meta"), ("linkedin", "LinkedIn"), ("openai", "ChatGPT"), ("claude", "Claude")],
               kaarten=[("google", "Google", "Zoeken", "serp"), ("googleads", "Google Ads", "", "ad"), ("openai", "ChatGPT", "", "chat"),
                        ("google", "Google", "Maps", "local"), ("instagram", "Instagram", "Gesponsord", "social"), ("linkedin", "LinkedIn", "", "social")])


# ---------------------------------------------------------------- componenten
def spec_icon(kind):
    t, n = kind
    if t == "brand":
        return f'<span class="brand-tile">{brand(n)}</span>'
    return f'<span class="card__icon">{icon(n)}</span>'


def section_head(pill, title, lead_txt=None, center=False, tag="h2", hid=None):
    cls = "section-head section-head--center" if center else "section-head"
    idattr = f' id="{hid}"' if hid else ""
    lead_html = f'<p class="lead">{lead_txt}</p>' if lead_txt else ""
    pill_html = f'<p class="pill">{pill}</p>' if pill else ""
    return f'<div class="{cls}">{pill_html}<{tag}{idattr}>{title}</{tag}>{lead_html}</div>'


def section(inner, cls="", label=None):
    aria = f' aria-labelledby="{label}"' if label else ""
    return f'<section class="section {cls}"{aria}><div class="container">{inner}</div></section>'


def btn(text, href, kind="grad", ico=None, lg=False, attrs=""):
    size = " btn--lg" if lg else ""
    i = icon(ico) if ico else ""
    return f'<a class="btn btn--{kind}{size}" href="{href}"{attrs}>{i}{text}</a>'


def hero_buttons(label="Vraag een offerte aan", href="#offerte"):
    return (f'<div class="btn-row btn-row--stack">{btn(label, href, "grad", "arrow-right", True)}'
            f'{btn("Bel " + PHONE, PHONE_HREF, "outline", "phone", True)}</div>')


def crumbs(items):
    lis = []
    for i, (name, url) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li><span aria-current="page">{name}</span></li>')
        else:
            lis.append(f'<li><a href="{url}">{name}</a>{icon("chevron-right")}</li>')
    return f'<nav class="crumbs" aria-label="Kruimelpad"><ol>{"".join(lis)}</ol></nav>'


def field(fid, label, typ="text", ph="", required=True, ac="", full=False, textarea=False):
    req = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    r = " required" if required else ""
    a = f' autocomplete="{ac}"' if ac else ""
    p = f' placeholder="{ph}"' if ph else ""
    cls = "field field--full" if full else "field"
    ctrl = (f'<textarea id="{fid}" name="{fid.split("-")[0]}" rows="5"{p}{r} aria-describedby="{fid}-err"></textarea>' if textarea else
            f'<input id="{fid}" name="{fid.split("-")[0]}" type="{typ}"{p}{a}{r} aria-describedby="{fid}-err">')
    return f'<div class="{cls}"><label for="{fid}">{label}{req}</label>{ctrl}<p class="field__error" id="{fid}-err"></p></div>'


FORM_IDS = {}


def uid(base):
    FORM_IDS[base] = FORM_IDS.get(base, 0) + 1
    return f"{base}-{FORM_IDS[base]}"


def form_open(name, page_slug):
    return (f'<form class="form-card" name="{name}" method="post" action="/bedankt/" data-netlify="true" netlify-honeypot="bot-field" novalidate data-validate>'
            f'<input type="hidden" name="form-name" value="{name}"><input type="hidden" name="pagina" value="/{page_slug}">'
            f'<p class="hp" aria-hidden="true"><label>Laat dit veld leeg <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>')


PRIVACY_NOTE = '<p class="form-note">We gebruiken je gegevens alleen om je aanvraag te beantwoorden. Lees ons <a href="/privacy-policy/">privacybeleid</a>.</p>'


def offerte_form(page_slug, title="Vraag vrijblijvend een offerte aan", hid="offerte"):
    n = uid("f")
    return f'''<div id="{hid}">{form_open("offerte", page_slug)}
  <h2>{title}</h2>
  <fieldset class="choice"><legend>Wat zoek je?</legend>
    <label><input type="radio" name="werkvorm" value="Student inhuren" checked>Student inhuren</label>
    <label><input type="radio" name="werkvorm" value="Opdracht uitbesteden">Opdracht uitbesteden</label>
  </fieldset>
  <div class="form-grid form-grid--2">
    {field(f"naam-{n}", "Naam", ph="Voor- en achternaam", ac="name")}
    {field(f"bedrijf-{n}", "Bedrijfsnaam", ph="Naam van je bedrijf", ac="organization")}
    {field(f"telefoon-{n}", "Telefoon", "tel", "06 12345678", ac="tel")}
    {field(f"email-{n}", "Zakelijk e-mailadres", "email", "naam@bedrijf.nl", ac="email")}
  </div>
  <button class="btn btn--grad form-submit" type="submit">Ontvang mijn offerte{icon("arrow-right")}</button>
  {PRIVACY_NOTE}
</form></div>'''


def trustbar():
    items = [("users", "HBO/WO-studenten", "Getraind en gescreend"), ("shield", "Onderdeel van", "BlauweLink.nl en Careerguys.nl")]
    cells = "".join(f'<div class="trustbar__item"><span class="trustbar__icon">{icon(i)}</span><div><strong>{a}</strong><span>{b}</span></div></div>' for i, a, b in items)
    return section(f'<div class="trustbar">{cells}</div>', "section--flush-top")


def sc_card(merk, naam, label, soort, vraag):
    lab = f'<span class="sc-card__label">{label}</span>' if label else ""
    ln = lambda w: f'<span class="sc-ln" style="width:{w}%"></span>'
    kop = lambda t: f'<span class="sc-hit__kop">{t}</span>'
    if soort in ("serp", "ad"):
        tag = '<span class="sc-hit__tag">Gesponsord</span>' if soort == "ad" else ""
        hit = f'<div class="sc-hit">{tag}{kop("Jouw bedrijf")}<span class="sc-hit__sub">jouwbedrijf.nl › diensten</span>{ln(92)}{ln(66)}</div>'
    elif soort == "local":
        hit = f'<div class="sc-hit"><span class="sc-map"></span>{kop("Jouw bedrijf")}<span class="sc-hit__sub">Open · in de buurt</span></div>'
    elif soort == "chat":
        hit = f'<div class="sc-hit">{kop("1. Jouw bedrijf")}<span class="sc-hit__sub">Genoemd als bron, met link</span></div>'
    elif soort == "snippet":
        hit = f'<div class="sc-hit">{ln(96)}{ln(84)}{ln(58)}{kop("jouwbedrijf.nl")}</div>'
    else:
        hit = (f'<div class="sc-hit">{kop("Jouw bedrijf")}<span class="sc-img"></span>{ln(78)}'
               '<span class="sc-acts"><span>Vind ik leuk</span><span>Reageren</span><span>Delen</span></span></div>')
    lijst = ""
    if soort in ("serp", "ad", "chat", "local"):
        lijst = f'<div class="sc-list"><div><i></i>{ln(60)}</div><div><i></i>{ln(46)}</div></div>'
    return (f'<div class="sc-card"><div class="sc-card__bar"><span class="sc-card__logo">{brand(merk)}</span>'
            f'<span class="sc-card__name">{naam}</span>{lab}</div><span class="sc-card__q">{vraag}</span>{hit}{lijst}</div>')


def showcase(cfg):
    cards = "".join(sc_card(*k, cfg["vraag"]) for k in cfg["kaarten"])
    brands_html = "".join(f"<span>{brand(b)}{n}</span>" for b, n in cfg["links"])
    return f'''<section class="section" aria-labelledby="showcase-titel"><div class="container">
  <p class="sr-only">{cfg["sr"]}</p>
  <div class="showcase__stage">
    <div class="showcase__center">
      <p class="pill">{cfg["pill"]}</p>
      <h2 id="showcase-titel">{cfg["t1"]} <span class="grad">{cfg["t2"]}</span></h2>
      <div class="searchbar" aria-hidden="true">{icon("search")}<span>{cfg["vraag"]}</span></div>
    </div>
    <div class="showcase__cards" aria-hidden="true">{cards}</div>
  </div>
  <div class="showcase__foot"><p class="lead">{cfg["lead"]}</p><div class="showcase__brands" aria-hidden="true">{brands_html}</div></div>
</div></section>'''


def spec_grid():
    cards = ""
    for slug, label, kind, card, _ in SPECS:
        cards += (f'<a class="card spec-card" href="/{slug}/">{spec_icon(kind)}<h3>{label}</h3><p>{card}</p>'
                  f'<span class="link-arrow">Bekijk{icon("arrow-right")}</span></a>')
    cards += (f'<div class="spec-cta"><div><h3>Twijfel je welke student past?</h3><p>Beschrijf je vraag, dan denken we mee.</p></div>'
              f'{btn("Vraag een offerte aan", "/offerte-aanvragen/", "grad", "arrow-right")}</div>')
    return f'<div class="spec-grid">{cards}</div>'


def plans(noun=None, href="#offerte"):
    t1 = f"{noun} structureel inhuren" if noun else "Student structureel inhuren"
    data = [
        ("users", t1, "Doorlopend", "vanaf 4 uur per week",
         ["Werkt mee in jouw team en tools", "Uren schalen mee met je planning", "Begeleid door een senior marketeer", "Geen contract, kosteloze vervanging"],
         "Student inhuren", True),
        ("file", "Opdracht uitbesteden", "Eenmalig", "afgebakend project",
         ["Heldere scope en deadline vooraf", "Ideaal voor een audit, campagne of contentreeks", "Opgeleverd en gecontroleerd door een senior", "Je weet vooraf wat het kost"],
         "Opdracht bespreken", False),
    ]
    out = ""
    for ic, t, kind, sub, pts, cta, feat in data:
        tag = '<span class="plan__tag">Meest gekozen</span>' if feat else ""
        li = "".join(f"<li>{icon('check')}<span>{p}</span></li>" for p in pts)
        out += (f'<div class="plan{" plan--featured" if feat else ""}">{tag}<div class="plan__head">{icon(ic)}<h3>{t}</h3></div>'
                f'<p class="plan__kind"><strong>{kind}</strong><span>{sub}</span></p><ul class="checks">{li}</ul>'
                f'{btn(cta, href, "grad" if feat else "outline")}</div>')
    return f'<div class="plans">{out}</div>'


def steps():
    out = "".join(f'<li class="card"><span class="step__num" aria-hidden="true">{i}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS, 1))
    return f'<ol class="steps">{out}</ol>'


def compare(rows):
    heads = ["Marketing student", "Freelancer", "Bureau"]
    th = '<th scope="col"><span class="sr-only">Kenmerk</span></th>' + "".join(f'<th scope="col">{h}</th>' for h in heads)
    trs = ""
    for r in rows:
        cells = f'<th scope="row">{r[0]}</th>'
        for v in r[1:]:
            if v.startswith("+"):
                cells += f'<td class="yes"><span>{icon("check")}{v[1:]}</span></td>'
            elif v.startswith("-"):
                cells += f'<td class="no"><span>{icon("x")}{v[1:]}</span></td>'
            else:
                cells += f"<td><span>{v}</span></td>"
        trs += f"<tr>{cells}</tr>"
    return (f'<div class="compare"><table><caption class="sr-only">Vergelijking marketing student, freelancer en bureau</caption>'
            f'<colgroup><col><col><col><col></colgroup><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')


def platform_tiles(items):
    out = "".join(f'<div class="platform"><span class="brand-tile">{brand(b)}</span><h3>{n}</h3><p>{d}</p></div>' for b, n, d in items)
    return f'<div class="platforms" style="--cols:{min(len(items), 5)}">{out}</div>'


def post_cards(slugs):
    out = ""
    for s in slugs:
        a = ART[s]
        out += (f'<a class="post-card" href="/kennisbank/{s}/"><span class="post-card__img"><span class="post-card__cat">{a["categorie"]}</span></span>'
                f'<div class="post-card__body"><h3>{a["titel"]}</h3><p>{meta_short(a["meta"])}</p>'
                f'<span class="link-arrow">Lees het artikel{icon("arrow-right")}</span></div></a>')
    return f'<div class="grid grid--3">{out}</div>'


def meta_short(t):
    return t.split(". ")[0].rstrip(".") + "."


def faq_block(title, questions, answers_override=None):
    """questions: lijst vragen; antwoord komt uit faq_data (één bron voor pagina en schema)."""
    items = []
    for i, q in enumerate(questions):
        a = (answers_override or {}).get(q) or antwoord(q)
        items.append((q, a))
    det = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}{icon("plus")}</summary><div class="faq__body"><p>{a}</p></div></details>'
                  for i, (q, a) in enumerate(items))
    inner = f'<div class="faq-wrap">{section_head("Veelgestelde vragen", title)}<div class="faq">{det}</div></div>'
    return section(inner), items


def cta_block(title="Klaar om je marketing te versterken?", text="Vertel wat je nodig hebt. Je krijgt een voorstel met de student die past bij jouw vraag, en de senior die meekijkt."):
    return (f'<section class="section section--flush-top"><div class="container"><div class="cta-block"><h2>{title}</h2><p>{text}</p>'
            f'<div class="btn-row">{btn("Vraag een offerte aan", "/offerte-aanvragen/", "navy", "arrow-right", True)}'
            f'{btn("Bel " + PHONE, PHONE_HREF, "navy-outline", "phone", True)}</div></div></div></section>')


# ---------------------------------------------------------------- header en footer
NAV = [("Werkwijze", "/werkwijze/"), ("Over ons", "/over-ons/"), ("Kennisbank", "/kennisbank/"), ("Contact", "/contact/")]


def header(current):
    groups = ""
    for g in GROUPS:
        lis = "".join(f'<li><a href="/{s[0]}/">{s[1]}</a></li>' for s in SPECS if s[4] == g)
        groups += f'<div class="dropdown__group"><p class="dropdown__title">{g}</p><ul>{lis}</ul></div>'
    spec_cur = ' aria-current="page"' if current == "specialisaties" else ""
    cur = ' aria-current="page"'
    links = "".join(f'<li><a href="{u}"{cur if current == n else ""}>{n}</a></li>' for n, u in NAV)
    mob_groups = ""
    for g in GROUPS:
        lis = "".join(f'<li><a href="/{s[0]}/">{s[1]}</a></li>' for s in SPECS if s[4] == g)
        mob_groups += f'<p class="mobile-nav__title">{g}</p><ul>{lis}</ul>'
    mob_links = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in [("Alle specialisaties", "/specialisaties/")] + NAV)
    return f'''<a class="skip-link" href="#main">Naar de inhoud</a>
<header class="header">
  <div class="header__bar">
    <a class="logo" href="/" aria-label="Marketing Student, naar de homepage"><picture><source srcset="/assets/img/logo-220.webp 1x, /assets/img/logo-440.webp 2x" type="image/webp"><img src="/assets/img/logo-220.png" srcset="/assets/img/logo-220.png 1x, /assets/img/logo-440.png 2x" width="110" height="34" alt="Marketing Student"></picture></a>
    <nav class="nav" aria-label="Hoofdmenu"><ul>
      <li class="has-dropdown"><button type="button" aria-expanded="false" aria-controls="dropdown-specialisaties"{spec_cur}>Specialisaties{icon("chevron-down")}</button>
        <div class="dropdown" id="dropdown-specialisaties">{groups}<div class="dropdown__all"><a href="/specialisaties/">Alle specialisaties</a></div></div></li>
      {links}
    </ul></nav>
    <div class="header__actions">
      <a class="header__phone" href="{PHONE_HREF}">{icon("phone")}{PHONE}</a>
      <a class="btn btn--grad header__cta" href="/offerte-aanvragen/">Offerte aanvragen</a>
      <div class="header__mobile">
        <a class="icon-btn icon-btn--light" href="{PHONE_HREF}" aria-label="Bel {PHONE}">{icon("phone")}</a>
        <button class="icon-btn icon-btn--dark" type="button" data-menu-toggle aria-expanded="false" aria-controls="mobile-nav" aria-label="Menu openen">{icon("menu", "icon-open")}{icon("x", "icon-close")}</button>
      </div>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobile-nav">
  <nav aria-label="Mobiel menu">{mob_groups}<p class="mobile-nav__title">Marketing Student</p><ul>{mob_links}</ul>
  {btn("Offerte aanvragen", "/offerte-aanvragen/", "grad", "arrow-right", True)}</nav>
</div>'''


def footer():
    specs = "".join(f'<li><a href="/{s[0]}/">{s[1]}</a></li>' for s in SPECS)
    bedrijf = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in [("Alle specialisaties", "/specialisaties/"), ("Werkwijze", "/werkwijze/"), ("Over ons", "/over-ons/"),
                                                                     ("Kennisbank", "/kennisbank/"), ("Werken als student", "/werken-als-student/"),
                                                                     ("Offerte aanvragen", "/offerte-aanvragen/"), ("Contact", "/contact/")])
    cookie_link = '<button type="button" class="footer__cookie" data-cookie-settings>Cookie-instellingen</button>' if GTM_ID else ""
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__intro"><img src="/assets/img/logo-220.png" srcset="/assets/img/logo-440.png 2x" width="116" height="36" alt="Marketing Student" loading="lazy"><p>Getrainde HBO/WO-marketingstudenten, begeleid door ervaren marketeers. Zonder contract.</p></div>
      <div><h2>Specialisaties</h2><ul class="footer__specs">{specs}</ul></div>
      <div><h2>Marketing Student</h2><ul>{bedrijf}</ul></div>
      <div><h2>Contact</h2><div class="footer__contact">
        <a class="strong" href="{PHONE_HREF}">{icon("phone")}{PHONE}</a>
        <a class="strong" href="mailto:{EMAIL}">{icon("mail")}{EMAIL}</a>
        <span>Ma–do 08:30–17:30, vr 08:30–16:30</span>
        <span>KvK 90875206</span>
        <span>Onderdeel van BlauweLink.nl en Careerguys.nl</span>
      </div></div>
    </div>
    <div class="footer__legal"><span>© {datetime.date.today().year} Marketing Student</span><nav aria-label="Juridisch"><a href="/privacy-policy/">Privacy- en cookiebeleid</a><a href="/sitemap.xml">Sitemap</a>{cookie_link}</nav></div>
  </div>
</footer>'''


def mobile_cta(current):
    if current in ("offerte", "bedankt"):
        return ""
    return f'<div class="mobile-cta">{btn("Bellen", PHONE_HREF, "outline", "phone")}{btn("Offerte", "/offerte-aanvragen/", "grad", "arrow-right")}</div>'


def cookie_banner():
    if not GTM_ID:
        return ""
    return '''<div class="cookie" id="cookie" role="dialog" aria-labelledby="cookie-titel" aria-describedby="cookie-tekst" hidden>
  <div class="cookie__inner">
    <div><strong id="cookie-titel">Cookies voor statistieken</strong>
    <p id="cookie-tekst">We gebruiken analytische cookies om de site te verbeteren. Lees meer in ons <a href="/privacy-policy/">privacy- en cookiebeleid</a>.</p></div>
    <div class="cookie__actions"><button class="btn btn--navy-outline" type="button" data-consent="deny">Weigeren</button><button class="btn btn--grad" type="button" data-consent="grant">Accepteren</button></div>
  </div>
</div>'''


def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css)
    css = css.replace(";}", "}")
    return css.strip()


CSS_INLINE = minify_css((ROOT / "assets/css/style.css").read_text())


def asset_v(rel):
    p = ROOT / rel
    return hashlib.md5(p.read_bytes()).hexdigest()[:8]


# ---------------------------------------------------------------- schema
ORG = SITE + "/#organization"
LOGO_URL = SITE + "/assets/img/logo-440.png"
UREN = [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "08:30", "closes": "17:30"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "08:30", "closes": "16:30"}]
NL = {"@type": "Country", "name": "Nederland"}


def vestiging(slug, plaats, straat, pc):
    return {"@type": "ProfessionalService", "@id": f"{SITE}/#vestiging-{slug}", "name": f"Marketing Student {plaats}",
            "url": SITE + "/contact/", "image": LOGO_URL, "telephone": "+31850608631", "email": EMAIL,
            "address": {"@type": "PostalAddress", "streetAddress": straat, "postalCode": pc, "addressLocality": plaats, "addressCountry": "NL"},
            "openingHoursSpecification": UREN, "parentOrganization": {"@id": ORG}}


BASE_GRAPH = [
    {"@type": "Organization", "@id": ORG, "name": SITE_NAME, "url": SITE + "/",
     "logo": {"@type": "ImageObject", "@id": SITE + "/#logo", "url": LOGO_URL, "width": 440, "height": 138, "caption": SITE_NAME},
     "image": {"@id": SITE + "/#logo"},
     "description": "Getrainde HBO/WO-marketingstudenten voor het mkb, begeleid door ervaren marketeers.",
     "telephone": "+31850608631", "email": EMAIL,
     "address": {"@type": "PostalAddress", "streetAddress": "Koninginnegracht 5", "postalCode": "2514 AA", "addressLocality": "Den Haag", "addressCountry": "NL"},
     "identifier": {"@type": "PropertyValue", "propertyID": "KvK", "value": "90875206"},
     "areaServed": NL, "knowsLanguage": "nl",
     "parentOrganization": [{"@type": "Organization", "name": "BlauweLink", "url": "https://www.blauwelink.nl/"},
                            {"@type": "Organization", "name": "Careerguys", "url": "https://careerguys.nl/"}],
     "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "telephone": "+31850608631", "email": EMAIL,
                      "areaServed": "NL", "availableLanguage": "Dutch", "hoursAvailable": UREN},
     "location": [{"@id": f"{SITE}/#vestiging-den-haag"}, {"@id": f"{SITE}/#vestiging-mijdrecht"}]},
    {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": SITE_NAME, "inLanguage": "nl-NL", "publisher": {"@id": ORG}},
    vestiging("den-haag", "Den Haag", "Koninginnegracht 5", "2514 AA"),
    vestiging("mijdrecht", "Mijdrecht", "Industrieweg 6", "3641 RM"),
]


def ld_webpage(url, title, desc, typ="WebPage", crumb=True, main=None):
    n = {"@type": typ, "@id": url + "#webpage", "url": url, "name": title, "description": desc, "inLanguage": "nl-NL",
         "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": ORG}, "primaryImageOfPage": {"@id": SITE + "/#logo"}}
    if crumb:
        n["breadcrumb"] = {"@id": url + "#breadcrumb"}
    if main:
        n["mainEntity"] = {"@id": main}
    return n


def ld_crumbs(url, items):
    return {"@type": "BreadcrumbList", "@id": url + "#breadcrumb",
            "itemListElement": [{"@type": "ListItem", "position": i, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items, 1)]}


def ld_faq(url, items):
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url + "#webpage"},
            "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in items]}


# ---------------------------------------------------------------- layout
def layout(path, title, desc, body, current, graph, noindex=False, og_type="website"):
    url = SITE + path
    js_v = asset_v("assets/js/main.js")
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    ld = json.dumps({"@context": "https://schema.org", "@graph": BASE_GRAPH + graph}, ensure_ascii=False, separators=(",", ":"))
    gtm_head = gtm_body = ""
    if GTM_ID:
        gtm_head = (f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}"
                    f"gtag('consent','default',{{'ad_storage':'denied','ad_user_data':'denied','ad_personalization':'denied','analytics_storage':'denied','wait_for_update':500}});"
                    f"try{{if(localStorage.getItem('ms_consent')==='granted')gtag('consent','update',{{'analytics_storage':'granted'}})}}catch(e){{}}</script>\n"
                    f"<script>window.addEventListener('load',function(){{setTimeout(function(){{(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}')}},1500)}});</script>\n")
        gtm_body = f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>\n'
    canonical = "" if noindex else f'<link rel="canonical" href="{url}">\n'
    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
{canonical}<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="nl_NL">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Marketing Student: marketing uitbesteden aan een student">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f2741">
<link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/plus-jakarta-sans-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS_INLINE}</style>
<script type="application/ld+json">{ld}</script>
{gtm_head}</head>
<body>
{gtm_body}{header(current)}
<main id="main">
{body}
</main>
{footer()}
{mobile_cta(current)}
{cookie_banner()}
<script src="/assets/js/main.js?v={js_v}" defer></script>
</body>
</html>
'''


# ---------------------------------------------------------------- pagina's
def hero(crumb_items, h1a, h1b, lead_txt, extra="", form=None, home=False, cls=""):
    c = crumbs(crumb_items) if crumb_items else ""
    g = f' <span class="grad">{h1b}</span>' if h1b else ""
    text = f'<div class="hero__text">{c}<h1>{h1a}{g}</h1><p class="lead">{lead_txt}</p>{extra}</div>'
    inner = f'<div class="hero__grid">{text}{form}</div>' if form else text
    return f'<section class="hero glow-right{" hero--home" if home else ""}{" " + cls if cls else ""}"><div class="container">{inner}</div></section>'


def page_home():
    path = "/"
    title = "Marketing uitbesteden? Huur een marketing student in"
    desc = "Marketing uitbesteden aan getrainde HBO/WO-studenten, begeleid door ervaren marketeers. Geen contract. Vraag vrijblijvend een offerte aan."
    faq_html, faq_items = faq_block("Vragen over marketing uitbesteden", FAQ_HOME)
    body = hero(None, "Marketing uitbesteden", "aan een student",
                "Marketing student inhuren in plaats van een bureau: getrainde HBO/WO-studenten die direct meebouwen aan je online marketing. Altijd begeleid door ervaren marketeers, zonder contract.",
                hero_buttons(), offerte_form(""), home=True)
    body += trustbar()
    body += showcase(HOME_SC)
    body += section(section_head("Specialisaties", "Kies de student die past bij jouw vraag", "Elke specialisatie heeft een eigen pagina met taken en voorbeelden. Zo vind je sneller wat je zoekt.") + spec_grid(), "glow-left")
    body += section(section_head("Samenwerken", "Twee manieren om samen te werken", "Structureel meewerken of één afgebakende opdracht. Je kiest wat past, zonder contract.") + plans())
    body += section(section_head("Werkwijze", "Zo staat jouw student klaar") + steps())
    body += section(section_head("Vergelijking", "Student, freelance marketeer of bureau?", "Een eerlijke vergelijking op de punten die voor het mkb tellen.") + compare(COMPARE), "glow-right")
    body += section(section_head("Tools", "Onze studenten werken in jouw tools", "Ze stappen in je bestaande accounts. Jij blijft eigenaar van alle data.") + platform_tiles(HOME_PLATFORMS))
    body += section(section_head("Kennisbank", "Slimmer inhuren begint hier") + post_cards(["freelance-marketeer-of-marketing-student", "welke-social-media-kiezen", "wat-voor-type-marketeers-zijn-er"])
                    + f'<div class="btn-row" style="justify-content:center;margin-top:28px">{btn("Naar de kennisbank", "/kennisbank/", "outline", "arrow-right")}</div>')
    body += faq_html
    body += cta_block()
    graph = [ld_webpage(SITE + "/", title, desc, crumb=False, main=ORG), ld_faq(SITE + "/", faq_items)]
    return path, title, desc, body, "home", graph


def page_dienst(slug):
    d = DIENST[slug]
    _, label, kind, card, _ = SPEC[slug]
    path = f"/{slug}/"
    url = SITE + path
    noun = d["noun"]
    Noun = noun[0].upper() + noun[1:]
    FAQ_ONDERWERP = {"Social media": "social media uitbesteden", "Content": "contentmarketing", "Branding": "een huisstijl",
                     "E-mailmarketing": "e-mailmarketing", "LinkedIn": "LinkedIn-marketing", "TikTok": "TikTok uitbesteden",
                     "Instagram": "Instagram uitbesteden"}
    lab = FAQ_ONDERWERP.get(d["short"], d["short"] if d["short"] in ("SEO", "Google Ads", "AI", "Claude") else d["short"])
    if d["short"] in ("SEO", "Google Ads", "AI", "Claude", "WordPress", "Shopify"):
        lab = "een " + d["noun"]
    faq_html, faq_items = faq_block(f"Vragen over {lab}", [q for q, _ in d["faq"]], {q: a for q, a in d["faq"] if a})
    body = hero([("Home", "/"), ("Specialisaties", "/specialisaties/"), (label, path)], d["h1"][0], d["h1"][1], d["lead"],
                hero_buttons(), offerte_form(slug))
    body += trustbar()
    if d["sc"]:
        body += showcase(SHOWCASES[d["sc"]])
    tasks = "".join(f'<div class="card"><span class="card__icon">{icon(i)}</span><h3>{t}</h3><p>{x}</p></div>' for i, t, x in d["tasks"])
    body += section(section_head("Taken", f"Wat een {noun} voor je doet", "Concreet werk, afgestemd op jouw doelen. Jij bepaalt de prioriteiten, de senior bewaakt de aanpak.")
                    + f'<div class="grid grid--3">{tasks}</div><div class="btn-row" style="justify-content:center;margin-top:32px">{btn("Bespreek je vraag", "#offerte", "grad", "arrow-right")}</div>', "glow-left")
    if d["platforms"]:
        body += section(section_head("Platformen", "De tools die we gebruiken") + platform_tiles(PLATFORMS[d["platforms"]]))
    body += section(section_head("Samenwerken", f"Zo werk je met een {noun}", "Twee werkvormen, allebei zonder contract. Je krijgt altijd eerst een offerte op maat.") + plans(Noun))
    seo = slug == "seo-specialist-inhuren"
    body += section(section_head("Vergelijking", "SEO-student, SEO-freelancer of bureau?" if seo else "Student, freelancer of bureau?") + compare(COMPARE_SEO if seo else COMPARE), "glow-right")
    body += faq_html
    body += section(section_head("Kennisbank", "Meer lezen") + post_cards(REL.get(slug, REL_DEFAULT)))
    body += cta_block(d["cta"], "Vertel wat je nodig hebt. Je krijgt een voorstel met de student en de senior die jouw vraag oppakken.")
    graph = [ld_webpage(url, d["title"], d["meta"], main=url + "#service"),
             ld_crumbs(url, [("Home", "/"), ("Specialisaties", "/specialisaties/"), (label, path)]),
             {"@type": "Service", "@id": url + "#service", "name": label, "serviceType": label, "description": d["meta"], "url": url,
              "provider": {"@id": ORG}, "areaServed": NL, "category": d["short"],
              "audience": {"@type": "BusinessAudience", "audienceType": "mkb-ondernemers en marketingmanagers"}},
             ld_faq(url, faq_items)]
    return path, d["title"], d["meta"], body, "specialisaties", graph


def simple_page(path, crumb, h1a, h1b, lead_txt, title, desc, sections_html, current, typ="WebPage", faq=None, extra_graph=(), hero_extra=None, form=None, noindex=False):
    url = SITE + path
    body = hero([("Home", "/"), (crumb, path)] if crumb else None, h1a, h1b, lead_txt, hero_extra if hero_extra is not None else hero_buttons(href="/offerte-aanvragen/"), form)
    body += sections_html
    graph = [ld_webpage(url, title, desc, typ, crumb=bool(crumb))]
    if crumb:
        graph.append(ld_crumbs(url, [("Home", "/"), (crumb, path)]))
    if faq:
        faq_html, items = faq
        body += faq_html
        graph.append(ld_faq(url, items))
    graph += list(extra_graph)
    return path, title, desc, body, current, graph, noindex


def page_specialisaties():
    items = [{"@type": "ListItem", "position": i, "url": f"{SITE}/{s[0]}/", "name": s[1]} for i, s in enumerate(SPECS, 1)]
    secs = section(section_head("Overzicht", "Kies de student die past bij jouw vraag") + spec_grid(), "section--flush-top")
    secs += section(section_head("Samenwerken", "Twee manieren om samen te werken") + plans(href="/offerte-aanvragen/"))
    faq = faq_block("Vragen over de specialisaties", ["Welke specialisatie past bij mij?", "Kan één student meerdere taken doen?", "Wie begeleidt de student?", "Zit ik vast aan een contract?"])
    secs_after = cta_block()
    p = simple_page("/specialisaties/", "Specialisaties", "Alle specialisaties", "op een rij",
                    "Dertien specialisaties, van SEO tot content. Elke student is getraind in zijn vak en werkt onder een ervaren marketeer. Kies wat je nodig hebt, of laat ons meedenken.",
                    "Alle specialisaties | Marketing Student",
                    "Dertien specialisaties, van SEO tot content. Getrainde marketingstudenten, begeleid door ervaren marketeers. Bekijk welke student past.",
                    secs, "specialisaties", "CollectionPage", faq,
                    [{"@type": "ItemList", "@id": SITE + "/specialisaties/#lijst", "name": "Specialisaties", "numberOfItems": len(items), "itemListElement": items}])
    return p[0], p[1], p[2], p[3] + secs_after, p[4], p[5], p[6]


def page_werkwijze():
    secs = section(section_head("Stappen", "In drie stappen aan de slag") + steps(), "section--flush-top")
    secs += section(section_head("Samenwerken", "Twee manieren om samen te werken") + plans(href="/offerte-aanvragen/"))
    secs += section(section_head("Vergelijking", "Student, freelance marketeer of bureau?") + compare(COMPARE), "glow-right")
    faq = faq_block("Vragen over de werkwijze", ["Hoe snel kan een student beginnen?", "Werken studenten remote of op locatie?", "Wat als de student niet bevalt?", "Zit ik vast aan een contract?"])
    p = simple_page("/werkwijze/", "Werkwijze", "Zo werkt marketing", "uitbesteden",
                    "Van eerste vraag tot vaste student in je team. Een senior marketeer kijkt altijd mee, en je zit nergens aan vast.",
                    "Zo werkt marketing uitbesteden | Marketing Student",
                    "Van eerste vraag tot vaste student in je team: zo werkt marketing uitbesteden aan een student. Begeleid door seniors, zonder contract.",
                    secs, "Werkwijze", faq=faq)
    return p[0], p[1], p[2], p[3] + cta_block(), p[4], p[5], p[6]


def page_over():
    princ = [("users", "Altijd senior begeleiding", "Geen student werkt alleen. Een ervaren marketeer controleert het werk en stuurt bij."),
             ("clock", "Transparant in tijd", "Je ziet waar de uren naartoe gaan en wat ze opleveren."),
             ("target", "Resultaatgericht", "We sturen op wat jouw bedrijf verder helpt, niet op uren."),
             ("zap", "Frisse blik", "Studenten kennen de nieuwste tools en platforms, en kijken met nieuwe ogen naar je marketing.")]
    cards = "".join(f'<div class="card"><span class="card__icon">{icon(i)}</span><h3>{t}</h3><p>{x}</p></div>' for i, t, x in princ)
    offices = "".join(f'<div class="card office"><span class="card__icon">{icon("map-pin")}</span><h3>{p}</h3><address>{a}<br>{c}</address></div>'
                      for p, a, c in [("Den Haag", "Koninginnegracht 5", "2514 AA Den Haag"), ("Mijdrecht", "Industrieweg 6", "3641 RM Mijdrecht")])
    secs = section(section_head("Principes", "Vier afspraken waar je op kunt rekenen") + f'<div class="grid grid--4">{cards}</div>', "section--flush-top")
    secs += section(section_head("Kantoren", "Hier vind je ons") + f'<div class="grid grid--2">{offices}</div>')
    secs += cta_block("Zin om kennis te maken?")
    return simple_page("/over-ons/", "Over ons", "Getrainde studenten,", "begeleid door seniors",
                       "Marketing Student is opgezet door een SEO-bureau en een brandingbureau: BlauweLink.nl en Careerguys.nl. Wij koppelen getrainde HBO/WO-studenten aan het mkb, met ervaren marketeers achter de schermen.",
                       "Over Marketing Student | BlauweLink en Careerguys",
                       "Marketing Student is opgezet door BlauweLink en Careerguys: getrainde marketingstudenten voor het mkb, begeleid door ervaren marketeers.",
                       secs, "Over ons", "AboutPage")


def page_contact():
    n = uid("c")
    form = f'''{form_open("contact", "contact/")}
  <h2>Stuur ons een bericht</h2>
  <div class="form-grid form-grid--2">
    {field(f"naam-{n}", "Naam", ph="Voor- en achternaam", ac="name")}
    {field(f"bedrijf-{n}", "Bedrijfsnaam", ph="Naam van je bedrijf", ac="organization", required=False)}
    {field(f"telefoon-{n}", "Telefoon", "tel", "06 12345678", ac="tel", required=False)}
    {field(f"email-{n}", "E-mailadres", "email", "naam@bedrijf.nl", ac="email")}
    {field(f"bericht-{n}", "Bericht", ph="Waar kunnen we je mee helpen?", full=True, textarea=True)}
  </div>
  <button class="btn btn--grad form-submit" type="submit">Verstuur bericht{icon("arrow-right")}</button>
  {PRIVACY_NOTE}
</form>'''
    cards = f'''<div class="contact-cards">
  <div class="contact-card">{icon("phone")}<h2>Bellen</h2><a href="{PHONE_HREF}">{PHONE}</a><span>Ma–do 08:30–17:30, vr 08:30–16:30</span></div>
  <div class="contact-card">{icon("mail")}<h2>Mailen</h2><a href="mailto:{EMAIL}">{EMAIL}</a></div>
  <div class="contact-card">{icon("map-pin")}<h2>Langskomen</h2><strong>Den Haag of Mijdrecht</strong><span>Op afspraak. <a href="/over-ons/">Bekijk de adressen</a></span></div>
</div>'''
    secs = section(f'<div class="contact-grid">{form}{cards}</div>', "section--flush-top")
    return simple_page("/contact/", "Contact", "Neem contact op", "", "Een vraag over een student, een specialisatie of een lopende samenwerking? Bel, mail of stuur een bericht.",
                       "Contact | Marketing Student",
                       "Bel 085-060 8631, mail info@marketing-student.nl of stuur een bericht. Vestigingen in Den Haag en Mijdrecht.",
                       secs, "Contact", "ContactPage", hero_extra="")


def page_offerte():
    secs = section(section_head("Wat er daarna gebeurt", "Van aanvraag tot start") + steps())
    return simple_page("/offerte-aanvragen/", "Offerte aanvragen", "Offerte aanvragen", "",
                       "Vertel wat je nodig hebt. Je krijgt een vrijblijvend voorstel met de student en de senior die jouw vraag oppakken.",
                       "Offerte aanvragen | Marketing Student",
                       "Vraag vrijblijvend een offerte aan voor een marketingstudent. Begeleid door ervaren marketeers, geen contract en kosteloze vervanging.",
                       secs, "offerte", hero_extra="", form=offerte_form("offerte-aanvragen/"))


def page_kennisbank():
    items = [{"@type": "ListItem", "position": i, "url": f"{SITE}/kennisbank/{a['slug']}/", "name": a["titel"]} for i, a in enumerate(ARTIKELEN, 1)]
    secs = section('<h2 class="sr-only">Alle artikelen</h2>' + post_cards([a["slug"] for a in ARTIKELEN]), "section--flush-top")
    secs += cta_block()
    return simple_page("/kennisbank/", "Kennisbank", "Kennisbank", "", "Praktische artikelen over marketing uitbesteden, SEO en social media.",
                       "Kennisbank marketing uitbesteden | Marketing Student",
                       "Praktische artikelen over marketing uitbesteden, SEO, social media en het kiezen van de juiste marketeer.",
                       secs, "Kennisbank", "CollectionPage", hero_extra="",
                       extra_graph=[{"@type": "ItemList", "@id": SITE + "/kennisbank/#lijst", "name": "Artikelen", "numberOfItems": len(items), "itemListElement": items}])


def slugify(t):
    t = t.lower().replace("?", "")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def page_artikel(a):
    path = f"/kennisbank/{a['slug']}/"
    url = SITE + path
    toc, prose = [], [f'<p>{a["intro"]}</p>']
    for i, (kop, alineas) in enumerate(a["secties"]):
        hid = slugify(kop)
        toc.append(f'<li><a href="#{hid}">{kop}</a></li>')
        prose.append(f'<h2 id="{hid}">{kop}</h2>')
        for al in alineas:
            if al.startswith("- "):
                prose.append("<ul>" + "".join(f"<li>{x[2:]}</li>" for x in al.split("\n")) + "</ul>")
            else:
                prose.append(f"<p>{al}</p>")
        if i == 1 and a["dienst"]:
            _, label, *_ = SPEC[a["dienst"]]
            prose.append(f'<div class="article-cta"><strong>{label}?</strong><span>Een getrainde student, begeleid door een senior. Geen contract.</span>'
                         f'{btn("Meer over " + label[0].lower() + label[1:] if not label.startswith(("SEO", "Google", "AI", "Claude", "WordPress", "TikTok", "Instagram", "LinkedIn", "Shopify")) else "Meer over " + label, "/" + a["dienst"] + "/", "grad", "arrow-right")}</div>')
    if not a["dienst"]:
        prose.append(f'<div class="article-cta"><strong>Hulp nodig bij je marketing?</strong><span>Een getrainde student, begeleid door een senior. Geen contract.</span>'
                     f'{btn("Bekijk alle specialisaties", "/specialisaties/", "grad", "arrow-right")}</div>')
    aside = f'<aside class="aside-sticky"><nav class="toc" aria-label="Inhoud van dit artikel"><h2>In dit artikel</h2><ol>{"".join(toc)}</ol></nav></aside>'
    meta_line = f'<p class="meta-line">Redactie Marketing Student · <time datetime="{PUBLISHED}">25 september 2026</time></p>'
    body = hero([("Home", "/"), ("Kennisbank", "/kennisbank/"), (a["titel"], path)], a["titel"], "", a["meta"], meta_line, cls="hero--article")
    body += section(f'<div class="article-grid"><article class="prose">{"".join(prose)}</article>{aside}</div>', "section--flush-top")
    rel = [x["slug"] for x in ARTIKELEN if x["slug"] != a["slug"]][:3]
    body += section(section_head("Verder lezen", "Meer uit de kennisbank") + post_cards(rel))
    body += cta_block()
    graph = [ld_webpage(url, a["title"], a["meta"], main=url + "#artikel"),
             ld_crumbs(url, [("Home", "/"), ("Kennisbank", "/kennisbank/"), (a["titel"], path)]),
             {"@type": "Article", "@id": url + "#artikel", "headline": a["titel"], "description": a["meta"], "image": SITE + "/assets/img/og-image.png",
              "datePublished": PUBLISHED, "dateModified": PUBLISHED, "inLanguage": "nl-NL",
              "author": {"@type": "Organization", "@id": ORG, "name": SITE_NAME}, "publisher": {"@id": ORG},
              "mainEntityOfPage": {"@id": url + "#webpage"}}]
    if a["dienst"]:
        graph[-1]["about"] = {"@id": f"{SITE}/{a['dienst']}/#service"}
    return path, a["title"], a["meta"], body, "Kennisbank", graph, False, "article"


def page_student():
    n = uid("s")
    form = f'''<div id="aanmelden">{form_open("student-aanmelding", "werken-als-student/")}
  <h2>Meld je aan</h2>
  <div class="form-grid">
    {field(f"naam-{n}", "Naam", ph="Voor- en achternaam", ac="name")}
    {field(f"email-{n}", "E-mailadres", "email", "naam@student.nl", ac="email")}
    {field(f"opleiding-{n}", "Opleiding en onderwijsinstelling", ph="Bijvoorbeeld: Commerciële Economie, HvA")}
    {field(f"profiel-{n}", "LinkedIn-profiel of portfolio", "url", "https://", required=False)}
  </div>
  <button class="btn btn--grad form-submit" type="submit">Aanmelden{icon("arrow-right")}</button>
  <p class="form-note">We gebruiken je gegevens alleen voor je aanmelding. Lees ons <a href="/privacy-policy/">privacybeleid</a>.</p>
</form></div>'''
    krijg = [("users", "Begeleiding door seniors", "Je werkt onder een ervaren marketeer die je feedback geeft."),
             ("building", "Echte klanten", "Je werkt voor mkb-bedrijven, niet aan oefenopdrachten."),
             ("clock", "Flexibel naast je studie", "In overleg bepaal je hoeveel uur je per week werkt."),
             ("trending", "Groei in je vak", "Je leert de tools en methodes die marketeers dagelijks gebruiken.")]
    cards = "".join(f'<div class="card"><span class="card__icon">{icon(i)}</span><h3>{t}</h3><p>{x}</p></div>' for i, t, x in krijg)
    secs = section(section_head("Wat je krijgt", "Waarom studenten bij ons werken") + f'<div class="grid grid--4">{cards}</div>')
    faq = faq_block("Vragen van studenten", ["Wat zijn de eisen?", "Werk ik remote of op locatie?", "Hoeveel uur per week werk ik?"])
    return simple_page("/werken-als-student/", "Werken als student", "Marketing bijbaan", "naast je studie",
                       "Studeer je marketing, communicatie of iets vergelijkbaars op HBO- of WO-niveau? Werk voor echte klanten, begeleid door ervaren marketeers.",
                       "Marketing bijbaan naast je studie | Marketing Student",
                       "Studeer je marketing of communicatie op HBO- of WO-niveau? Werk naast je studie voor echte klanten, begeleid door ervaren marketeers.",
                       secs, None, faq=faq, hero_extra="", form=form)


PRIVACY = (ROOT / "privacy.html").read_text() if (ROOT / "privacy.html").exists() else ""


def page_privacy():
    secs = section(f'<div class="legal">{PRIVACY}</div>', "section--flush-top")
    return simple_page("/privacy-policy/", "Privacy- en cookiebeleid", "Privacy- en cookiebeleid", "", "Hoe we omgaan met je persoonsgegevens en cookies.",
                       "Privacy- en cookiebeleid | Marketing Student",
                       "Lees hoe Marketing Student omgaat met je persoonsgegevens en cookies, welke rechten je hebt en hoe je contact met ons opneemt.",
                       secs, None, hero_extra="")


def page_bedankt():
    extra = f'<div class="btn-row btn-row--stack">{btn("Naar de homepage", "/", "grad", "arrow-right", True)}{btn("Bel " + PHONE, PHONE_HREF, "outline", "phone", True)}</div>'
    return simple_page("/bedankt/", None, "Bedankt,", "we hebben je aanvraag ontvangen", "We nemen zo snel mogelijk contact met je op. Liever direct schakelen? Bel ons.",
                       "Bedankt | Marketing Student", "Bedankt voor je aanvraag bij Marketing Student. We nemen zo snel mogelijk contact met je op.",
                       "", "bedankt", hero_extra=extra, noindex=True)


def page_404():
    extra = f'<div class="btn-row btn-row--stack">{btn("Naar de homepage", "/", "grad", "arrow-right", True)}{btn("Alle specialisaties", "/specialisaties/", "outline", None, True)}</div>'
    return simple_page("/404.html", None, "Deze pagina", "bestaat niet (meer)", "De pagina die je zoekt is verplaatst of verwijderd. Kies een specialisatie of ga terug naar de homepage.",
                       "Pagina niet gevonden | Marketing Student", "Deze pagina bestaat niet (meer). Ga terug naar de homepage of kies een specialisatie van Marketing Student.",
                       section('<h2 class="sr-only">Specialisaties</h2>' + spec_grid(), "section--flush-top"), None, hero_extra=extra, noindex=True)


# ---------------------------------------------------------------- redirects
REDIRECTS = [
    ("/seo-student-inhuren/", "/seo-specialist-inhuren/"),
    ("/google-ads-student-inhuren/", "/google-ads-specialist-inhuren/"),
    ("/sea-student-inhuren/", "/google-ads-specialist-inhuren/"),
    ("/social-media-student-inhuren/", "/social-media-uitbesteden/"),
    ("/linkbuilding-student-inhuren/", "/seo-specialist-inhuren/"),
    ("/ai-specialist-student-inhuren/", "/ai-specialist-inhuren/"),
    ("/claude-specialist-student-inhuren/", "/claude-specialist-inhuren/"),
    ("/content-creator-student-inhuren/", "/contentmarketing-uitbesteden/"),
    ("/content-creatie-social-media-student-inhuren/", "/contentmarketing-uitbesteden/"),
    ("/branding-student-inhuren/", "/huisstijl-laten-maken/"),
    ("/email-marketing-student-inhuren/", "/email-marketing-uitbesteden/"),
    ("/e-mailmarketing-student-inhuren/", "/email-marketing-uitbesteden/"),
    ("/wordpress-student-inhuren/", "/wordpress-specialist-inhuren/"),
    ("/tiktok-student-inhuren/", "/tiktok-uitbesteden/"),
    ("/instagram-student-inhuren/", "/instagram-uitbesteden/"),
    ("/linkedin-student-inhuren/", "/linkedin-marketing-uitbesteden/"),
    ("/shopify-student-inhuren/", "/shopify-specialist-inhuren/"),
    ("/studenten/", "/specialisaties/"),
    ("/blog/", "/kennisbank/"),
    ("/marketing-blog/", "/kennisbank/"),
    ("/welke-social-media-is-het-populairst-onder-de-studenten/", "/kennisbank/welke-social-media-kiezen/"),
    ("/wat-voor-type-marketeers-zijn-er/", "/kennisbank/wat-voor-type-marketeers-zijn-er/"),
    ("/wat-doet-een-head-of-marketing/", "/kennisbank/wat-doet-een-head-of-marketing/"),
    ("/marketeer-inhuren/", "/"),
    ("/marketing-opdracht-uitbesteden/", "/werkwijze/"),
    ("/word-student/", "/werken-als-student/"),
    ("/cases/", "/"),
    ("/marketing-bureau-den-haag/", "/contact/"),
    ("/marketing-bureau-mijdrecht/", "/contact/"),
    ("/privacy/", "/privacy-policy/"),
    ("/author/blauwelink/", "/over-ons/"),
    ("/sitemap_index.xml", "/sitemap.xml"),
    ("/page-sitemap.xml", "/sitemap.xml"),
    ("/post-sitemap.xml", "/sitemap.xml"),
    ("/category-sitemap.xml", "/sitemap.xml"),
    ("/wp-sitemap.xml", "/sitemap.xml"),
    ("/feed/", "/kennisbank/"),
    ("/comments/feed/", "/kennisbank/"),
]
GONE = ["/test-bericht/", "/test-bericht-2/", "/category/uncategorized/", "/wp-json/*", "/xmlrpc.php", "/wp-admin/*", "/wp-login.php"]
BLOCK = ["/build.py", "/artikelen.py", "/diensten_data.py", "/faq_data.py", "/brands.json", "/privacy.html", "/README.md", "/check.py"]


# ---------------------------------------------------------------- bouwen
def write(path, htmltext):
    out = ROOT / ("404.html" if path == "/404.html" else path.strip("/") + "/index.html" if path != "/" else "index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(htmltext, encoding="utf-8")
    return out


def main():
    pages = [page_home()] + [page_dienst(s[0]) for s in SPECS]
    pages += [page_specialisaties(), page_werkwijze(), page_over(), page_contact(), page_offerte(), page_kennisbank()]
    pages += [page_artikel(a) for a in ARTIKELEN]
    pages += [page_student(), page_privacy(), page_bedankt(), page_404()]
    sitemap = []
    for p in pages:
        path, title, desc, body, current, graph = p[:6]
        noindex = p[6] if len(p) > 6 else False
        og = p[7] if len(p) > 7 else "website"
        write(path, layout(path, title, desc, body, current, graph, noindex, og))
        if not noindex:
            sitemap.append(path)
    urls = "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in sitemap)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /bedankt/\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    red = "# Gegenereerd door build.py. Pas REDIRECTS in build.py aan, niet dit bestand.\n\n"
    red += "# Netlify-subdomein naar het hoofddomein (voorkomt dubbele content)\n"
    red += "https://marketing-student.netlify.app/*  https://marketing-student.nl/:splat  301!\n"
    red += "http://marketing-student.netlify.app/*   https://marketing-student.nl/:splat  301!\n\n"
    red += "# Broncode niet uitleveren\n"
    red += "".join(f"{b:<62} /404.html  404!\n" for b in BLOCK)
    red += "\n# Oude URL's van de WordPress-site (permanent)\n"
    red += "".join(f"{a:<62} {b:<46} 301!\n" for a, b in REDIRECTS)
    red += "\n# Definitief verwijderd\n" + "".join(f"{g:<62} /404.html  410!\n" for g in GONE)
    (ROOT / "_redirects").write_text(red, encoding="utf-8")
    (ROOT / "netlify.toml").write_text('''# De HTML wordt lokaal gebouwd met `python3 build.py` en staat in de repository.
# Netlify publiceert alleen; er is bewust geen bouwstap.
[build]
  publish = "."

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    X-Frame-Options = "SAMEORIGIN"
    Permissions-Policy = "camera=(), microphone=(), geolocation=()"
    Strict-Transport-Security = "max-age=31536000; includeSubDomains"
''', encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(json.dumps({"name": SITE_NAME, "short_name": SITE_NAME, "start_url": "/", "display": "browser",
                                                       "background_color": "#0f2741", "theme_color": "#0f2741",
                                                       "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                                                                 {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1), encoding="utf-8")
    llms = [f"# {SITE_NAME}", "", "> Getrainde HBO/WO-marketingstudenten voor het mkb, begeleid door ervaren marketeers. Geen contract, kosteloze vervanging. Onderdeel van BlauweLink.nl en Careerguys.nl.", "",
            f"Contact: {PHONE}, {EMAIL}. Vestigingen in Den Haag en Mijdrecht.", "", "## Specialisaties", ""]
    llms += [f"- [{s[1]}]({SITE}/{s[0]}/): {s[3]}" for s in SPECS]
    llms += ["", "## Kennisbank", ""] + [f"- [{a['titel']}]({SITE}/kennisbank/{a['slug']}/): {meta_short(a['meta'])}" for a in ARTIKELEN]
    llms += ["", "## Overig", "", f"- [Werkwijze]({SITE}/werkwijze/)", f"- [Over ons]({SITE}/over-ons/)", f"- [Offerte aanvragen]({SITE}/offerte-aanvragen/)", f"- [Contact]({SITE}/contact/)", ""]
    (ROOT / "llms.txt").write_text("\n".join(llms), encoding="utf-8")
    print(f"{len(pages)} pagina's gebouwd, {len(sitemap)} in de sitemap")


if __name__ == "__main__":
    main()
