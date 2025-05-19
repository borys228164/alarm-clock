import datetime as timr


def alarm_clock(hour, minute, second):
    now = timr.datetime.now()
    just_time = timr.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
    rise_time = timr.timedelta(hours=hour, minutes=minute, seconds=second)
    cycle = timr.timedelta(hours=1, minutes=30, seconds=0)
    time_sleep = rise_time - just_time
    remainder = time_sleep % cycle
    result_alarm = (rise_time - remainder) + timr.timedelta(hours= 0, minutes= 15, seconds=0)
    return result_alarm



def time_now():
    now = timr.datetime.now()
    just_tim = now.time().replace(microsecond=0)
    return just_tim



result = alarm_clock(17, 0, 0)
print(result)
