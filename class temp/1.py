import time

a = time.time()
loc = time.localtime()
print type(loc),loc.tm_year,loc.tm_mon,loc.tm_mday,loc.tm_wday
print a