
def lineaarotsing(data, otsi_term): # sisenditeks on data ja otsingusõna
    for index, toode in enumerate(data): # käiakse läbi kõik indeksid ja tooted, enumerate aitab indeksitega järge pidada, ei pea manuaalselt seda osa koodis lahti kirjutama
        if otsi_term.lower() in toode['nimetus'].lower():
            return index
    return -1

def binaarotsing(data, otsi_term):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]['nimetus'].lower() == otsi_term.lower():
            return mid
        elif data[mid]['nimetus'].lower() < otsi_term.lower():
            low = mid + 1
        else:
            high = mid - 1
    return -1