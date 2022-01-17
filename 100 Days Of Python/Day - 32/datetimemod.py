import datetime as dt
time = dt.datetime.now()
year = time.year
month = time.month
weekday = time.weekday()   # Computer Starts Counting from 0
hour = time.hour
# If not specified the default hour is 00:00:00
dob = dt.datetime(year=2020, month=12, day=4)
dob_update = dt.datetime(year=2020, month=12, day=4, hour=4)
print(time, year, month, weekday, hour, sep="\n")
