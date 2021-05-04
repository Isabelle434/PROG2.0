from flask import Flask
from flask import render_template

app = Flask("Bootstrap_Demo")


@app.route("/")
def start():
    name="Isabelle"
    cards = [{"title": "Card 0", "inhalt": "Blubber"},
             {"title": "Card 1", "inhalt": "Bla"},
             {"title": "Card 1", "inhalt": "Bla"},
             {"title": "Card 1", "inhalt": "Bla"},
             {"title": "Card 1", "inhalt": "Bla"},
             {"title": "Card 1", "inhalt": "Bla"},
             {"title": "Card 1", "inhalt": "Bla"},
             {"title": "Card 1", "inhalt": "Bla"},
             {"title": "Card 1", "inhalt": "Bla"},
             {"title": "Card 2", "inhalt": "Käsekuchen"}
             ]
    return render_template("start.html", name=name, cards=cards, )



if __name__ == "__main__":
    app.run(debug=True, port=5000)

