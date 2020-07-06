from datetime import datetime
m2 = '1:07:07PM'
in_time = datetime.strptime(m2, "%I:%M:%S%p")
print(in_time)
m2 =  datetime.strftime(in_time, "%H:%M:%S")
print(m2)
