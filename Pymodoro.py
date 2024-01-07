from src.utils import *
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
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


pause_categories = {
    "scacchi": 3,
    "push_up": 2,
    "pull_up": 1,
    "planck": 2,
    "reading": 2,
    "youtube": 1
}
insert_config('pippo', dict_to_string(pause_categories))


app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.SKETCHY,
        dbc.icons.BOOTSTRAP],
    title='PyModoro'
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

content = html.Div(id="page-content", style=CONTENT_STYLE)

sidebar = html.Div([html.H2("PyModoro",
                            className="display-4"),
                    html.Hr(),
                    dbc.Nav([dbc.NavLink("Timer",
                                         href="/",
                                         active="exact"),
                            dbc.NavLink("Stats",
                                        href="/stats",
                                        active="exact"),
                            dbc.NavLink("Config",
                                        href="/config",
                                        active="exact"),
                             ],
                            vertical=True,
                            pills=True,
                            ),
                    ],
                   style=SIDEBAR_STYLE,
                   )

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

get_callbacks(app)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        Globals.POMODORI_TODAY, Globals.POMODORI_LAST_WEEK = count_past_pomodori()
        return html.Div(children=[
            timer_tab
        ]),
    elif pathname == "/stats":
        return html.Div(children=[
            stats_tab
        ]),
    elif pathname == "/config":
        return html.Div(children=[
            config_tab
        ]),
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == '__main__':
    app.run_server(debug=True)
