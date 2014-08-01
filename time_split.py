from datetime import timedelta, date, time, datetime
from dateutil.rrule import *

def main():
    start = datetime(2009, 6, 14, 4, 0, 0)
    stop = datetime(2009, 6, 14, 4, 1, 10) 

    time_list=time_split(start,stop,1)
    print time_list

def round_down_minute(time_,minute_interval):
    """ Pass in datetime and round down to nearest minute interval """
    time_ = time_ - timedelta(minutes=time_.minute % minute_interval,
                     seconds=time_.second,
                     microseconds=time_.microsecond)
    return time_

def time_by_minute(start,stop,minute_interval):
    """ start and stop time passed in and return list of times in 
    period encompasing start and stop times at given minute interval """
    tpb = round_down_minute(start,minute_interval)
    tpe = round_down_minute(stop,minute_interval) + \
        timedelta(minutes=minute_interval)
    
    minute_list = list(rrule(MINUTELY, interval=minute_interval, \
        dtstart = tpb, until = tpe))
    return minute_list

def time_split(start,stop,minute_interval):
    """ Using a start and stop time return a list of allotted time by hour """
    minute_list = time_by_minute(start,stop,minute_interval)
        
    time_list = []

    i=0
    for item in minute_list:
        i=i+1
        tint_bg = item
        tint_end = tint_bg + timedelta(minutes=minute_interval)
        """ First loop different than rest """
        temp_dict={}

        if stop < tint_bg:
            continue
            # return time_list

        if i==1: 
            if stop <= tint_end:    #A            # In this case only one hour
                duration = stop - start
                temp_dict[tint_bg] = duration
                time_list.append(temp_dict)

            if stop > tint_end:     #B
                duration = tint_end - start
                temp_dict[(tint_bg)] = duration
                time_list.append(temp_dict)

        else:
            if stop <= tint_end:     #C
                duration = stop - tint_bg
                temp_dict[(tint_bg)] = duration
                time_list.append(temp_dict)

            if stop > tint_end:      #D
                duration = tint_end - tint_bg
                temp_dict[tint_bg] = duration
                time_list.append(temp_dict)

    """ Remove 0 timedelta entries and empty dicts """
    for dict in time_list:
        for k, v in dict.items():
            if v.total_seconds() == 0:
                dict.pop(k)
    time_list = [x for x in time_list if x]
    return time_list

if __name__ == "__main__":   
    main()