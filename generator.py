import graph
import arrow
import subprocess


def genSeznam(seznamSkupin):
    for skupina in seznamSkupin:
        count = graph.getTotalCount(skupina)
        zahajeni = graph.getSkupinaZahajeni(count)
        probihajici = graph.getSkupinaProbihajici(count)
        yield {'jmeno': skupina, 'pocet': count, 'zahajeni': zahajeni,
               'probihajici': probihajici}


def generate(seznamSkupin):
    printHeader()
    printBody(genSeznam(seznamSkupin))
    printFooter()


def printHeader():
    print("<!DOCTYPE  html>\n<html lang=\"cs\">\n<head>\n" +
          "<meta charset=\"utf-8\" />\n"
          "<title>Skupiny clenu</title>\n" +
          "<style> table { border: 1px solid black; " +
          "border-collapse: collapse; }\n" +
          "td {border-left: 1px solid black; " +
          "border-right: 1px solid black;}\n" +
          "</style>\n</head>\n")


def printBody(seznam):
    # seznam ctveric: jmeno, pocet, zahajeni, probihajici
    print("<body>\n" +
          "<h1>Skupiny clenu u Piratu</h1>")

    for skupina in seznam:
        print("<h2>" + skupina['jmeno'] + "</h2>\n" +
              "<table><thead><tr>\n" +
              "<td>Pocet clenu</td>\n" +
              "<td>Velikost skupiny pro zahajeni jednani</td>\n" +
              "<td>Velikost skupiny na probihajicim jednani</td>\n" +
              "</tr>\n</thead>\n<tbody>\n<tr>" +
              "<td>" +
              str(skupina['pocet']) +
              "</td><td>" +
              str(skupina['zahajeni']) +
              "</td><td>" +
              str(skupina['probihajici']) +
              "</td></tr>\n" +
              "</tbody></table>\n")


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
    print("</body></html>")


skupiny = ["Republikovy vybor", "Celostatni forum", "KS Praha",
           "KS Stredocesky kraj", "KS Ustecky kraj"]
generate(skupiny)
