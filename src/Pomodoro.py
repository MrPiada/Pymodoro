import time
import threading
from enum import Enum

from src.utils.db import *

POMODORO = None


class TimerType(Enum):
    POMODORO = 1
    PAUSE = 2
    LONG_PAUSE = 3


class Pomodoro:
    def __init__(self, timer_type, duration, category, sub_category=None):
        print(timer_type)
        self.initial_duration = duration  # seconds
        self._duration = duration
        self.timer_type = timer_type
        self.timer_thread = None
        self.stop_timer = False
        self.category = category
        self.sub_category = sub_category
        self.db_id = None
        self.lock = threading.Lock()

        self.__start()

    def __str__(self):
        return f"Pomodoro(timer_type={
            self.timer_type.name}, duration={
            self._duration}s, category={
            self.category}, sub_category={
                self.sub_category})"

    @property
    def duration(self):
        with self.lock:
            return self._duration

    @property
    def initial_durationduration(self):
        return self.initial_duration

    def is_ticking(self):
        return self._duration > 0

    def __start(self):
        log("INFO", f"Start pomodoro ({self})")
        if self.timer_type == TimerType.POMODORO:
            self.db_id = insert_pomodoro(
                self._duration,
                self.category,
                self.sub_category)
            self.timer_thread = threading.Thread(target=self._run_timer)
            self.timer_thread.start()
        else:
            self.db_id = insert_pause(
                self._duration,
                self.category,
                self.timer_type.name)
            self.timer_thread = threading.Thread(target=self._run_timer)
            self.timer_thread.start()

    def stop(self):
        with self.lock:
            self.stop_timer = True

        self._duration = 0
        log("INFO", f"Stop pomodoro ({self})")

        if self.timer_type == TimerType.POMODORO:
            update_pomodoro_stop_time(self.db_id)
        else:
            update_pause_stop_time(self.db_id)

    def _run_timer(self):
        while self.duration > 0 and not self.stop_timer:
            mins, secs = divmod(self.duration, 1)
            timeformat = '{:02.0f}:{:02.0f}'.format(mins, secs * 60)
            print(timeformat, end='\r')
            time.sleep(1)
            self._duration -= 1
            if self._duration <= 0:
                self._duration = 0
