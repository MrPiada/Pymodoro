from src.Pomodoro import *

print(POMODORO)

# this will be called with:
# global TIMER
# TIMER =
# TIMER.stop() 
POMODORO = Pomodoro(TimerType.POMODORO, 12)

time.sleep(5)
print(f"\nduration: {POMODORO.duration}\n")
time.sleep(1)
print(f"\nduration: {POMODORO.duration}\n")
time.sleep(1)
POMODORO.stop()
