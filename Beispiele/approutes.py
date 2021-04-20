from flask import Flask

app = Flask("Demo")

@app.route('/hello/')
@app.route('/hello/<name>') #diese beiden routen gehören zusammen, beide machen das was in def begruessung steht
def begruessung(name=False): #name ist gleich Wert False wenn kein name exisitert
    if name:
        return "Hallo " + name + "!"
    else:
        return "Not Hallo World again…"

if __name__ == "__main__":
    app.run(debug=True, port=5000)