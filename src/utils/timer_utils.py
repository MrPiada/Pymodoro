from src.globals import Globals
from src.Pomodoro import TimerType


def get_next_tymer_type(timer_type):
    switch_dict = {
        TimerType.POMODORO: TimerType.PAUSE,
        TimerType.PAUSE: TimerType.POMODORO,
        TimerType.LONG_PAUSE: None,
    }

    return switch_dict.get(timer_type, None)


def get_timer_color(timer_type):
    switch_dict = {
        TimerType.POMODORO: "success",
        TimerType.PAUSE: "info",
        TimerType.LONG_PAUSE: "info",
    }

    return switch_dict.get(timer_type, None)
