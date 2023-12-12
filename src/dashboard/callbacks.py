import datetime
from dash.dependencies import Input, Output
from src.dashboard.widgets.timer_button import *

from src.Pomodoro import *
from src.utils.db import *
from src.dashboard.widgets.timer_countdown import *


def get_callbacks(app):
    @app.callback(
        Output("play-icon", "className", allow_duplicate=True),
        Input("timer-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def toggle_play(n_clicks):
        global POMODORO
        is_ticking = False
        if POMODORO is not None:
            is_ticking = POMODORO.is_ticking()

        if is_ticking:
            POMODORO.stop()
            return "bi bi-play-circle-fill"
        else:
            selected_timer = TimerType.PAUSE
            POMODORO = Pomodoro(selected_timer, 20, "DummyCategory")
            return "bi bi-stop-circle-fill"

    @app.callback(
        [Output('timer-display', 'children'),
         Output('progress-bar', 'value'),
         Output("play-icon", "className", allow_duplicate=True)],
        Input('interval-component', 'n_intervals'),
        prevent_initial_call=True,
    )
    def update_timer(n):
        global POMODORO
        is_ticking = False
        if POMODORO is not None:
            remaining_seconds = POMODORO.duration
            initial_seconds = POMODORO.initial_duration

            remaining_time = str(datetime.timedelta(seconds=remaining_seconds))

            progress_percentage = (
                float(remaining_seconds) / initial_seconds) * 100

            is_ticking = POMODORO.is_ticking()
            icon = "bi bi-play-circle-fill"
            if is_ticking:
                icon = "bi bi-stop-circle-fill"

            return f'{remaining_time}', progress_percentage, icon
        else:
            return 0, None, "bi bi-play-circle-fill"
