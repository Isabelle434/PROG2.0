import json

def speichern(datei, keyv, keyn, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(keyv) + " " + str(keyn)] = value

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def eintrag_speichern(vorname, name, bemerkung):
    datei_name = "persontest.json"
    speichern(datei_name, vorname, name, bemerkung)
    return vorname, name


def suche(suchbegriff):
    datei_name = "persontest.json"
    result = datei_name[suchbegriff]
    return result