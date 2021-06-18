import json
from plotly.offline import plot
import plotly.express as px


# Quelle für das Öffnen der Datei (json.load, usw.) sind die Vorlesungsunterlagen.


# Neuer Eintrag in JSON Datei speichern
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

# Suchfunktion, welche die Keys des Dictionary nach dem Suchbegriff durchsucht
# Wenn dieser exakt gefunden wird, wird das entsprechende Dictionary als Resultat zurückgegeben.
# Ansonsten wird die Meldung, dass kein Eintrag gefunden wurde, zurückgegeben.
def suche(suchbegriff):
    with open("personen.json") as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        if suchbegriff in my_read_dict.keys():
            result = my_read_dict[suchbegriff]
        else:
            result = "Nein"
        return result

# Speichern eines Tagesabschlusses in der JSON Datei
def speichernlog(person, datum, morgen, mittag, abend, nacht):
    datei = "logfile.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    if str(person) in datei_inhalt:
        datei_inhalt[str(person)][datum] = {
            "Morgen": morgen,
            "Mittag": mittag,
            "Abend": abend,
            "Nacht": nacht
        }
    else:
        datei_inhalt[str(person)] = {}
        datei_inhalt[str(person)][datum] = {
            "Morgen": morgen,
            "Mittag": mittag,
            "Abend": abend,
            "Nacht": nacht
        }

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

# Laden des kompletten Inhaltes einer Datei.
# Wird verwendet für die Approutes "Allepersonen" und "Allelogs".
def alles(datei):
    with open(datei) as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        return my_read_dict

# Aufrufen eines einzelnen Datensatzes (verschachteltes Dictionary) aus der JSON Datei.
# Wird verwendet in der Approute "Allepersonen" und "Allelogs", wenn bei einer Person auf "Logfiles" geklickt wird.
def datensatz(datei, person):
    with open(datei) as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        return my_read_dict[person]

#Quelle: https://plotly.com/python/pie-charts/ und Vorlesungsunterlagen aus Programmieren 2
#Visualisiert aus Ja und Nein Werten ein Kuchendiagramm.
def piechart(counterja, counternein, titel):
    dfmo = {
    "Names": [
        "Ja",
        "Nein"
        ],
    "Values": [
        counterja,
        counternein
    ]
    }
    fig = px.pie(dfmo, names="Names", values="Values", title=titel, color_discrete_sequence=["green", "red"])
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    div = plot(fig, output_type="div")
    return div

def df(datei, person):
    with open(datei) as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        countermoja = 0
        countermonein = 0
        countermija = 0
        counterminein = 0
        counterabja = 0
        counterabnein = 0
        counternaja = 0
        counternanein = 0
        dict = my_read_dict[person]
        for key, value in dict.items():
            if value["Morgen"] == "Ja":
                countermoja = countermoja +1
            else:
                countermonein = countermonein +1
            if value["Mittag"] == "Ja":
                countermija = countermija +1
            else:
                counterminein = counterminein +1
            if value["Abend"] == "Ja":
                counterabja = counterabja +1
            else:
                counterabnein = counterabnein +1
            if value["Nacht"] == "Ja":
                counternaja = counternaja +1
            else:
                counternanein = counternanein +1
        return countermoja, countermonein, countermija, counterminein, counterabja, counterabnein,counternaja, counternanein

