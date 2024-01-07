from src.Pomodoro import TimerType
import json


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


def dict_to_string(d):
    return json.dumps(d)


def string_to_dict(str):
    return json.loads(str)
