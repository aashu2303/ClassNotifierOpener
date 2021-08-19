'''
A very simple Notifier program ,not App ;) to open my class links. (I dont have to remember my class schedule
 all the time. Although i need to remember once XD)
'''

import json
from plyer import notification
import webbrowser
import time
import datetime

today = datetime.date.today()
year, month, date = today.year, today.month, today.day
day = today.strftime("%A")
ENDTIME = 18

with open("times.json") as file:
    data = json.load(file)["classtimes"]

print("Program has started")

while datetime.datetime.now().time().hour < ENDTIME:
    now = datetime.datetime.now().time().strftime("%X")[0:5]
    for dt in data:
        if dt['status']:
            for t in dt['times']:
                if (day in t) and (now in t):
                    print(f"Opening {dt['name']} meeting @ {dt['link']} link")
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