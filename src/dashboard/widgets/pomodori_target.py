from dash import html
import dash_bootstrap_components as dbc

pomodori_target = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H2("Obiettivo giornaliero:"),
                    width=6),
                dbc.Col(
                    html.H2(
                        id='obiettivo-giornaliero',
                        style={
                            'color': 'orange'}),
                    width=6),
            ]),
        dbc.Row(
            [
                dbc.Col(
                    html.H2("Obiettivo settimanale:"),
                    width=6),
                dbc.Col(
                    html.H2(
                        id='obiettivo-settimanale',
                        style={
                            'color': 'orange'}),
                    width=6),
            ]),
    ],
    fluid=True)
