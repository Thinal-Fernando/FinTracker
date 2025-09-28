from dash import Dash,html

def create_dashboard(server):
    dash_app = Dash(__name__, server=server, url_base_pathname="/statistics/")

    dash_app.layout = ([
        html.Div(children="FinTrack")
    ])


    return dash_app