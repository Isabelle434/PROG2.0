from datetime import datetime
import json

def speichern(vorname, name, geburtstag, morgen, mittag, abend, nacht, bemerkung):
    datei = "personen.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(vorname) + " " + str(name)] = {
        "Vorname": vorname,
        "Name": name,
        "Geburtsdatum": geburtstag,
        "Morgen": morgen,
        "Mittag": mittag,
        "Abend": abend,
        "Nacht": nacht,
        "Bemerkungen": bemerkung
    }

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def suche(suchbegriff):
    with open("personen.json") as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        if suchbegriff in my_read_dict.keys():
            result = my_read_dict[suchbegriff]
        else:
            result = "no"
        return result


def speichernlog(person, datum, morgen, mittag, abend, nacht):
    datei = "logfile.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(person)][datum] = {
        "Morgen": morgen,
        "Mittag": mittag,
        "Abend": abend,
        "Nacht": nacht
    }

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

def alles(datei):
    with open(datei) as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        return my_read_dict

