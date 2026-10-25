# Verbeteringen van bestaande artikelen na een top-3-analyse (audit 2026-10-22).
# Per slug: nieuwe secties (ingevoegd vóór de laatste sectie), aanvullingen op bestaande secties,
# extra FAQ en de datum van bijwerken. Een alinea die met "<table" begint, wordt als tabel getoond; met "- " als lijst.
# Huisstijl: geen dubbele punt in koppen, geen komma voor "en", geen em-streepjes, geen bedragen.

UPGRADE = {
    "verschil-seo-en-sea": dict(
        bijgewerkt="2026-10-22",
        aanvullen={
            "Wat is SEO?": ["SEO rust op drie pijlers. Techniek zorgt dat Google je pagina's kan vinden en lezen. Content zorgt dat je pagina's de vraag van de zoeker beantwoorden. Autoriteit, vooral links en vermeldingen op andere websites, laat Google zien dat je te vertrouwen bent. Belangrijk om te weten: Google zegt zelf dat het geen geld aanneemt om een website vaker te bezoeken of hoger te tonen (<a href=\"https://developers.google.com/search/docs/fundamentals/how-search-works\" rel=\"noopener\" target=\"_blank\">Google Search Central</a>). Een plek in de organische resultaten kun je dus niet kopen."],
        },
        secties=[
            ("SEO en SEA naast elkaar", [
                "De belangrijkste verschillen in één overzicht.",
                "<table><thead><tr><th scope=\"col\"></th><th scope=\"col\">SEO</th><th scope=\"col\">SEA</th></tr></thead><tbody>"
                "<tr><td>Waar je staat</td><td>In de gewone zoekresultaten</td><td>Bij de advertenties, met het label Gesponsord</td></tr>"
                "<tr><td>Hoe je betaalt</td><td>Met tijd en werk aan je website</td><td>Per klik op je advertentie</td></tr>"
                "<tr><td>Snelheid</td><td>Weken tot maanden</td><td>Vanaf de dag dat je campagne live staat</td></tr>"
                "<tr><td>Als je stopt</td><td>Posities zakken langzaam</td><td>Je advertentie verdwijnt direct</td></tr>"
                "<tr><td>Controle</td><td>Google bepaalt je positie</td><td>Jij kiest zoekwoorden, tekst en budget</td></tr>"
                "<tr><td>Herkenbaarheid</td><td>Een gewoon zoekresultaat</td><td>Herkenbaar als advertentie</td></tr>"
                "<tr><td>Meten</td><td>Search Console en Analytics</td><td>Tot op het zoekwoord in Google Ads</td></tr>"
                "<tr><td>Past bij</td><td>Lange termijn en veel gezochte onderwerpen</td><td>Snel resultaat, acties en testen</td></tr>"
                "</tbody></table>",
            ]),
            ("Wat hebben SEO en SEA gemeen?", [
                "Meer dan je denkt. Allebei beginnen ze bij zoekwoordonderzoek: waar zoekt je klant op en wat bedoelt die ermee? Allebei hebben ze een goede pagina nodig om op te landen. Google Ads beoordeelt ook de kwaliteit van je landingspagina, dus een trage of onduidelijke pagina maakt je advertenties duurder. En allebei werken ze alleen als je meet wat het oplevert.",
                "Daarom versterken ze elkaar. Een <a href=\"/landingspagina-laten-maken/\">goede landingspagina</a> helpt je advertenties en je organische posities tegelijk.",
            ]),
            ("Hoe verdeel je je inzet over de tijd?", [
                "Een veelgebruikte aanpak voor een nieuwe website of dienst gaat in fases.",
                "- Eerste maanden: SEA levert direct bezoekers en laat zien welke zoekwoorden aanvragen opleveren. Tegelijk zet je de SEO-basis neer.\n- Daarna: je SEO-posities groeien op de zoekwoorden die in je advertenties goed werkten.\n- Op termijn: waar je organisch goed staat, kun je minder adverteren. SEA blijft nuttig voor acties, seizoenen en zoekwoorden waar je nog niet organisch scoort.",
                "Hoeveel je in elke fase inzet, hangt af van je markt en concurrentie. Google zelf zegt dat het effect van SEO-wijzigingen een paar uur tot een paar maanden kan duren (<a href=\"https://developers.google.com/search/docs/fundamentals/seo-starter-guide\" rel=\"noopener\" target=\"_blank\">SEO-starthandleiding van Google</a>).",
            ]),
            ("SEO en SEA in tijden van AI", [
                "Google toont bij steeds meer zoekopdrachten een AI-overzicht boven de resultaten. Volgens Google gelden daarvoor dezelfde richtlijnen als voor gewone SEO (<a href=\"https://developers.google.com/search/docs/appearance/ai-features\" rel=\"noopener\" target=\"_blank\">Google Search Central</a>). Dat betekent duidelijke antwoorden, betrouwbare informatie en een goed gebouwde website. Ook in Google Ads doet automatisering steeds meer, bijvoorbeeld bij biedstrategieën. Dat maakt een goede meting en een goede landingspagina alleen maar belangrijker, want de systemen sturen op de data die jij ze geeft.",
            ]),
        ],
        faq=[
            ("Hoe lang duurt het voordat SEO werkt?", "Technische verbeteringen zie je soms binnen weken terug. Een blijvende stijging op belangrijke zoekwoorden kost meestal een aantal maanden, afhankelijk van je concurrentie en hoe sterk je website al is."),
            ("Waar hangen de kosten van SEO en SEA van af?", "Bij SEO vooral van de tijd die nodig is voor techniek, content en links. Bij SEA van je advertentiebudget, de concurrentie op je zoekwoorden en de tijd voor het beheer van je campagnes."),
        ],
    ),
    "wat-doet-een-marketeer": dict(
        bijgewerkt="2026-10-22",
        secties=[
            ("Met welke tools werkt een marketeer?", [
                "Welke tools je gebruikt, hangt af van je rol. Deze kom je in bijna elke marketingbaan tegen.",
                "- Meten: Google Analytics, Google Tag Manager en Search Console\n- Website: WordPress of Shopify\n- Adverteren: Google Ads, Meta Ads Manager en LinkedIn Campaign Manager\n- Social media en content: Meta Business Suite, Canva en een planningstool\n- E-mail: Mailchimp, Brevo of een vergelijkbaar programma\n- AI: ChatGPT, Claude of Gemini voor ideeën, eerste versies en analyses",
                "Je hoeft niet alles te kennen. Werkgevers zoeken vooral iemand die snel een nieuwe tool oppikt en weet wat hij wil meten. Lees ook hoe je <a href=\"/ai-specialist-inhuren/\">AI inzet in je marketing</a>.",
            ]),
            ("Marketing, sales en reclame, wat is het verschil?", [
                "Marketing zorgt dat de juiste mensen je kennen en interesse krijgen. Sales zet die interesse om in een klant, bijvoorbeeld met een offerte of een gesprek. Reclame is één onderdeel van marketing: betaalde boodschappen, zoals advertenties. Een marketeer werkt dus breder dan reclame en levert de aanvragen waar sales mee verder gaat.",
            ]),
            ("Doorgroeien als marketeer", [
                "De meeste marketeers beginnen breed, bijvoorbeeld als marketingassistent of junior online marketeer. Na een paar jaar kies je vaak een richting: specialist in een vak zoals SEO, SEA of content, of juist breder als marketingmanager. Wie doorgroeit naar een leidinggevende rol, wordt bijvoorbeeld <a href=\"/kennisbank/wat-doet-een-head-of-marketing/\">head of marketing</a>.",
                "Overstappen vanuit een ander vak kan ook. Veel vaardigheden, zoals schrijven, analyseren en klantcontact, neem je mee. Een cursus in een concreet vak, zoals Google Ads of SEO. Praktijkervaring helpt je daarna verder.",
            ]),
        ],
        faq=[
            ("Welke vaardigheden heeft een marketeer nodig?", "Goed schrijven, analytisch denken, je kunnen verplaatsen in de klant en vlot met tools werken. Daarnaast helpt het als je resultaten helder kunt uitleggen aan collega's of klanten."),
            ("Hoe word je marketeer?", "Meestal via een HBO- of WO-opleiding in marketing, communicatie of een verwante richting. Praktijkervaring naast je studie, bijvoorbeeld als werkstudent, maakt het verschil bij je eerste baan."),
        ],
    ),
    "social-media-uitbesteden-waar-let-je-op": dict(
        bijgewerkt="2026-10-25",
        intro="Wil je <a href=\"/social-media-uitbesteden/\">social media uitbesteden</a>? Dat scheelt tijd, maar alleen als je het goed regelt. Met deze 8 tips voorkom je dat je merk ongemerkt een andere kant op gaat of dat je de toegang tot je eigen accounts kwijtraakt. Je leest wat je wel en niet kunt uitbesteden, welke afspraken je maakt en hoe je beoordeelt of het werkt.",
        secties=[
            ("De voor- en nadelen van uitbesteden", [
                "Uitbesteden levert tijd en kennis op, maar het heeft ook risico's. Zet ze naast elkaar voordat je kiest.",
                "<table><thead><tr><th scope=\"col\">Voordelen</th><th scope=\"col\">Nadelen en risico's</th></tr></thead><tbody>"
                "<tr><td>Je wint tijd voor je eigen werk</td><td>Je hebt minder direct controle over wat er online komt</td></tr>"
                "<tr><td>Kennis van platforms, trends en tools</td><td>Content die niet past bij je merk als de briefing zwak is</td></tr>"
                "<tr><td>Een vast ritme dat je volhoudt</td><td>Kennis zit bij een ander als je het later terughaalt</td></tr>"
                "<tr><td>Iemand die meet wat werkt</td><td>Je blijft nodig voor input en akkoord</td></tr>"
                "</tbody></table>",
                "De risico's beperk je met de tips hierboven: zelf eigenaar blijven van je accounts, goede afspraken over toon en goedkeuring en een vaste evaluatie.",
            ]),
            ("Strategie zelf, uitvoering uitbesteden", [
                "Een veelgebruikte verdeling: jij bepaalt de richting, de uitvoering besteed je uit. Jij weet wat je bedrijf wil bereiken en wat je klanten bezighoudt. Het maken, plannen en beantwoorden kost vooral tijd en dat kun je goed overdragen. Zo houd je de regie over je merk zonder dat je er elke dag mee bezig bent.",
            ]),
            ("Hoe beoordeel je een partij?", [
                "- Vraag om voorbeelden van eerder werk in een vergelijkbare branche.\n- Plan een kennismaking en let op de vragen die ze stellen over je doel en je klanten.\n- Vraag hoe ze rapporteren en wat ze meten.\n- Check wie het werk echt doet en wie het controleert.\n- Lees het contract: looptijd, opzegtermijn en wie eigenaar is van de content.",
            ]),
            ("Waar hangen de kosten van af?", [
                "De kosten hangen vooral af van het aantal kanalen, hoeveel content je per maand wilt, de verhouding tussen foto en video en of community management erbij hoort. Let op of het advertentiebudget voor social ads in de offerte zit of apart wordt betaald. Vraag altijd om een offerte die precies laat zien wat je krijgt. Wil je zelf eerst de basis leggen, begin dan met een <a href=\"/kennisbank/contentkalender-maken/\">contentkalender</a>.",
            ]),
        ],
        faq=[
            ("Wat besteed je beter niet uit?", "Je strategie en je merk. Jij bepaalt waar je naartoe wilt en wat je bedrijf uniek maakt. Ook gevoelige klachten of vragen over offertes handel je het best zelf af."),
            ("Hoe lang duurt het voordat uitbesteden resultaat oplevert?", "Een vast ritme en een herkenbare uitstraling zie je binnen een maand. Groei in bereik en aanvragen bouwt zich meestal op over een aantal maanden."),
        ],
    ),
    "freelance-marketeer-of-marketing-student": dict(
        bijgewerkt="2026-10-22",
        secties=[
            ("Een freelancer inhuren, waar moet je rekening mee houden?", [
                "Huur je een zzp'er in, dan moet het echt een opdracht zijn en geen verkapt dienstverband. De overheid wijst erop dat jij als opdrachtgever moet controleren dat er geen sprake is van loondienst. Is dat wel zo, dan kun je alsnog loonbelasting en premies moeten betalen (<a href=\"https://business.gov.nl/running-your-business/staff/recruiting-and-hiring-staff/hire-a-self-employed-professional/\" rel=\"noopener\" target=\"_blank\">Business.gov.nl</a>).",
                "- Leg de opdracht vast in een overeenkomst met het resultaat, de planning en wie eigenaar is van het werk.\n- Stuur op het resultaat, niet op hoe en wanneer de freelancer werkt.\n- Spreek af wat er wel en niet onder de opdracht valt, zodat de klus niet ongemerkt groter wordt.\n- Maak afspraken over geheimhouding als de freelancer met klantgegevens werkt.",
            ]),
            ("Op uurbasis of per project?", [
                "Freelancers rekenen op uurbasis of per project. Per project weet je vooraf waar je aan toe bent, maar alleen als de opdracht scherp is omschreven. Op uurbasis is flexibeler voor doorlopend werk, zoals social media of campagnebeheer. Bij Marketing Student werk je met een vast aantal uren per maand, zonder langlopend contract. Waar de kosten van afhangen, staat in je offerte.",
            ]),
            ("Freelancer, bureau of student naast elkaar", [
                "<table><thead><tr><th scope=\"col\"></th><th scope=\"col\">Freelancer</th><th scope=\"col\">Bureau</th><th scope=\"col\">Marketing student</th></tr></thead><tbody>"
                "<tr><td>Wie doet het werk</td><td>De freelancer zelf</td><td>Een team</td><td>Een getrainde student</td></tr>"
                "<tr><td>Controle op kwaliteit</td><td>Doe je zelf</td><td>Binnen het bureau</td><td>Een senior marketeer</td></tr>"
                "<tr><td>Bij ziekte of vertrek</td><td>Je zoekt zelf een vervanger</td><td>Het bureau regelt het</td><td>We regelen een nieuwe student</td></tr>"
                "<tr><td>Past bij</td><td>Een specialistische klus</td><td>Grote of complexe trajecten</td><td>Structureel uitvoerend werk</td></tr>"
                "</tbody></table>",
                "Meer over de verschillende rollen lees je in <a href=\"/kennisbank/wat-voor-type-marketeers-zijn-er/\">wat voor type marketeers zijn er</a>.",
            ]),
        ],
        faq=[
            ("Wat is schijnzelfstandigheid?", "Daarvan is sprake als een zzp'er in de praktijk werkt als een werknemer, bijvoorbeeld omdat jij bepaalt hoe en wanneer het werk gebeurt. Als opdrachtgever kun je dan alsnog loonbelasting en premies moeten betalen."),
            ("Welke soorten freelance marketeers zijn er?", "De meeste freelancers hebben een specialisme, zoals SEO, Google Ads, social media, content of performance marketing. Kies iemand met ervaring in precies het vak dat je nodig hebt."),
        ],
    ),
    "online-marketing-mkb": dict(
        bijgewerkt="2026-10-22",
        aanvullen={
            "Stap 3. Word gevonden in Google": ["Een Google Bedrijfsprofiel is gratis. Je beheert er zelf mee hoe je bedrijf in Google Maps en Zoeken verschijnt (<a href=\"https://support.google.com/business/answer/7039811?hl=nl\" rel=\"noopener\" target=\"_blank\">Google Bedrijfsprofiel-help</a>). Vul alles in: categorie, diensten, openingstijden, foto's en een beschrijving. Vraag tevreden klanten om een review."],
        },
        secties=[
            ("Een plan voor de eerste 90 dagen", [
                "Wie alles tegelijk wil, komt nergens. Verdeel de eerste drie maanden in drie fases.",
                "<table><thead><tr><th scope=\"col\">Periode</th><th scope=\"col\">Waar je mee bezig bent</th></tr></thead><tbody>"
                "<tr><td>Week 1 en 2</td><td>Doel en klant op papier, Google Bedrijfsprofiel volledig, meting met Analytics en Search Console</td></tr>"
                "<tr><td>Week 3 tot 6</td><td>Website verbeteren, de belangrijkste dienstpagina's herschrijven, één social media-kanaal starten met een vast ritme</td></tr>"
                "<tr><td>Week 7 tot 12</td><td>Eerste content voor Google, een inschrijving voor je nieuwsbrief, eventueel een kleine campagne om te testen</td></tr>"
                "</tbody></table>",
                "Kijk na 90 dagen wat het heeft opgeleverd en kies waar je meer tijd in steekt.",
            ]),
            ("Welke cijfers houd je bij?", [
                "Je hoeft niet alles te meten. Deze cijfers vertellen je het meest.",
                "- Aanvragen: hoeveel offerteaanvragen, telefoontjes of verkopen komen er via je website?\n- Herkomst: via welk kanaal kwamen ze binnen?\n- Conversieratio: welk deel van je bezoekers neemt contact op of koopt?\n- Kosten per aanvraag: wat kost één aanvraag, in tijd of advertentiebudget?\n- Klantwaarde: wat levert een klant gemiddeld op over de hele samenwerking?",
                "Zet die vijf cijfers elke maand op een rij. Dan zie je snel welk kanaal het waard is om in te investeren.",
            ]),
            ("Vergeet offline niet", [
                "Online marketing werkt het best samen met wat je al offline doet. Een tevreden klant die je aanbeveelt, een netwerkbijeenkomst of een lokale sponsoring levert vaak de eerste zoekopdrachten naar je bedrijfsnaam op. Vraag bij elke nieuwe klant hoe die je heeft gevonden. Dat vertelt je meer dan elk dashboard.",
            ]),
        ],
        faq=[
            ("Wat is een Google Bedrijfsprofiel?", "Een gratis profiel waarmee je bedrijf verschijnt in Google Maps en in de lokale zoekresultaten, met je adres, openingstijden, foto's en reviews. Voor bedrijven met klanten in de regio is het vaak de eerste stap."),
            ("Hoe meet ik of online marketing werkt?", "Kijk vooral naar aanvragen en verkopen en waar die vandaan komen. Google Analytics en Search Console laten zien welke kanalen en pagina's werken. Vraag nieuwe klanten ook hoe ze je hebben gevonden."),
        ],
    ),
}


def upgrade(a):
    u = UPGRADE.get(a["slug"])
    if not u:
        return a
    a = dict(a)
    secties = list(a["secties"])
    for kop, extra in u.get("aanvullen", {}).items():
        assert any(k == kop for k, _ in secties), f"{a['slug']}: sectie {kop} niet gevonden"
        secties = [(k, list(p) + extra) if k == kop else (k, p) for k, p in secties]
    a["secties"] = secties[:-1] + u.get("secties", []) + secties[-1:]
    a["faq"] = list(a["faq"]) + u.get("faq", [])
    if u.get("intro"):
        a["intro"] = u["intro"]
    a["bijgewerkt"] = u["bijgewerkt"]
    return a
