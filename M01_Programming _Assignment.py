seconds_per_minute = 60
minutes_per_hour = 60
print("seconds_per_minute = ", seconds_per_minute)
print("minutes_per_hour = ", minutes_per_hour)

seconds_per_hour = seconds_per_minute * minutes_per_hour
print("seconds_per_hour = ", seconds_per_hour)

seconds_per_day = seconds_per_hour * 24
print("seconds_per_day = ", seconds_per_day)

x = seconds_per_day / seconds_per_hour
print("x = ", x)

y = seconds_per_day // seconds_per_hour
print("y = ", y)