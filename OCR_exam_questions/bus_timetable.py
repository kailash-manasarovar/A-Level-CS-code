# Practice Papers Set 2 Paper 1 Q4
times = {
    "StopA":["06:55","07:25","07:55","08:55","09:55","11:55","14:00","15:00","15:30","16:00"],
    "StopB":["06:40","07:40","08:40","09:20","09:40","14:00","15:00","16:00","16:30"]
}

print(times["StopB"][4])

def time_value(time):
    strip_time = time.replace(":","")
    return int(strip_time)


print(time_value(times["StopB"][4]))


def next_bus(stop_name, current_time):
    count = 0
    times_left = True
    times_list = times[stop_name]
    while times_left == True and time_value(times_list[count]) < current_time:
        count = count + 1
        if count == len(times_list):
            times_left = False
            return "No buses"
    if times_left == True:
        return times_list[count]


print(next_bus("StopA", 2013))
