import datetime
from dash import Input, Output, State, ctx

from src.Pomodoro import *
from src.utils.db import *

from src.dashboard.widgets.timer_button import *
from src.dashboard.widgets.timer_countdown import *
from src.dashboard.widgets.category_choice import *


def get_callbacks(app):
    @app.callback(
        Output("play-icon", "className", allow_duplicate=True),
        Input("timer-button", "n_clicks"),
        State('selected-category', 'data'),
        prevent_initial_call=True,
    )
    def toggle_play(n_clicks, selected_category):
        global POMODORO
        is_ticking = False
        if POMODORO is not None:
            is_ticking = POMODORO.is_ticking()

        if is_ticking:
            POMODORO.stop()
            return "bi bi-play-circle-fill"
        else:
            selected_timer = TimerType.PAUSE  # TODO: switch between pomodori and pauses
            POMODORO = Pomodoro(selected_timer, 20, selected_category)
            return "bi bi-stop-circle-fill"

    # Callback per disabilitare il pulsante quando selected_category è None
    @app.callback(
        Output("timer-button", "disabled"),
        [Input('selected-category', 'data')],
        prevent_initial_call=True,
    )
    def disable_button(selected_category):
        return selected_category is None

    @app.callback(
        [Output('timer-display', 'children'),
         Output('progress-bar', 'value'),
         Output("play-icon", "className", allow_duplicate=True),
         Output("timer-button", "disabled", allow_duplicate=True)],
        Input('interval-component', 'n_intervals'),
        State("timer-button", "disabled"),
        prevent_initial_call=True,
    )
    def update_timer(n, button_disabled_state):
        global POMODORO
        is_ticking = False
        disable_button = button_disabled_state
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
                disable_button = False

            return f'{remaining_time}', progress_percentage, icon, disable_button
        else:
            return 0, None, "bi bi-play-circle-fill", disable_button

    @app.callback(
        Output("category-choice-modal", "is_open"),
        Output("category-dropdown", 'options'),
        Output("category-dropdown", 'value'),
        Input("category-ok", "n_clicks"),
        Input("category-cancel", "n_clicks"),
        Input("category-dropdown", "value"),
        State("category-dropdown", "options"),
        State("category-name-input", 'value'),
        State("category-choice-modal", "is_open"),
        prevent_initial_call=True
    )
    def toggle_modal(
            ok,
            cancel,
            drop_value,
            drop_options,
            input_value,
            is_open):

        global CATEGORIES

        # which component has triggered the callback?
        trigger = ctx.triggered_id

        # change of drop down value triggered
        if trigger == 'category-dropdown':
            if NEW_CATEGORY in drop_value:
                # if 'new category', open modal
                return not is_open, drop_options, drop_value
            else:
                # if not 'new category', do nothing
                return is_open, drop_options, drop_value

        # ok button has been clicked
        if trigger == 'category-ok':
            # ok has been clicked, update the drop-down options
            new_options = [opt for opt in drop_options]
            new_options.insert(-1, input_value)
            new_values = [val for val in drop_value if val != NEW_CATEGORY]
            new_values.append(input_value)

            if input_value not in CATEGORIES:
                CATEGORIES.insert(-1, input_value)

            return not is_open, new_options, new_values

        # cancel button has been clicked
        if trigger == 'category-cancel':
            # cancel has been clicked, do not change options but return already
            # selected to drop down value
            existing_values = [
                val for val in drop_value if val != NEW_CATEGORY]
            return not is_open, drop_options, existing_values

    @app.callback(
        Output('selected-category', 'data'),
        Input('category-dropdown', 'value')
    )
    def update_selected_category(selected_value):
        return selected_value
