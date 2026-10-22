# Verbeteringen van bestaande artikelen na een top-3-analyse (audit 2026-10-22).
# Per slug: nieuwe secties (ingevoegd vóór de laatste sectie), extra FAQ en de datum van bijwerken.
# Een alinea die met "<table" begint, wordt als tabel getoond; met "- " als lijst.

UPGRADE = {}


def upgrade(a):
    u = UPGRADE.get(a["slug"])
    if not u:
        return a
    a = dict(a)
    secties = list(a["secties"])
    for kop, extra in u.get("aanvullen", {}).items():
        secties = [(k, list(p) + extra) if k == kop else (k, p) for k, p in secties]
    a["secties"] = secties[:-1] + u.get("secties", []) + secties[-1:]
    a["faq"] = list(a["faq"]) + u.get("faq", [])
    if u.get("intro"):
        a["intro"] = u["intro"]
    a["bijgewerkt"] = u["bijgewerkt"]
    return a
