# !/usr/bin/python
'''
A simple script to output interesting Raspberry Pi 3 (Linux) 
system information values. For testing purposes only and 
not intended for production uses, as it may go wrong.
Tested with Python 2.4+ on Raspbian Stretch.
GitHub: /kongrawd (On Dec 22, 2018) 
'''
import subprocess

def show_mem():
    # Show details about your memory
    out = subprocess.Popen(['cat', '/proc/meminfo'], 
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    return  s

def measure_temp():
        # Shows the temperature of the CPU in Celcius
        out = subprocess.Popen(['/opt/vc/bin/vcgencmd', 'measure_temp'], 
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        return (stdout.replace("temp=","")) if not stderr else 'Error'


print(measure_temp())