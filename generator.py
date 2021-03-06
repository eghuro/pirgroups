import graph
import arrow
import subprocess
import json


def genSeznam(seznamSkupin):
    for skupina in seznamSkupin:
        count = graph.getTotalCount(skupina)
        zahajeni = graph.getSkupinaZahajeni(count)
        probihajici = graph.getSkupinaProbihajici(count)
        yield {'jmeno': skupina, 'pocet': count, 'zahajeni': zahajeni,
               'probihajici': probihajici}


def teeLog(data, out, buf):
    for item in data:
        buf[item['jmeno']] = {
            "pocet": item['pocet'],
            "zahajeni": item['zahajeni'],
            "probihajici": item['probihajici']
        }
        yield item


def generate(seznamSkupin):
    printHeader()
    buf = {}
    printBody(teeLog(genSeznam(seznamSkupin), 'data.csv', buf))
    with open('current.json', 'w') as cur:
        json.dump(buf, cur)
    printFooter()


def printHeader():
    fav = 'https://forum.pirati.cz/styles/prosilver-ppcz-wide/theme/favicon.png'
    fvlnk = "".join(['<link rel="shortcut icon" href="',
                     fav,
                     '" type="image/x-icon" />'])
    lines = ['<!DOCTYPE html>', '<html lang="cs">', '<head>', fvlnk,
             '<meta charset="utf-8" />', '<title>Skupiny clenu</title>',
             '<style>',
             'table { border: 1px solid black; border-collapse: collapse; }',
             'td {border-left:1px solid black;border-right:1px solid black;}',
             '</style>',
             '</head>']
    print("\n".join(lines))


def printBody(seznam):
    print("<body>\n<h1>Skupiny clenu u Piratu</h1>")

    common = "\n".join(['<table><thead><tr>', '<td>Pocet clenu</td>',
                        '<td>Velikost skupiny pro zahajeni jednani</td>',
                        '<td>Velikost skupiny na probihajicim jednani</td>',
                        '</tr>', '</thead>', '<tbody>', '<tr><td>'])
    for skupina in seznam:
        print("<h2>" + skupina['jmeno'] + "</h2>\n")
        print(common)
        print(str(skupina['pocet']) + "</td><td> " + str(skupina['zahajeni']))
        print("</td><td>" + str(skupina['probihajici']) + "</td></tr>\n")
        print("</tbody></table>\n")


def printFooter():
    utc = arrow.utcnow()
    local = utc.to('Europe/Prague')
    rev = subprocess.check_output(["git", "describe", "--always"])
    rev = rev.strip().decode('utf-8')
    link = '<a href="https://github.com/eghuro/pirgroups/tree/%s">%s</a>' %\
           (rev, rev)

    print("<p>Generated on " +
          local.format('YYYY-MM-DD HH:mm ZZ') +
          " using script rev. " + link +
          "</p>")
    print("<p>Machine readable open data: " +
          "<a href=\"current.json\">current</a>, "+
          "<a href=\"data.csv\">historical</a></p>")
    print("</body></html>")


skupiny = ["Republikovy vybor", "Celostatni forum", "KS Praha",
           "KS Stredocesky kraj", "KS Ustecky kraj", "Poslanecka snemovna - poslanci", "MS Praha 4"]
generate(skupiny)
