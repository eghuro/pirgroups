# Skupiny clenu u Piratu
Skripty generujici prehled, kolik clenu cini jednotlive skupiny clenu
v Piratske strane ve vybranych organech.

`graph.py` je knihovna pracujici nad Piratskym Graph API, ktera umoznuje
zjistit pocet clenu nejake skupiny a nasledne vypocitat velikosti jednotlivych
skupin clenu.

`generator.py` vygeneruje jednoduchou HTML stranku, ktera zobrazuje velikosti
prislusnych skupin clenu ve vybranych skupinach, konkretne: Celostatni forum,
Republikovy vybor, KF KS Praha, KS ScK, KS UsK a Poslanci.

`csvLogger.py` zaznamena aktualni pocty clenu a velikosti skupin ve vybranych
skupinach do CSV souboru.

Pro pouziti je potreba `python3`, `requests` a `arrow`.
Jednotlive zavislosti lze nainstalovat pres pip pomoci `pip install -r requirements.txt`

Spousti se pomoci `python3 generator.py > skupiny.html`
Vysledek je mozne videt na: https://poseidon.eghuro.cz/skupiny.html
