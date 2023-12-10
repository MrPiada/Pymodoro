from dash.dependencies import Input, Output
from src.dashboard.widgets.timer_button import *

from src.Pomodoro import *
from src.utils.db import *

def get_callbacks(app):
    @app.callback(
        Output("play-icon", "className"),
        Input("timer-button", "n_clicks"),
        prevent_initial_call=True
    )
    def toggle_play(n_clicks):
        global POMODORO
        if n_clicks % 2 == 0:
            POMODORO.stop()
            return "bi bi-play-circle-fill"
        else:
            POMODORO = Pomodoro(TimerType.POMODORO, 20)
            return "bi bi-stop-circle-fill"        
