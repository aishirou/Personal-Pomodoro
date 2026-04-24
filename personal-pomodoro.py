import time
import sys

def timer_countdown(seconds):
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            print(f"Time remaining: {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            seconds -= 1
        print("Time's up!              ")
    except KeyboardInterrupt:
        print("\nTimer stopped.")
        sys.exit()

def pomodoro_timer():
    try:
        work = int(input("Enter work minutes: "))
        break_m = int(input("Enter break minutes: "))
        
        while True:
            print("\n--- Work Time! ---")
            timer_countdown(work * 60)
            print("\n--- Break Time! ---")
            timer_countdown(break_m * 60)
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    pomodoro_timer()
