# marketing-student.nl

Statische website voor Marketing Student. Geen CMS en geen framework: alleen Python 3 om te bouwen.

## Werkwijze

Bewerk nooit de HTML direct. Die wordt bij elke bouw overschreven.

```bash
python3 build.py   # bouwt alle pagina's, sitemap.xml, robots.txt, _redirects, netlify.toml, llms.txt
python3 check.py   # controleert koppen, titles, descriptions, links, schema, redirects en plaatshouders
```

Publiceer alleen als `check.py` 0 problemen meldt.

| Bestand | Waarvoor |
|---|---|
| `build.py` | Opbouw, componenten, navigatie, schema, redirects |
| `diensten_data.py` | Teksten per dienstpagina: title, meta, H1, taken, FAQ-vragen |
| `faq_data.py` | Antwoorden op alle FAQ-vragen (één bron voor pagina en schema) |
| `artikelen.py` | Kennisbank-artikelen |
| `privacy.html` | Tekst privacy- en cookiebeleid |
| `assets/css/style.css` | Alle opmaak |
| `assets/js/main.js` | Menu, formuliercontrole, cookiebanner |

## Afspraken

- Geen prijzen op de site.
- Geen verzonnen reviews, cijfers of klantnamen.
- Koppen maximaal twee regels, ook op 320 px breed.
- Contrast minimaal 4,5:1. Blauw `#60a6d9` alleen op `#0f2741`, niet op `#143c59`.
- Nieuwe of gewijzigde URL: altijd een 301 in `REDIRECTS` in `build.py`.

## Tracking

Zet de Tag Manager-ID in `GTM_ID` in `build.py`. Dan komen GTM (met consent mode, standaard geweigerd) en de cookiebanner vanzelf mee. Leeg betekent geen tracking en geen banner.

Gebeurtenissen in de dataLayer: `form_submit`, `phone_click`, `email_click`. Formulieren sturen na verzending door naar `/bedankt/`.

## Formulieren

Netlify Forms: `offerte`, `contact` en `student-aanmelding`. Formulierdetectie staat aan; meldingen van nieuwe inzendingen gaan naar marketing@blauwelink.nl (Netlify, project `marketing-student`, Forms).

## Publiceren

Netlify-project `marketing-student` (https://marketing-student.netlify.app) publiceert vanaf de `main`-branch van github.com/Careerguys/marketing-student. De repository is openbaar: op het huidige Netlify-abonnement worden bij privé-repositories alleen commits van één GitHub-gebruiker gebouwd. Er is geen bouwstap op Netlify: de gebouwde HTML staat in de repository.
