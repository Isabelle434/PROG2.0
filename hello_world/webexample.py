import plotly.express as px

def test():
    x_achse = ["PROG1", "PROG2", "PROM", "REQE", "MIKR", "WPFL"]
    y_achse = [10, 20, 15, 22, 43, 2]
    title = "Stuff"
    fig = px.bar(
        x=x_achse,
        y=y_achse,
        title=title,
        color=y_achse,
        labels={"x": "Fächer", "y": "Spassfaktor"}
    )
    fig.show()



if __name__ == "__main__":
    test()