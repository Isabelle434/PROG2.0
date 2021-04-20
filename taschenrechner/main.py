from flask import Flask
from flask import render_template
from flask import request

app = Flask("Taschenrechner")

@app.route("/rechner/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        eingabe_1 = int(request.form['zahl1'])
        eingabe_2 = int(request.form['zahl2'])
        eingabe_3 = int(request.form['zahl3'])
        summe = eingabe_1 + eingabe_2 + eingabe_3
        return render_template("result.html", resultat=str(summe))
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)