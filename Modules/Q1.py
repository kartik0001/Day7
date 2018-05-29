'''
Time Tuples= It is defined as the Time stores in Python is called Time Tuple as it is easy to understand for Python.

 These Many of Python's time functions handle time as a tuple of 9 numbers-

Index	Field	                Values
0	    4-digit year	        2008
1	    Month	                1 to 12
2	    Day	                    1 to 31
3	    Hour	                0 to 23
4	    Minute	                0 to 59
5	    Second	                0 to 61 (60 or 61 are leap-seconds)
6	    Day of Week	            0 to 6 (0 is Monday)
7	    Day of year	            1 to 366 (Julian day)
8	    Daylight savings	   -1, 0, 1, -1 means library determines DST


The above tuple is equivalent to struct_time structure. This structure has following attributes-

Index	Attributes	    Values
0	    tm_year	        2008
1	    tm_mon	        1 to 12
2	    tm_mday	        1 to 31
3	    tm_hour	        0 to 23
4	    tm_min	        0 to 59
5	    tm_sec	        0 to 61 (60 or 61 are leap-seconds)
6	    tm_wday	        0 to 6 (0 is Monday)
7	    tm_yday	        1 to 366 (Julian day)
8	    tm_isdst	    -1, 0, 1, -1 means library determines DST

'''

# Example:

import datetime
d = datetime.date(2012, 10, 18)
print(d.timetuple())
print("Tupple Is:",tuple(d.timetuple()))



'''
OUTPUT: 
time.struct_time(tm_year=2012, tm_mon=10, tm_mday=18, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=292, tm_isdst=-1)
Tupple Is: (2012, 10, 18, 0, 0, 0, 3, 292, -1)
'''