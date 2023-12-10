import time
import threading
from enum import Enum

from src.utils.db import *

POMODORO = None


class TimerType(Enum):
    POMODORO = 1
    PAUSE = 1
    LONG_PAUSE = 2


class Pomodoro:
    def __init__(self, timer_type, duration, category, sub_category=None):
        self._duration = duration  # seconds
        self.timer_type = timer_type
        self.timer_thread = None
        self.stop_timer = False
        self.category = category
        self.sub_category = sub_category
        self.db_id = None
        self.lock = threading.Lock()

        self.__start()

    def __str__(self):
        return f"Pomodoro(timer_type={self.timer_type.name}, duration={self._duration}s, category={self.category}, sub_category={self.sub_category})"

    @property
    def duration(self):
        with self.lock:
            return self._duration

    def __start(self):
        log("INFO", f"Start pomodoro ({self})")
        self.db_id = insert_pomodoro(
            25,
            self.category,
            self.sub_category)
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.start()

    def stop(self):
        with self.lock:
            self.stop_timer = True
        log("INFO", f"Stop pomodoro ({self})")
        update_pomodoro_stop_time(self.db_id)

    def _run_timer(self):
        while self.duration > 0 and not self.stop_timer:
            mins, secs = divmod(self.duration, 1)
            timeformat = '{:02.0f}:{:02.0f}'.format(mins, secs * 60)
            print(timeformat, end='\r')
            time.sleep(1)
            self._duration -= 1
