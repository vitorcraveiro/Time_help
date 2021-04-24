import datatime as dt

current_time = dt.datetime.now()

#transforming_date_style 

#datetime to strings 
string_date = current_time.strftime("%Z, %B %d , %Y ") #name_week_day , month and number , year 
print(string_date)

print('''  strtime         
                 
            %a	Abbreviated weekday name.
            %A	Full weekday name.
            %w	Weekday as a decimal number.
            %d	Day of the month as a zero-padded decimal.
            %-d	Day of the month as a decimal number.
            %b	Abbreviated month name.
            %B	Full month name.
            %m	Month as a zero-padded decimal number.
            %-m	Month as a decimal number.
            %y	Year without century as a zero-padded decimal number.
            %-y	Year without century as a decimal number.
            %Y	Year with century as a decimal number.
            %H	Hour (24-hour clock) as a zero-padded decimal number.
            %H	Hour (24-hour clock) as a zero-padded decimal number.
            %I	Hour (12-hour clock) as a zero-padded decimal number.
            %-I	Hour (12-hour clock) as a decimal number.
            %p	Locale’s AM or PM.
            %M	Minute as a zero-padded decimal number.
            %-M	Minute as a decimal number.
            %S	Second as a zero-padded decimal number.
            %-S	Second as a decimal number.
            %f	Microsecond as a decimal number, zero-padded on the left.
            %z	UTC offset in the form +HHMM or -HHMM.
            %Z	Time zone name.
            %j	Day of the year as a zero-padded decimal number.
            %-j	Day of the year as a decimal number.
            %U	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.
            %W	Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.
            %c	Locale’s appropriate date and time representation.
            %x	Locale’s appropriate date representation.
            %X	Locale’s appropriate time representation.              ''')
            
#transforming_date_style

#strings to datetime 

date_string = "10 April, 2022"

date_object = dt.datetime.strptime(date_string, "%d %B, %Y")
print(date_object)



 