#!/bin/python3

import sys

def timeConversion(s):
    if not len(s) == 10:
        return "Bad input"
    hour = int(s[:2])
    minutes = int(s[3:5])
    seconds = int(s[6:8])
    period = s[8:10]
    if (1 <= hour <= 12) and (0 <= minutes <= 59) and (0 <= seconds <= 59):
        if period == "AM":
            if hour == 12:
                return "00:" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
            else:
                return str(hour).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
        elif period == "PM":
            if hour == 12:
                return str(hour).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
            else:
                return str(12 + hour).zfill(2) + ":" + str(minutes).zfill(2) + ":" +  str(seconds).zfill(2)
        else:
            return "Bad input"
    else:
        return "Bad input"


s = input().strip()
result = timeConversion(s)
print(result)
