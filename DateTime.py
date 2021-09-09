import datetime
from datetime import timedelta

def currentDate():
    now=datetime.datetime.now
    #print("Date: ",now().date())
    return str(now().date())

def currentTime():
    now=datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())





