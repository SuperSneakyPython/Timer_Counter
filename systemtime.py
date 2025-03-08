import time
from pathlib import Path
import math as math

main_dir = Path(__file__).parent.absolute()
datadir = sprite_dir = main_dir.joinpath("starttimedata")

def uptime():
    #read time the computer booted as a float
    with open(datadir,'r') as file:
        starttime = float(file.read())

    #calcuate minutes/days etc. from float generated from time.time()
    currenttime = time.time() - starttime
    days = float(currenttime/60/60/60)
    hours = math.modf(days)[0]*24
    minutes = math.modf(hours)[0]*60
    seconds = math.modf(minutes)[0]*60
    
    #truncate it all to round it to the nearest integer
    daystrunc = str(math.trunc(days))
    hourstrunc = str(math.trunc(hours))
    minutestrunc = str(math.trunc(minutes))
    secondstrunc = str(math.trunc(seconds))
    print(daystrunc + ' days, ' + hourstrunc + ' hours, ' + minutestrunc + ' minutes, ' + secondstrunc + ' seconds uptime.')

if __name__ == '__main__':
    uptime()