import datetime
from dash.dependencies import Input, Output
from src.dashboard.widgets.timer_button import *

from src.Pomodoro import *
from src.utils.db import *
from src.dashboard.widgets.timer_countdown import *


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
            selected_timer = TimerType.PAUSE
            POMODORO = Pomodoro(selected_timer, 20, "DummyCategory")
            return "bi bi-stop-circle-fill"

    @app.callback(
        [Output('timer-display', 'children'),
         Output('progress-bar', 'value')],
        Input('interval-component', 'n_intervals')
    )
    def update_timer(n):
        global POMODORO
        remaining_seconds = POMODORO.duration
        initial_seconds = POMODORO.initial_duration

        remaining_time = str(datetime.timedelta(seconds=remaining_seconds))

        progress_percentage = (
            float(remaining_seconds) / initial_seconds) * 100

        return f'{remaining_time}', progress_percentage
