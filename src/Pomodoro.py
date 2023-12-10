import time
import threading
from enum import Enum

from src.utils.db import *

POMODORO = None


class TimerType(Enum):
    POMODORO = 1
    BREAK = 1
    LONG_BREAK = 2


class Pomodoro:
    def __init__(self, timer_type, duration):
        self._duration = duration  # seconds
        self.timer_type = timer_type
        self.timer_thread = None
        self.stop_timer = False
        self.lock = threading.Lock()

        self.__start()

    def __str__(self):
        return f"Pomodoro(timer_type={self.timer_type.name}, duration={self._duration}s)"

    @property
    def duration(self):
        with self.lock:
            return self._duration

    def __start(self):
        log("INFO", f"Start pomodoro ({self})")
        insert_pomodoro(
            "13:02 8/12/2023",
            "13:27 8/12/2023",
            25,
            "Issue",
            "#321 pelloide")
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.start()

    def stop(self):
        with self.lock:
            self.stop_timer = True
        log("INFO", f"Stop pomodoro ({self})")

    def _run_timer(self):
        while self.duration > 0 and not self.stop_timer:
            mins, secs = divmod(self.duration, 1)
            timeformat = '{:02.0f}:{:02.0f}'.format(mins, secs * 60)
            print(timeformat, end='\r')
            time.sleep(1)
            self._duration -= 1
