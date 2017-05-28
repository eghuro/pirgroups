import graph
import arrow


def generate(seznamSkupin):
    seznam = []
    for skupina in seznamSkupin:
        count = graph.getTotalCount(skupina)
        zahajeni = graph.getSkupinaZahajeni(count)
        probihajici = graph.getSkupinaProbihajici(count)
        seznam.append((skupina, count, zahajeni, probihajici))

    printHeader()
    printBody(seznam)
    printFooter()


def printHeader():
    print("<!DOCTYPE  html>\n<html>\n<head>\n" +
          "<title>Skupiny clenu</title>\n" +
          "</head>")


def printBody(seznam):
    # seznam ctveric: jmeno, pocet, zahajeni, probihajici
    print("<body>\n" +
          "<h1>Skupiny clenu u Piratu</h1>")

    for skupina in seznam:
        jmeno = skupina[0]
        pocet = str(skupina[1])
        zahajeni = str(skupina[2])
        probihajici = str(skupina[3])

        print("<h2>" + jmeno + "</h2>\n" +
              "<table border=\"1\"><thead><tr>\n" +
              "<td>Pocet clenu</td>\n" +
              "<td>Velikost skupiny pro zahajeni jednani</td>\n" +
              "<td>Velikost skupiny na probihajicim jednani</td>\n" +
              "</tr>\n</thead>\n<tbody>\n<tr>" +
              "<td>" +
              pocet +
              "</td><td>" +
              zahajeni +
              "</td><td>" +
              probihajici +
              "</td></tr>\n" +
              "</tbody></table>\n")


def printFooter():
    utc = arrow.utcnow()
    local = utc.to('Europe/Prague')
    print("<p>Generated: " +
          local.format('YYYY-MM-DD HH:mm ZZ') +
          "</p>")
    print("</body></html>")


skupiny = ["Republikovy vybor", "Celostatni forum", "KS Praha",
           "KS Stredocesky kraj", "KS Ustecky kraj"]
generate(skupiny)
