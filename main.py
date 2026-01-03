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

def countdown_timer():
    print("**COUNTDOWN TIMER**")
    print("You've selected the countdown timer. Please enter the time below (format: hh:mm:ss)")
    proceed = input()
    time_split = proceed.split(":")
    hours = int(time_split[0])
    minutes = int(time_split[1])
    seconds = int(time_split[2])
    clear_screen()
    while True:
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        seconds -= 1
        if seconds == -1 and minutes == 0 and hours == 0:
            break
        if seconds == -1:
            seconds = 59
            minutes -= 1
        if minutes == -1:
            minutes = 59
            if hours != 0:
                hours -= 1
        time.sleep(1)
        clear_screen()
    print("Timer done!")

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
            clear_screen()
            countdown_timer()
            break
        case "3":
            clear_screen()
            stopwatch_timer()
            break
        case _:
            print("Wrong choice! Please ")
