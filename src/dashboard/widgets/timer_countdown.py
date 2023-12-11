from dash import html, dcc
import dash_bootstrap_components as dbc


timer_countdown = dbc.Container([
    html.H1(id='timer-display'),
    dcc.Interval(
        id='interval-component',
        interval=1000,  # intervallo di aggiornamento in millisecondi
        n_intervals=0
    ),
    dbc.Progress(id='progress-bar', value=100, striped=True, animated=True),
])
