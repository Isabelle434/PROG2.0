from flask import Flask
from flask import render_template
from flask import request

app = Flask("Home")




@app.route("/index/", methods=['GET', 'POST'])
def suche():
    if request.method == 'POST':
        suche_person = request.form['suchbegriff']
        return render_template("suche.html", suchbegriff=suche_person)
    else:
        return render_template("index.html")


@app.route("/neuereintrag/")
def neuereintrag():
    return render_template("neuereintrag.html")


#def neuereintrag():
#    if request.method == 'POST':
#        vorname_person = request.form['vorname_neu']
#        nachname_person = request.form['vorname_neu']
#        return render_template("neuereintrag.html", vorname_neu=vorname_person, nachname_neu=nachname_person)
#    else:
#        return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True, port=5000)