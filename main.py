import os
import sys
import time

if sys.platform in "linux":
    clear = "clear"
elif sys.platform in "win32":
    clear = "cls"
else:
    print("System not recognized! Clearing the screen of the console will most likely result in some errors.")
def clear_screen():
    os.system(clear)

def stopwatch_timer():
    print("**STOPWATCH TIMER**")
    print("You've selected the stopwatch timer. The stopwatch will go on forever until you exit out of the program. Or until the stopwatch reaches 100 hours.")
    print("Press enter to proceed.")
    proceed = input()
    if proceed == "":
        clear_screen()
        seconds = 0
        minutes = 0
        hours = 0
        while True:
            print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            seconds += 1
            if seconds == 60:
                seconds = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
            if hours == 100:
                break
            time.sleep(1)
            clear_screen()
    else:
        print("Something other than enter has been entered. Please run the program and try again.")

clear_screen()
print("Paradajz - work more efficiently. Choose your options:")
print("1. Pomodoro timer")
print("2. Countdown timer")
print("3. Stopwatch timer")

while True:
    choice = input()
    match choice:
        case "1":
            break
        case "2":
            break
        case "3":
            clear_screen()
            stopwatch_timer()
            break
        case _:
            print("Wrong choice! Please ")
