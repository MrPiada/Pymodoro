from src.utils import *
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from src.dashboard.callbacks import get_callbacks
from src.dashboard.style import *
from src.dashboard.timer import *
from src.dashboard.stats import *
from src.dashboard.config import *
from src.db import *
from src.globals import *

# Call the setupdb function to initialize the database
setupdb()
log("INFO", "STARTUP")

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.SKETCHY,
        dbc.icons.BOOTSTRAP],
    title='PyModoro'
)

tabs = dbc.Tabs([dbc.Tab(label='Timer ⏱️',
                         tab_id='timer',
                         children=timer_tab),
                 dbc.Tab(label='Stats 📊',
                         tab_id='stats',
                         children=stats_tab),
                 dbc.Tab(label='Config ⚙️',
                         tab_id='config',
                         children=config_tab,
                         tab_style={"marginLeft": "auto"}),
                 ],
                id='tabs',
                active_tab='timer')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    tabs,
])

get_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
