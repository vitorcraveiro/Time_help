import datetime as dt 

# difference between to times

current_time = dt.datetime.now()
next_year = dt.datetime(2022, 1 , 1, 0, 0,0, 1)


remaining_time = next_year - current_time
print(remaining_time)
#class 
print(type(remaining_time))