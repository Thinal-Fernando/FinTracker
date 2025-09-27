from dash import Dash,html


app = Dash()

app.layout = ([
    html.Div(children="FinTrack")
])

if __name__  == "__main__":
    app.run(debug=True)