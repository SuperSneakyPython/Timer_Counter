import timermanager as tm
import time

"""
Example for how to use calc.
"""

start = tm.time_start()
#code starts here
time.sleep(1)
#code ends here
end = tm.time_end()
cal = tm.time_calc(start, end)
print(cal)