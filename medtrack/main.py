from flask import Flask
from flask import render_template
from flask import request


import daten

app = Flask("medtrack")


@app.route("/index/", methods=['GET', 'POST'])
def suche():
    if request.method == 'POST':
        suche_person = request.form['suchbegriff']
        ergebnis = daten.suche(suche_person)
        return render_template("suche.html", suchbegriff=suche_person, datensatz=ergebnis)
    else:
        return render_template("index.html")

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

@app.route("/personen", methods=['GET', 'POST'])
def allepersonen():
    if request.method == 'POST':
        #button = request.form['button']
        #if button == "logfileperson":
        person = request.form['logfileperson']
        datei = "logfile.json"
        logfile = daten.datensatz(datei, person)
        return render_template("logfile.html", person=person, logfile=logfile)
        #if button == "tagesabschluss":
        #    person = request.form['tagesabschluss']
        #    return render_template("abschluss.html", person=person)
    else:
        datei = "personen.json"
        personen = daten.alles(datei)
        return render_template("personen.html", personen=personen)


@app.route("/logfiles")
def allelogs():
    datei = "logfile.json"
    logfiles = daten.alles(datei)
    return render_template("logfiles.html", logfiles=logfiles)





if __name__ == "__main__":
    app.run(debug=True, port=5000)
