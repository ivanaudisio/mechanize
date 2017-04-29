import re
import time
from mechanize import Browser

tried=0
connected = False
while not connected:
    try:
        r = b.open('http://www.google.com/foobar')
        connected = true # if line above fails, this is never executed
    except:
        print "connection interrupted"
        time.sleep(30)
