from dash import html
import dash_bootstrap_components as dbc

timer_button = dbc.Button(
    html.I(className="bi bi-play-circle-fill", id="play-icon", style={"font-size": "2rem"}),
    color="primary",
    className="rounded-circle",
    id="play-button"
)
