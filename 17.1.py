class Time(object):
    def time_to_int(self):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

time = Time()
time.hour = 2
time.minute = 24
time.second = 56

print time.time_to_int()
