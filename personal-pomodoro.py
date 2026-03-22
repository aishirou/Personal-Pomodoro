import time
import os

def pomodoro_timer(work_mins, break_mins):
    # Convert minutes to seconds
    work_sec = work_mins * 60
    break_sec = break_mins * 60

    print(f"Timer started: {work_mins}m Work / {break_mins}m Break")
    
    while True:
        # Work Phase
        print("\n--- Work Time! Focus up. ---")
        timer_countdown(work_sec)
        
        # Break Phase
        print("\n--- Break Time! Stretch a bit. ---")
        timer_countdown(break_sec)

def timer_countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        # The \r allows the timer to overwrite the same line in the terminal
        print(f"Time remaining: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!                      ") # Clear the line

# Run it: 25 mins work, 5 mins break
pomodoro_timer(25, 5)
