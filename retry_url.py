import re
import time
from mechanize import Browser

max_retries=10
br = Browser()
br.set_handle_robots(False)
tried=0
connected = False

while not connected:
    try:
        response = br.open("http://cjoc:8080/job/shared-agent-01")
        connected = True # if line above fails, this is never executed
    except:
        print "connection could not be establish"
        time.sleep(5)
        tried += 1
    if tried > max_retries:
        exit()

print "URL active"
