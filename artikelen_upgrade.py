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
    # Audit 2026-11-10: zoektermen net buiten de top 10.
    "website-laten-maken-zzp": dict(
        bijgewerkt="2026-11-10",
        intro="Een website laten maken als zzp'er hoeft niet groot of duur te zijn. Met vijf tot tien pagina's, een duidelijk aanbod en een makkelijke manier om contact op te nemen heb je de basis. In dit artikel lees je welke pagina's je nodig hebt, welke gegevens verplicht zijn en hoe opdrachtgevers je vinden.",
        aanvullen={
            "Zelf maken of laten maken?": [
                "<table><thead><tr><th scope=\"col\"></th><th scope=\"col\">Zelf maken</th><th scope=\"col\">Laten maken</th></tr></thead><tbody>"
                "<tr><td>Wat het je kost</td><td>Vooral eigen tijd</td><td>Een investering vooraf</td></tr>"
                "<tr><td>Hoe snel het klaar is</td><td>Hangt af van je vrije uren</td><td>Volgens een afgesproken planning</td></tr>"
                "<tr><td>Vindbaarheid in Google</td><td>Moet je zelf uitzoeken</td><td>De SEO-basis hoort erbij</td></tr>"
                "<tr><td>Ontwerp</td><td>Een standaardsjabloon</td><td>Afgestemd op je bedrijf</td></tr>"
                "<tr><td>Past bij</td><td>Een eenvoudig visitekaartje</td><td>Een website die aanvragen moet opleveren</td></tr>"
                "</tbody></table>",
            ],
        },
        secties=[
            ("Welke gegevens zijn verplicht op je website?", [
                "Als ondernemer moet je een aantal gegevens op je website zetten. Volgens de overheid zijn dat je naam en handelsnaam, je bezoekadres, je e-mailadres en je telefoonnummer. Lever je diensten of verkoop je via internet, dan horen je KVK-nummer en je btw-identificatienummer er ook bij (<a href=\"https://ondernemersplein.overheid.nl/wetten-en-regels/regels-voor-bedrijfscorrespondentie/\" rel=\"noopener\" target=\"_blank\">Ondernemersplein</a>). Zet ze op een plek waar bezoekers ze makkelijk vinden, bijvoorbeeld in de footer en op je contactpagina.",
                "Heeft je website een contactformulier of een nieuwsbrief, dan verwerk je persoonsgegevens. Een privacyverklaring is dan verplicht (<a href=\"https://ondernemersplein.overheid.nl/wetten-en-regels/privacyverklaring-opstellen/\" rel=\"noopener\" target=\"_blank\">Ondernemersplein over de privacyverklaring</a>). Voor cookies geldt dit:",
                "- Functionele cookies en analytische cookies met weinig gevolgen voor de privacy mag je plaatsen zonder toestemming. Je informeert bezoekers er wel over.\n- Voor trackingcookies, zoals die van advertentieplatforms, vraag je altijd vooraf toestemming.",
                "De regels staan bij <a href=\"https://ondernemersplein.overheid.nl/wetten-en-regels/gebruik-van-cookies-op-uw-website/\" rel=\"noopener\" target=\"_blank\">Ondernemersplein over cookies</a>. Laat je een website maken, vraag dan of de cookiebanner en de privacyverklaring zijn inbegrepen.",
            ]),
            ("Een domeinnaam kiezen", [
                "Je domeinnaam is het adres van je website. Kies een naam die kort is, makkelijk te spellen en past bij je bedrijfsnaam. Voor Nederlandse klanten is .nl de meest herkenbare extensie. Vermijd streepjes en cijfers als dat kan, want die leiden tot typfouten als je het adres aan de telefoon doorgeeft.",
                "Registreer de domeinnaam altijd op je eigen naam, ook als een ander de website bouwt. Dan blijft het adres van jou als je later van bouwer of hosting wisselt. Gebruik hetzelfde domein voor je e-mailadres. Een adres op je eigen domein komt professioneler over dan een gratis mailadres.",
            ]),
            ("De woorden van je klant gebruiken", [
                "Opdrachtgevers zoeken niet op je functietitel, maar op hun probleem en vaak op een plaats. Een voorbeeld: een zelfstandig boekhouder in Leiden wordt eerder gevonden op \"boekhouder zzp Leiden\" dan op \"financiële dienstverlening\". Zet die woorden in de titel van je pagina, in de kop en in de eerste alinea.",
                "- Schrijf op welke vragen klanten je stellen in een eerste gesprek.\n- Maak per dienst één pagina met die dienst in de titel.\n- Noem je werkgebied, in de tekst en bij je contactgegevens.\n- Schrijf zoals je praat met een klant, zonder vakjargon.",
                "Controleer de website daarna op je telefoon. Google gebruikt de mobiele versie van je pagina's om ze te indexeren en te beoordelen (<a href=\"https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing?hl=nl\" rel=\"noopener\" target=\"_blank\">Google Search Central</a>).",
            ]),
        ],
        faq=[
            ("Is een website verplicht als zzp'er?", "Nee, je bent niet verplicht om een website te hebben. Heb je er wel een, dan gelden er regels voor de gegevens die erop staan, zoals je handelsnaam, adres en contactgegevens."),
            ("Welke gegevens moeten op mijn zzp-website staan?", "Je naam en handelsnaam, je bezoekadres, je e-mailadres en je telefoonnummer. Lever je diensten of verkoop je via internet, dan ook je KVK-nummer en je btw-identificatienummer."),
            ("Heb ik als zzp'er een privacyverklaring nodig?", "Ja, zodra je persoonsgegevens verwerkt. Dat doe je al met een contactformulier of een nieuwsbrief. In de privacyverklaring leg je uit welke gegevens je verzamelt en waarom."),
        ],
    ),
    "goedkope-website-laten-maken": dict(
        bijgewerkt="2026-11-10",
        intro="Een goedkope website laten maken kan prima, zolang je bespaart op omvang en niet op de basis. Die basis is snelheid, mobiel gebruik, vindbaarheid in Google en eigendom van je website. In dit artikel lees je waar je wel en niet op bespaart, welke valkuilen er zijn en welke optie bij jou past.",
        secties=[
            ("Websitebouwer, freelancer, bureau of student naast elkaar", [
                "Er zijn grofweg vier manieren om aan een betaalbare website te komen. Ze verschillen vooral in wie het werk doet en wie de kwaliteit bewaakt.",
                "<table><thead><tr><th scope=\"col\"></th><th scope=\"col\">Websitebouwer</th><th scope=\"col\">Freelancer</th><th scope=\"col\">Bureau</th><th scope=\"col\">Marketing student</th></tr></thead><tbody>"
                "<tr><td>Wie bouwt</td><td>Jijzelf</td><td>Eén zelfstandige</td><td>Een team</td><td>Een getrainde student</td></tr>"
                "<tr><td>Controle op kwaliteit</td><td>Doe je zelf</td><td>Doe je zelf</td><td>Binnen het bureau</td><td>Een senior webspecialist</td></tr>"
                "<tr><td>Kosten</td><td>Laag, plus je eigen tijd</td><td>Gemiddeld</td><td>Hoog</td><td>Lager dan een bureau</td></tr>"
                "<tr><td>Eigendom</td><td>Je zit vast aan het platform</td><td>Hangt af van de afspraken</td><td>Hangt af van de afspraken</td><td>Alles op jouw naam</td></tr>"
                "<tr><td>Past bij</td><td>Een eenvoudig visitekaartje</td><td>Een afgebakende klus</td><td>Grote of complexe websites</td><td>Een mkb-website die aanvragen oplevert</td></tr>"
                "</tbody></table>",
                "Er komen ook steeds meer websitebouwers met AI bij, die in een paar minuten een eerste versie maken. Dat is handig om snel iets te hebben staan. De teksten, de opbouw en de vindbaarheid blijven werk dat je daarna zelf moet doen.",
            ]),
            ("Reken met de kosten over een paar jaar", [
                "De bouwprijs is maar een deel van wat een website kost. Daarna komen er elk jaar kosten terug. Een goedkoop aanbod met hoge vaste lasten is over drie jaar vaak duurder dan een hogere prijs vooraf.",
                "- Hosting en de domeinnaam\n- Licenties voor een thema of plugins\n- Onderhoud: updates, back-ups en beveiliging\n- Wijzigingen die je niet zelf kunt doen\n- Bij een webshop de kosten van de betaalprovider",
                "Tel de bouw en drie jaar aan vaste kosten bij elkaar op en vergelijk aanbieders op dat totaal. Vraag ook wat er gebeurt als je opzegt: krijg je de website mee of begin je opnieuw? Meer over de terugkerende kosten lees je bij <a href=\"/website-laten-onderhouden/\">website laten onderhouden</a>.",
            ]),
            ("Thema of maatwerk?", [
                "Een bestaand thema is de grootste besparing. Het ontwerp is er al, de bouwer past kleuren, lettertypen en indeling aan je bedrijf aan. Voor de meeste mkb-websites is dat ruim voldoende. Let wel op de keuze: een licht en goed onderhouden thema laadt snel, een thema vol effecten en plugins niet.",
                "Maatwerk is zinvol als je website iets moet kunnen wat een thema niet biedt, zoals een eigen rekentool, een klantportaal of een koppeling met je systemen. Heb je dat niet nodig, dan betaal je bij maatwerk vooral voor uren die je bezoeker niet ziet.",
            ]),
            ("Welke optie past bij jou?", [
                "- Je begint net en wilt vooral vindbaar zijn op je naam: een websitebouwer of een kleine website met een paar pagina's is genoeg.\n- Je wilt aanvragen uit Google: laat de website maken, met een pagina per dienst en de SEO-basis op orde.\n- Je hebt al een website die traag of verouderd is: laat eerst bekijken of verbeteren kan, dat is vaak goedkoper dan opnieuw beginnen.\n- Je wilt online verkopen: kies een webshop op een bekend platform, zodat je later niet vastloopt.",
                "Twijfel je, begin dan klein. Een goede website van vijf pagina's levert meer op dan een grote website die half af is.",
            ]),
        ],
        faq=[
            ("Is een goedkope website een slechte investering?", "Nee, niet als de basis klopt: snel, goed op mobiel, vindbaar en op jouw naam. Een goedkope website wordt pas duur als je hem niet zelf kunt aanpassen, als hij niet gevonden wordt of als je vastzit aan hoge vaste kosten."),
            ("Welke kosten komen elk jaar terug?", "Hosting, de domeinnaam en eventueel licenties en onderhoud. Bij een webshop komen daar de kosten van de betaalprovider bij. Vraag bij elke offerte welke kosten na de livegang terugkomen."),
            ("Thema of maatwerk, wat is goedkoper?", "Een bestaand thema, omdat het ontwerp er al is. Maatwerk kost meer uren en is alleen nodig als je website functies heeft die een thema niet biedt."),
        ],
    ),
    "wat-is-sea": dict(
        bijgewerkt="2026-11-10",
        titel="Wat is SEA?",
        intro="SEA staat voor Search Engine Advertising, oftewel adverteren in zoekmachines. Je betaalt per klik om bovenaan de zoekresultaten te staan bij zoekopdrachten die bij je bedrijf passen. In dit artikel lees je hoe SEA werkt, waar de kosten uit bestaan en wanneer het past bij jouw bedrijf.",
        aanvullen={
            "Wat kost SEA?": [
                "De kosten van SEA bestaan uit twee delen.",
                "<table><thead><tr><th scope=\"col\"></th><th scope=\"col\">Advertentiebudget</th><th scope=\"col\">Beheer</th></tr></thead><tbody>"
                "<tr><td>Wat het is</td><td>Wat je per klik aan Google betaalt</td><td>De tijd om campagnes op te zetten en bij te sturen</td></tr>"
                "<tr><td>Wie je betaalt</td><td>Google, rechtstreeks vanuit je eigen account</td><td>Je specialist, of je eigen uren als je het zelf doet</td></tr>"
                "<tr><td>Waar het van afhangt</td><td>Concurrentie op je zoekwoorden, je kwaliteit en je dagbudget</td><td>Aantal campagnes, hoe vaak er wordt bijgestuurd en de rapportage</td></tr>"
                "<tr><td>Hoe je het begrenst</td><td>Met een dagbudget per campagne</td><td>Met een vast aantal uren per maand</td></tr>"
                "</tbody></table>",
                "Let er bij uitbesteden op dat het advertentiebudget rechtstreeks van jou naar Google gaat en dat het account op jouw naam staat. Dan zie je altijd zelf wat er is uitgegeven.",
            ],
        },
        secties=[
            ("Hoe komt de prijs van een klik tot stand?", [
                "Je stelt per zoekwoord of campagne in wat je maximaal voor een klik wilt betalen. Wat je echt betaalt, is vaak minder. Volgens Google betaal je wat nodig is om de adverteerder direct onder je voor te blijven en nooit meer dan je maximale bod, tenzij je Google automatisch laat bieden (<a href=\"https://support.google.com/google-ads/answer/6297?hl=nl\" rel=\"noopener\" target=\"_blank\">Google Ads Help over werkelijke CPC</a>).",
                "De volgorde van de advertenties hangt niet alleen af van je bod. Google kijkt ook naar de kwaliteit van je advertentie en je landingspagina, naar de concurrentie in de veiling en naar de context van de zoekopdracht. Google zegt daarover dat advertenties van hogere kwaliteit vaak leiden tot lagere kosten per klik (<a href=\"https://support.google.com/google-ads/answer/1722122?hl=nl\" rel=\"noopener\" target=\"_blank\">Google Ads Help over advertentierangschikking</a>).",
                "Daarom verschilt de klikprijs sterk per branche. Op zoekwoorden waar één klant veel oplevert, bieden meer adverteerders en ligt de prijs hoger. Zoekwoorden met een plaatsnaam of een specifieke dienst zijn vaak rustiger en leveren betere aanvragen op.",
            ]),
            ("Wat is de kwaliteitsscore?", [
                "De kwaliteitsscore is een cijfer van 1 tot 10 dat je per zoekwoord in Google Ads ziet. Het laat zien hoe jouw advertentie zich verhoudt tot die van andere adverteerders. De score bestaat uit drie onderdelen (<a href=\"https://support.google.com/google-ads/answer/6167118?hl=nl\" rel=\"noopener\" target=\"_blank\">Google Ads Help over de kwaliteitsscore</a>).",
                "- Verwachte klikfrequentie: hoe groot is de kans dat iemand op je advertentie klikt?\n- Advertentierelevantie: sluit je advertentie aan op wat de zoeker bedoelt?\n- Ervaring op de landingspagina: vindt de bezoeker daar wat de advertentie belooft?",
                "Google noemt de score zelf een hulpmiddel om te zien waar je kunt verbeteren. Het cijfer telt niet rechtstreeks mee in de veiling. De onderdelen erachter wel: een relevante advertentie en een goede pagina zorgen voor een betere positie tegen lagere kosten.",
            ]),
            ("Je dagbudget als rem", [
                "Per campagne stel je een gemiddeld dagbudget in. Op een drukke dag mag Google tot twee keer dat bedrag uitgeven, op rustige dagen minder. Over een hele maand betaal je nooit meer dan 30,4 keer je gemiddelde dagbudget (<a href=\"https://support.google.com/google-ads/answer/1704443?hl=nl\" rel=\"noopener\" target=\"_blank\">Google Ads Help over het dagbudget</a>). Zo weet je vooraf wat een campagne maximaal kost.",
                "Begin met een budget waarmee je genoeg klikken krijgt om iets te leren. Verhoog het pas als je ziet dat de campagne aanvragen oplevert. Sluit ook zoektermen uit die niets opleveren, zodat je budget naar de juiste klikken gaat.",
            ]),
            ("De voordelen en nadelen van SEA", [
                "<table><thead><tr><th scope=\"col\">Voordelen</th><th scope=\"col\">Nadelen</th></tr></thead><tbody>"
                "<tr><td>Zichtbaar vanaf de dag dat je campagne live staat</td><td>Je betaalt voor elke klik, ook als die niets oplevert</td></tr>"
                "<tr><td>Je bereikt mensen op het moment dat ze zoeken</td><td>Stop je met betalen, dan verdwijnt je advertentie</td></tr>"
                "<tr><td>Je bepaalt zelf zoekwoorden, regio en budget</td><td>Zonder wekelijks onderhoud lekt er budget weg</td></tr>"
                "<tr><td>Alles is te meten, tot op het zoekwoord</td><td>In drukke branches zijn klikken duur</td></tr>"
                "</tbody></table>",
                "SEA en SEO samen heten SEM, Search Engine Marketing. SEA is het betaalde deel en SEO het onbetaalde deel.",
            ]),
        ],
        faq=[
            ("Betaal je bij SEA voor vertoningen of voor klikken?", "Bij zoekadvertenties betaal je per klik. Wordt je advertentie getoond en klikt niemand, dan kost dat niets. Bij display en video kun je ook per duizend vertoningen betalen."),
            ("Waarom verschilt de prijs van een klik per branche?", "Omdat de prijs in een veiling tot stand komt. Hoe meer adverteerders op een zoekwoord bieden en hoe meer een klant hen oplevert, hoe hoger de prijs van een klik."),
            ("Wat is het verschil tussen SEA en SEM?", "SEM staat voor Search Engine Marketing en is de verzamelnaam voor alle marketing in zoekmachines. SEA is het betaalde deel daarvan, SEO het onbetaalde deel."),
            ("Waar bestaan de kosten van SEA uit?", "Uit het advertentiebudget dat je per klik aan Google betaalt en uit de tijd voor het opzetten en bijsturen van de campagnes. Besteed je het uit, dan betaal je die tijd aan je specialist."),
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
    if u.get("titel"):
        a["titel"] = u["titel"]
    a["bijgewerkt"] = u["bijgewerkt"]
    return a
