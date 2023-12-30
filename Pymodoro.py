import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from src.dashboard.callbacks import get_callbacks
from src.dashboard.style import *
from src.dashboard.timer import *
from src.dashboard.stats import *
from src.dashboard.config import *
from src.utils.db import *
from src.globals import *

# Call the setupdb function to initialize the database
setupdb()
log("INFO", "STARTUP")

# # Example usage:
# insert_pomodoro(
#     "13:02 8/12/2023",
#     "13:27 8/12/2023",
#     25,
#     "Issue",
#     "#321 pelloide")
# insert_pause("13:02 8/12/2023", "13:17 8/12/2023", 15, "coffe")
# insert_config("username", "Ciccio")
# insert_random_pause_category("scacchi", 3)
# insert_random_pause_category("reading", 5)
# insert_obiettivi("daily", 1, 10)


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
        print(Globals.POMODORI_TODAY, Globals.POMODORI_LAST_WEEK)
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
