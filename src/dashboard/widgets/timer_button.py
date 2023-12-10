from dash import html
import dash_bootstrap_components as dbc

timer_button = dbc.Button(
    html.I(
        className="bi bi-play-circle-fill",
        id="play-icon",
        style={
            "font-size": "18rem",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center"}),
    # color="primary",
    className="rounded-circle",
    id="timer-button",
    style={
        "width": "20rem",
        "height": "20rem"},
    color="danger")
