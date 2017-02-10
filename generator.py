import graph
import datetime

def generate():
    count = graph.getTotalCount()
    zahajeni = graph.getSkupinaZahajeni(count)
    probihajici = graph.getSkupinaProbihajici(count)

    printHeader()
    printBody(count, zahajeni, probihajici)
    printFooter()


def printHeader():
    print("<!DOCTYPE  html>\n<html>\n<head>\n" + 
          "<title>Skupiny clenu v RV</title>\n" + 
          "</head>")

    
def printBody(count, zahajeni, probihajici):
    print("<body>\n" +
          "<h1>Skupiny clenu v RV</h1>\n" +
          "<table border=\"1\"><thead><tr>\n" +
          "<td>Pocet clenu</td>\n" +
          "<td>Velikost skupiny pro zahajeni jednani</td>\n" +
          "<td>Velikost skupiny na probihajicim jednani</td>\n" +
          "</tr>\n</thead>\n<tbody>\n<tr>" +
          "<td>" +
          str(count) +
          "</td><td>" +
          str(zahajeni) +
          "</td><td>" +
          str(probihajici) +
          "</td></tr>\n" +
          "</tbody></table>\n")


def printFooter():
    print("<p>Generated: " + datetime.datetime.now().strftime("%b %d %Y, %H:%M") + "</p>")
    print("</body></html>")


generate()
