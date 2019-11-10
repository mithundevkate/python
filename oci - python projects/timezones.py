import pytz
import datetime

x = pytz.all_timezones

x1 = open("C:\\Users\\mdevkate\\Desktop\\time.txt", 'w+')
counter = 0
for i in x:
    tz = pytz.timezone(i)
    curtime = datetime.datetime.now(tz=tz).strftime("%H:%M:%S")
    print("Time zone is --> %s \t\t and Current time is %s \n" % (i, curtime))
    x1.write("Time zone is --> %s \t\t and Current time is --> %s \n" % (i, curtime))
    counter = counter + 1
    if counter == 40:
        break

x1.close()
