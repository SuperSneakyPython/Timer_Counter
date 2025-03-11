"""
# script useage is as follows:
# starttime = time_start() -> get start time
# endtime = time_end() -> get end time
# option = options() -> option selected as s, m, h, or d to give time in seconds, minutes, hours, or days running. 
# no input is seconds by default.
# timeoutput = option(timecalculation(starttime=starttime, endtime=endtime)) -> calculates the output for printing. Little complicated though.
# Note to yourself, I'd like to simplify this program so the user only has to call timeoutput = timeoutput() but I'm not sure how!
"""

import time
import math as math

def time_start():
    starttime = float(time.time())
    return starttime
def time_end():
    endtime = float(time.time())
    return endtime

class timecalculation():
    options = {}
    def __init__(self, endtime, starttime):
        self.currenttime = float(endtime - starttime)
    #calculations below
    def Days(self):
        days = float(self.currenttime/60/60/60)
        daystrunc = str(math.trunc(days))
        print(daystrunc + ' days ')
    def Hours(self):
        hours = float(self.currenttime/60/60)
        hourstrunc = str(math.trunc(hours))
        print(hourstrunc + ' hours ')
    def Minutes(self):
        minutes = float(self.currenttime/60)
        minutestrunc = str(math.trunc(minutes))
        print(minutestrunc + ' minutes ')
    def Seconds(self):
        seconds = float(self.currenttime)
        secondstrunc = str(math.trunc(seconds))
        print(secondstrunc + ' seconds ')
    #throwing the above calculations into a dictionary for user recall as letters
    options = {
        "d" : Days,
        "h" : Hours,
        "m" : Minutes,
        "s" : Seconds,
    }
#recall the dictionary above as an option and default to displaying seconds if no input
def options(input=None):
    if input is not None:
        option = timecalculation.options.get(input)
    else:
        option = timecalculation.options.get('s')
    return option