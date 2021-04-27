from flask import Flask
from flask import render_template
from flask import request

app = Flask("Hello")




#@app.route("/hello/", methods=['GET', 'POST'])
#def hallo():
#    if request.method == 'POST':
#       ziel_person = request.form['vorname']
#        #rueckgabe_string = "Hello " + ziel_person + "!"
#        #return rueckgabe_string #anstelle von dem könnte hier auch mit render_template auf eine andere html Seite verwiesen werden (return render_template("hello.html", name=ziel_person)
#        return render_template("begruessung.html", ansprechsperson=ziel_person)
#    else:
#        return render_template("hello.html")

@app.route("/jinjabegruessung/", methods=['GET', 'POST'])
def hallojinja():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        return render_template("begruessung.html", ansprechsperson=ziel_person, elements=["Eins", "Zwei", "Drei"])
    else:
        return render_template("hello.html")


@app.route("/jinja/", methods=['GET', 'POST'])
def jinjazahl():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        zahl1 = int(request.form['zahl1'])
        zahl2 = int(request.form['zahl2'])
        return render_template("jinja.html", ansprechperson=ziel_person, zahl1=zahl1, zahl2=zahl2)
    else:
        return render_template("hello.html")



@app.route("/testen")
def test():
    return "success"


if __name__ == "__main__":
    app.run(debug=True, port=5000)