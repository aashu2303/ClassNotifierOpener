'''
A very simple Notifier program ,not App ;) to open my class links. (I dont have to remember my class schedule
 all the time. Although i need to remember once XD)
'''

from plyer import notification
import time
import datetime
import webbrowser

class Course:
    def __init__(self, name, starttimes, link, status):
        self.name = name
        self.starttimes = starttimes
        self.link = link
        self.status = status


date, time_t = datetime.date.today(), datetime.datetime.now().time()
day = date.strftime("%A")
# day = "Monday"

print("Starting now")
# endtime = 0
with open("times.txt", 'r') as file:
    data = file.readlines()
    # for dt in data:
    #     stimes = dt.split("\n")[0].split("; ")[1].split(", ")
    #     for t in stimes:
    #         if day in t:
    #             ti = t.split("-")[1][:2]
    #             if int(ti) > endtime:
    #                 endtime = int(ti)
    #     print(stimes)
    # print(endtime)
    while time_t.hour <= 18:
        time_t = datetime.datetime.now().time()
        class_time = time_t.strftime("%X")
        # print(class_time)
        # day = "Friday"
        # class_time = "09:00:00"
        for dt in data:
            name, starttimes, link, status = (dt.split("\n")[0]).split("; ")
            course_tmp = Course(name=name, starttimes=starttimes, link=link, status=status)
            course_tmp.starttimes = course_tmp.starttimes.split(", ")
            course_tmp.link = course_tmp.link.split(", ")
            if course_tmp.status == "ACTIVE":
                for index, d in enumerate(course_tmp.starttimes):
                    if day in d and class_time in d:
                        print(f"{course_tmp.name}, {d}, {course_tmp.link[index % len(course_tmp.link)]}")
                        notification.notify(
                            title="CLASS Reminder",
                            message=f"You have {course_tmp.name} class now. Please join the class ASAP",
                            app_name="Reminder",
                            timeout=1
                        )
                        webbrowser.open(course_tmp.link[index % len(course_tmp.link)])
                        time.sleep(60*59 + 58)
                        # time.sleep(5)
                        # exit(0)
        time.sleep(0.5)
    print("Ending the process")


