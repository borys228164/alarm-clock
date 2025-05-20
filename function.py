import datetime as timr
from zoneinfo import ZoneInfo


def alarm_clock(hour, minute, second):
    now = timr.datetime.now(ZoneInfo("Europe/Kyiv"))
    just_time = timr.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
    rise_time = timr.timedelta(hours=hour, minutes=minute, seconds=second)
    cycle = timr.timedelta(hours=1, minutes=30, seconds=0)
    time_sleep = rise_time - just_time
    remainder = time_sleep % cycle
    result_alarm = (rise_time - remainder) + timr.timedelta(hours= 0, minutes= 15, seconds=0)
    return result_alarm



def time_now():
    now = timr.datetime.now(ZoneInfo("Europe/Kyiv"))
    just_tim = now.time().replace(microsecond=0)
    return just_tim



def time_to_sleep(time):
    now = timr.datetime.now(ZoneInfo("Europe/Kyiv"))
    just_time = timr.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
    wakeup_time = time
    result = (wakeup_time - just_time)
    if wakeup_time < just_time:
        wakeup1 = result + timr.timedelta(days=1)
        return wakeup1

    else:
        return result






