def Time_Conversion(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    formatted_time = f"{hours_str}:{minutes_str}:{seconds_str}"

    return formatted_time

print(Time_Conversion(5025))
print(Time_Conversion(61201))
print(Time_Conversion(87000))