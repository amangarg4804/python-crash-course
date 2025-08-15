def convert_seconds(seconds):
    hours = seconds // 3600 ## // is Floor division: Division that rounds down to the nearest int
    minutes = (seconds - hours * 3600) // 60 # how many minutes ? hours * 3600 means number of seconds consumed by hour part
    remaining_seconds = seconds - hours * 3600 - minutes * 60 # minutes * 60 = number of seconds consumed by minutes
    return hours, minutes, remaining_seconds
 
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)