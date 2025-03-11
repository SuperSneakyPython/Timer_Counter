import time
from pathlib import Path

#Saves the current time when the script is run. Put in a startup script for Linux/windows
main_dir = Path(__file__).parent.absolute()
datadir = sprite_dir = main_dir.joinpath("starttimedata")
Time = time.time()

with open(datadir,'w') as file:
    file.write(str(Time))