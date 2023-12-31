from enum import Enum


class TimerType(Enum):
    POMODORO = 1
    PAUSE = 2
    LONG_PAUSE = 3


NEW_CATEGORY = '+ ADD NEW CATEGORY'

daily_target = 5
weekly_target = 10


class Globals:
    POMODORO = None
    POMODORI_TODAY = 0
    POMODORI_LAST_WEEK = 0
    CATEGORIES = ["pippo", "ciccio", 'piada', NEW_CATEGORY]
    NEXT_TIMER_TYPE = TimerType.POMODORO
