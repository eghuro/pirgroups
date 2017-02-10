import requests
from math import sqrt


def getTotalCount():
    members_url = "https://graph.pirati.cz/group/Republikovy%20vybor/members"
    r = requests.get(members_url)

    count = 0
    for member in r.json():
        count = count + 1

    return count

def __countSkupinaZahajeni(total):
    '''
    Skupinou členů se rozumí jen taková skupina, která čítá aspoň stanovený počet členů strany, kteří podpořili určitý návrh. Počet členů se stanoví u návrhu na zahájení jednání jako dvojnásobek odmocniny z počtu přítomných členů, nejméně však jedna setina a nejvýše jedna pětina z počtu přítomných členů. U návrhu na již zahájeném jednání se takto stanovený počet snižuje na polovinu.4)
    '''

    zaklad = 2 * sqrt(total)
    minimium = total / 100
    maximum = total / 5

    if zaklad > maximum:
        return maximum
    elif zaklad < minimum:
        return minimum
    else:
        return zaklad

def getSkupinaZahajeni(total):
    return int(round(__countSkupinaZahajeni(total), 0))

def getSkupinaProbihajici(total):
    return int(round(__countSkupinaZahajeni(total) / 2, 0))