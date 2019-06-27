import time

print("The epoch start time of this system is : " + time.strftime("%C", time.gmtime(0)))
print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0 :
    print("\t Day light savings is in effect for this location \n")
    print("\t The DST timezone is " + time.tzname[1])

print("The Local time is " + time.strftime("%Y - %m - %d %H:%M:%S", time.localtime()))
print("The UTC time is " + time.strftime("%Y - %m - %d %H:%M:%S", time.gmtime()))

