from dash import html
import dash_bootstrap_components as dbc
from src.dashboard.widgets.timer_button import *
from src.dashboard.widgets.timer_countdown import *
from src.dashboard.widgets.category_choice import *
from src.dashboard.widgets.pomodori_target import *

timer_tab = dbc.Container([
    html.H1("Timer"),
    pomodori_target,
    timer_countdown,
    timer_button,
    category_choice
],
    fluid=True)
