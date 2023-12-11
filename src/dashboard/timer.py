from dash import html
import dash_bootstrap_components as dbc
from src.dashboard.widgets.timer_button import *
from src.dashboard.widgets.timer_countdown import *

timer_tab = dbc.Container([
    html.H1("Timer"),
    timer_countdown,
    timer_button,
],
    fluid=True)
