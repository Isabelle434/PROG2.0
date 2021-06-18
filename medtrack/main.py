from flask import Flask
from flask import render_template
from flask import request


import daten

app = Flask("medtrack")

# Bekommt ein Suchbegriff aus dem Formular der Seite index.html und ruft die suche Funktion auf (Datei Daten.py)
@app.route("/index/", methods=['GET', 'POST'])
def suche():
    if request.method == 'POST':
        suche_person = request.form['suchbegriff']
        ergebnis = daten.suche(suche_person)
        if ergebnis == "Nein":
            return render_template("index.html", suchfunktion="Unter diesem Namen gibt es keinen Eintrag. Bitte überprüfe die Schreibweise.")
        else:
            return render_template("suche.html", suchbegriff=suche_person, datensatz=ergebnis)
    else:
        return render_template("index.html")

# Bekommt die Daten aus dem Formular der Seite abschluss.html und ruft die speichernlog Funktion auf (Datei Daten.py).
@app.route("/abschluss", methods=['GET', 'POST'])
def abschluss():
    if request.method == 'POST':
        person = request.form['person']
        datum = request.form['datum']
        try:
            morgen = request.form['morgen']
        except:
            morgen = "Nein"
        try:
            mittag = request.form['mittag']
        except:
            mittag = "Nein"
        try:
            abend = request.form['abend']
        except:
            abend = "Nein"
        try:
            nacht = request.form['nacht']
        except:
            nacht = "Nein"
        daten.speichernlog(person, datum, morgen, mittag, abend, nacht)
        return render_template("abschluss.html", tagesabschluss="Der Tagesabschluss wurde erfolgreich erfasst.")
    else:
        return render_template("abschluss.html")

# Bekommt die Daten aus dem Formular und ruft die Speichern Funktion auf (Datei Daten.py).
@app.route("/neuereintrag/", methods=['GET', 'POST'])
def neuereintrag():
    if request.method == 'POST':
        vorname = request.form['vorname']
        name = request.form['name']
        geburtstag = request.form['geburtstag']
        morgen = request.form['morgen']
        mittag = request.form['mittag']
        abend = request.form['abend']
        nacht = request.form['nacht']
        bemerkung = request.form['bemerkung']
        daten.speichern(vorname, name, geburtstag, morgen, mittag, abend, nacht, bemerkung)
        return render_template("erfasst.html", vorname=vorname, name=name, geburtstag=geburtstag, morgen=morgen, mittag=mittag, abend=abend, nacht=nacht, bemerkung=bemerkung)
    else:
        return render_template("neuereintrag.html")

# Bekommt vom Formular bzw. Button den value einer Person und ruft die Datensatz Funktion auf (Datei Daten.py)
# Danach wird logfile.html wiedergegeben, um die Einträge zu der aufgerufenen Person anzuzeigen.
@app.route("/personen", methods=['GET', 'POST'])
def allepersonen():
    if request.method == 'POST':
        person = request.form['logfileperson']
        datei = "logfile.json"
        logfile = daten.datensatz(datei, person)
        countermoja, countermonein, countermija, counterminein, counterabja, counterabnein,counternaja, counternanein = daten.df(datei, person)
        divmorgen = daten.piechart(countermoja, countermonein, "Morgens")
        divmittag = daten.piechart(countermija, counterminein, "Mittags")
        divabend = daten.piechart(counterabja, counterabnein, "Abends")
        divnacht = daten.piechart(counternaja, counternanein, "Nacht")
        return render_template("logfile.html", person=person, logfile=logfile, piechartmorgens=divmorgen, piechartmittags=divmittag, piechartabends=divabend, piechartnachts=divnacht)
    else:
        datei = "personen.json"
        personen = daten.alles(datei)
        return render_template("personen.html", personen=personen)

# Es werden alle Einträge der Datei logfile.json angezeigt.
# Es kann via Button zur Ansicht der Logfiles einer einzelnen Person gewechselt werden (Seite logfile.html).
@app.route("/logfiles", methods=['GET', 'POST'])
def allelogs():
    if request.method == 'POST':
        person = request.form['logfileperson']
        datei = "logfile.json"
        logfile = daten.datensatz(datei, person)
        countermoja, countermonein, countermija, counterminein, counterabja, counterabnein, counternaja, counternanein = daten.df(datei, person)
        divmorgen = daten.piechart(countermoja, countermonein, "Morgens")
        divmittag = daten.piechart(countermija, counterminein, "Mittags")
        divabend = daten.piechart(counterabja, counterabnein, "Abends")
        divnacht = daten.piechart(counternaja, counternanein, "Nacht")
        return render_template("logfile.html", person=person, logfile=logfile, piechartmorgens=divmorgen, piechartmittags=divmittag, piechartabends=divabend, piechartnachts=divnacht)
    else:
        datei = "logfile.json"
        logfiles = daten.alles(datei)
        return render_template("logfiles.html", logfiles=logfiles)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
