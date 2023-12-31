from src.globals import Globals
from src.Pomodoro import TimerType


def get_next_tymer_type(timer_type):
    switch_dict = {
        TimerType.POMODORO: TimerType.PAUSE,
        TimerType.PAUSE: TimerType.POMODORO,
        TimerType.LONG_PAUSE: None,
    }

    return switch_dict.get(timer_type, None)
