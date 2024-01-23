# 3.1 How many seconds are in an hour?
seconds_in_minute = 60
minutes_in_hour = 60
seconds_per_hour = seconds_in_minute * minutes_in_hour

# 3.3 How many seconds are in a day?
seconds_per_day = seconds_per_hour * 24

# 3.5 Divide seconds_per_day by seconds_per_hour using floating-point division.
floating_point_result = seconds_per_day / seconds_per_hour

# 3.6 Divide seconds_per_day by seconds_per_hour using integer division.
integer_result = seconds_per_day // seconds_per_hour

#3.6 Question

# Print the results
print(f"3.1 Seconds in an hour: {seconds_per_hour}")
print(f"3.3 Seconds in a day: {seconds_per_day}")
print(f"3.5 Floating-point division result: {floating_point_result}")
print(f"3.6 Integer division result: {integer_result}")
print(f"{floating_point_result} is different from {integer_result} so they are different even though they are the same number.")