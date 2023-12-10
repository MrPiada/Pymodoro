from dash import html
import dash_bootstrap_components as dbc
from src.dashboard.widgets.timer_button import *

timer_tab = html.Div([
    html.H1("Timer"),
    timer_button
])
