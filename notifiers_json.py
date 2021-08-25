'''
A very simple Notifier program ,not App ;) to open my class links. (I dont have to remember my class schedule
 all the time. Although i need to remember once XD)
'''

import json
from plyer import notification
import webbrowser
import time
import datetime
from datetime import timedelta

today = datetime.date.today()
date = f"{int(today.day)}-{int(today.month)}-{int(today.year)}"
day = today.strftime("%A")

def isHoliday(data, date):
    day = date.strftime("%A")
    if date in data:
        return True
    elif day == "Saturday" or day == 'Sunday':
        return True
    return False

def getEndTime(data, day):
    times_data = []
    for dat in data:
        for d in dat['times']:
            if day in d:
                times_data.append((datetime.datetime.strptime(d.split("-")[-1], "%H:%M").time().hour + 1) % 24)
    return max(times_data)

def getStartTime(data, day):
    times_data = []
    for dat in data:
        for d in dat['times']:
            if day in d:
                times_data.append((datetime.datetime.strptime(d.split("-")[-1], "%H:%M").time().hour) % 24)
    return min(times_data)

def NextWorkingDay(today, data):
    today += timedelta(1)
    while True:
        if isHoliday(data=data, date=today):
            today += timedelta
        else:
            break
    return f"{today.strftime('%d')} {today.strftime('%b')}"

with open("times.json") as file:
    DATA = json.load(file)
data = DATA["classtimes"]
holiday_data = DATA["holidays"]
ENDTIME = getEndTime(data, day)
STARTTIME = getStartTime(data, day)

print("Program has started")

if date in holiday_data.keys():
    print(f"Sir, today is a holiday on account of {holiday_data[date]} occasion. You don't have any classes today")
elif day == "Saturday" or day == "Sunday":
    print(f"Sir, today is a weekend. You don't have any classes today")
else:
    while STARTTIME <= datetime.datetime.now().time().hour < ENDTIME:
        now = datetime.datetime.now().time().strftime("%X")[0:5]
        day = datetime.date.today().strftime("%A")
        date = f"{int(today.day)}-{int(today.month)}-{int(today.year)}"
        for dt in data:
            if dt['status']:
                for t in dt['times']:
                    if (day in t) and (now in t):
                        print(f"Opening {dt['name']} meeting @ {dt['link']} link")
                        print(f"Your LMS is {dt['lms']}")
                        if 'team' not in dt['lms']:
                            webbrowser.open_new_tab(dt['lms'])
                        notification.notify(
                            title="CLASS NOW",
                            message=f"Please join the {dt['name']} class via the opened link ASAP",
                            app_icon=None,
                            timeout=5,
                            toast=True
                        )
                        webbrowser.open_new_tab(dt['link'])
                        time.sleep(3599)
        time.sleep(0.5)
    print(f"All your classes are done for the day. See you on {NextWorkingDay(today, holiday_data)}, sir!!")