def gerade(zahl_1):
    if zahl_1 % 2 == 0:
        ergebnis = "gerade"
    else:
        ergebnis = "ungerade"
    return ergebnis

erste_zahl = 7
ergebnis = gerade(erste_zahl)
print(ergebnis)
