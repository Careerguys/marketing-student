"""Meldt nieuwe en gewijzigde pagina's bij IndexNow (Bing, Yandex, Seznam, Naver).

Gebruik, na een push die live staat:
    python3 tools/indexnow.py          # alleen pagina's die sinds de vorige melding zijn gewijzigd
    python3 tools/indexnow.py --all    # alle pagina's uit de sitemap

Vergelijkt lastmod.json met tools/indexnow-sent.json en werkt dat bestand daarna bij.
De sleutel staat in /<sleutel>.txt in de root van de site.
"""
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://marketing-student.nl"
SENT = ROOT / "tools" / "indexnow-sent.json"

key_files = [f for f in ROOT.glob("*.txt") if len(f.stem) == 32 and f.read_text().strip() == f.stem]
if len(key_files) != 1:
    sys.exit("Geen (of meer dan één) IndexNow-sleutelbestand in de root gevonden.")
KEY = key_files[0].stem

lastmod = json.loads((ROOT / "lastmod.json").read_text())
sent = json.loads(SENT.read_text()) if SENT.exists() else {}
paths = sorted(lastmod) if "--all" in sys.argv else sorted(p for p, v in lastmod.items() if sent.get(p) != v["h"])
if not paths:
    print("Niets gewijzigd sinds de vorige melding.")
    sys.exit()

body = json.dumps({"host": "marketing-student.nl", "key": KEY, "keyLocation": f"{SITE}/{KEY}.txt",
                   "urlList": [SITE + p for p in paths]}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req, timeout=30) as r:
    print(f"IndexNow: {r.status} voor {len(paths)} URL's")
    if r.status in (200, 202):
        SENT.write_text(json.dumps({p: v["h"] for p, v in lastmod.items()}, indent=1, sort_keys=True) + "\n")
