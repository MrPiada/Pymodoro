import time
import threading
from enum import Enum

POMODORO = None

class TimerType(Enum):
    POMODORO = 1
    BREAK = 1
    LONG_BREAK = 2

class Pomodoro:
    def __init__(self, timer_type, duration):
        self._duration = duration # seconds
        self.timer_type = timer_type
        self.timer_thread = None
        self.stop_timer = False
        self.lock = threading.Lock()
        
        self.__start()
        
    @property
    def duration(self):
        with self.lock:
            return self._duration

    def __start(self):
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.start()

    def stop(self):
        with self.lock:
            self.stop_timer = True
        print("Stop timer")

    def _run_timer(self):
        print(f"Starting a timer of {self.duration}s")
        while self.duration > 0 and not self.stop_timer:
            mins, secs = divmod(self.duration, 1)
            timeformat = '{:02.0f}:{:02.0f}'.format(mins, secs * 60)
            print(timeformat, end='\r')
            time.sleep(1)
            self._duration -= 1
        print(f"End of timer")

