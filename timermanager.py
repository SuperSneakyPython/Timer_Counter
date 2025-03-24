import time
import math as math
<<<<<<< HEAD

=======
>>>>>>> d717caf6d4d987ceaaabac84ca56d0670639d0a3
"""
# script useage is as follows:
# starttime = time_start() -> get start time
# endtime = time_end() -> get end time
# time_calc -> option selected as s, m, h, or d to give time in seconds, minutes, hours, or days running. 
# no input is seconds by default.
# timeoutput = option(timecalculation(starttime=starttime, endtime=endtime)) -> calculates the output for printing. Little complicated though.
# Note to yourself, I'd like to simplify this program so the user only has to call timeoutput = timeoutput() but I'm not sure how!
"""
<<<<<<< HEAD
=======
runtime = 0 #initalise variable
>>>>>>> d717caf6d4d987ceaaabac84ca56d0670639d0a3

def time_start() -> float:
    starttime = time.time()
    return starttime

def time_end() -> float:
    endtime = time.time()
    return endtime

class calculation():
    """
    Returns runtime as a (float, string) in days, hours, minutes, or seconds
    """
    def __init__(self, runtime):
        self.runtime = runtime

    def Days(self) -> tuple[float, str]:
        days = self.runtime/60/60/60 
        daystrunc = math.trunc(days)
        daystrunc_string = str(daystrunc) + ' days '
        return days, daystrunc_string

    def Hours(self) -> tuple[float, str]:
        hours = float(self.runtime/60/60)
        hourstrunc = math.trunc(hours)
        hourstrunc_string = str(hourstrunc) + ' hours '
        return hours, hourstrunc_string

    def Minutes(self) -> tuple[float, str]:
        minutes = float(self.runtime/60)
        minutestrunc = math.trunc(minutes)
        minutestrunc_string = str(minutestrunc) + ' minutes '
        return minutes, minutestrunc_string

    def Seconds(self) -> tuple[float, str]:
        seconds = float(self.runtime)
        secondstrunc = math.trunc(seconds)
        secondstrunc_string = str(secondstrunc) + ' seconds '
        return seconds, secondstrunc_string
    
def time_calc(start_time, end_time, option=None, text=True) -> float or str:
    """
    Performs main calc. Uses two input times, an option as string from dictionary below.
    Text=False will give a float instead of a string
    start_time and end_time are required but defaults are:
        option = seconds by default (display seconds)
        text = True by default (display string)
    """
    runtime = end_time - start_time
    cal = calculation(runtime=runtime)
    #key assigned to functions from calculation class
    options = {
    "d" : cal.Days,
    "h" : cal.Hours,
    "m" : cal.Minutes,
    "s" : cal.Seconds,
    }
    #tuple 1=string, 0=float output
    if text == True:
        index = 1
    else:
        index = 0
    #if user gives key, find function in options dict or use seconds by default.
    if option is not None:
        selected_option = options.get(option)
    else:
        selected_option = options.get('s')
    return selected_option()[index]