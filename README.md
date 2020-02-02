# Skupiny clenu u Piratu
Skripty generujici prehled, kolik clenu cini jednotlive skupiny clenu
v Piratske strane ve vybranych organech.

`graph.py` je "knihovna" pracujici nad Piratskym Graph API, ktera umoznuje
zjistit pocet clenu nejake skupiny a nasledne vypocitat velikosti jednotlivych
skupin clenu.

`generator.py` vygeneruje na standardni vystup jednoduchou HTML stranku, ktera zobrazuje velikosti
prislusnych skupin clenu ve vybranych skupinach, konkretne: Republikovy vybor, Celostatni forum,
KS Praha, KS Stredocesky kraj, S Ustecky kraj, Poslanecka snemovna - poslanci a MS Praha 4. Navic
vygeneruje soubor current.json, kde jsou prislusna data ve strojove citelne podobe.

`csvLogger.py` zaznamena aktualni pocty clenu a velikosti skupin ve vybranych
skupinach ze souboru current.json do CSV souboru.

Pro pouziti je potreba `python3`, `requests` a `arrow`.
Jednotlive zavislosti lze nainstalovat pres pip pomoci `pip install -r requirements.txt`

Spousti se pomoci `python3 generator.py > skupiny.html`
Vysledek je mozne videt na: https://poseidon.eghuro.cz/skupiny.html
