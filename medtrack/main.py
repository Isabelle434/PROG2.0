from flask import Flask
from flask import render_template
from flask import request

import daten

app = Flask("medtrack")


@app.route("/index/", methods=['GET', 'POST'])
def suche():
    if request.method == 'POST':
        suche_person = request.form['suchbegriff']
        return daten.suche(suche_person)
    else:
        return render_template("index.html")


#@app.route("/neuereintrag/", methods=['GET', 'POST'])
#def neuereintrag():
#    if request.method == 'POST':
#        vorname_person = request.form['vorname_neu']
#        nachname_person = request.form['vorname_neu']
#        geburtsdatum_person = request.form['geburtsdatum_neu']
#        morgen_person = request.form['morgen_neu']
#        mittag_person = request.form['mittag_neu']
#        abend_person = request.form['abend_neu']
#        nacht_person = request.form['nacht_neu']
#        bemerkungen_person = request.form['bemerkungen_neu']
#        return render_template("erfasst.html", vorname_neu=vorname_person, nachname_neu=nachname_person, geburtsdatum_neu=geburtsdatum_person, morgen_neu=morgen_person, mittag_neu=mittag_person, abend_neu=abend_person, nacht_neu=nacht_person, bemerkungen_neu=bemerkungen_person)
#        vorname_person, nachname_person = daten.eintrag_speichern(vorname_person, nachname_person)
#    else:
#        return render_template("neuereintrag.html")

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
        daten.eintrag_speichern(vorname, name, geburtstag, morgen, mittag, abend, nacht, bemerkung)
        return render_template("erfasst.html", vorname=vorname, name=name, geburtstag=geburtstag, morgen=morgen, mittag=mittag, abend=abend, nacht=nacht, bemerkung=bemerkung)
    else:
        return render_template("neuereintrag.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
