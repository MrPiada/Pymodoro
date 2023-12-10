from dash.dependencies import Input, Output
from src.dashboard.widgets.timer_button import *

def get_callbacks(app):
    @app.callback(
        Output("play-icon", "className"),
        Input("timer-button", "n_clicks"),
        prevent_initial_call=True
    )
    def toggle_play(n_clicks):
        if n_clicks % 2 == 0:
            return "bi bi-play-circle-fill"
        else:
            return "bi bi-stop-circle-fill"        
