Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import datetime
datetime.now()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    datetime.now()
AttributeError: module 'datetime' has no attribute 'now'
>>> datetime.datetime.now()
datetime.datetime(2023, 1, 31, 21, 42, 56, 244210)
>>> obj=datetime.datetime.now()
>>> obj
datetime.datetime(2023, 1, 31, 21, 43, 35, 576979)
>>> print(obj)
2023-01-31 21:43:35.576979
>>> from datetime import date
>>> today=date.today()
>>> print(today)
2023-01-31
>>> today
datetime.date(2023, 1, 31)
>>> print(today.year,today.month,today.day)
2023 1 31
>>> from datetime import datetime
>>> from datetime import *
>>> now = datetime.now()
>>> now
datetime.datetime(2023, 1, 31, 21, 45, 39, 978830)
>>> print(now)
2023-01-31 21:45:39.978830
>>> current_time = now.strftime("%H:%M:%S") #strftime - time in string format
>>> current_time
'21:45:39'
>>> print(current_time)
21:45:39
>>> import time
>>> t=time.localtime()
>>> t
time.struct_time(tm_year=2023, tm_mon=1, tm_mday=31, tm_hour=21, tm_min=46, tm_sec=44, tm_wday=1, tm_yday=31, tm_isdst=0)
>>> print(t)
time.struct_time(tm_year=2023, tm_mon=1, tm_mday=31, tm_hour=21, tm_min=46, tm_sec=44, tm_wday=1, tm_yday=31, tm_isdst=0)
>>> current_time=time.strftime("%H:%M:%S",t)
>>> current_time
'21:46:44'
