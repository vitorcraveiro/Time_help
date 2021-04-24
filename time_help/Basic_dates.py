# working with time in python 

import datetime as dt

current_date_all = dt.date.today()           #complete date
print(current_date_all)


#date class -> working with date
#time class -> working with time 
#datetime class -> working with both 

#printing a date 
datea = dt.date(2020, 2, 1)         #fist year , secund month, third day
print(datea)

#after instantiated the object

print("year: {}" .format(datea.year))
print("mount: {}" .format(datea.month))
print("day: {}".format(datea.day))
print("")

#printing a time
timea = dt.time(22,30,30,5555)         #fist hour , secund minutes , third secunds , fourth milliseconds
print(timea)

#after instantiated the object
print("hour: {}".format(timea.hour))
print("minute: {}".format(timea.minute))
print("secund: {}".format(timea.second))
print("microsecond: {}".format(timea.microsecond))
print("")

#printing a date time
date_time_a = dt.datetime(2002,11,28,23,55,59,40)         #year - month - day - hour - minutes - secunds - microsecond 
print(date_time_a)
print("")

#current_date_time 

current_date_time = dt.datetime.now()                # exactly the current time
print(current_date_time)