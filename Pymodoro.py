import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from src.dashboard.style import *
from src.dashboard.timer import *
from src.dashboard.stats import *
from src.dashboard.config import *

from src.Pomodoro import *


# print(POMODORO)
# POMODORO = Pomodoro(TimerType.POMODORO, 12)
# print(f"\nduration: {POMODORO.duration}\n")
# POMODORO.stop()


app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.SKETCHY],
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


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
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
