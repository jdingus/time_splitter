from datetime import timedelta, date, time, datetime

def main():
	start = datetime(2009, 6, 14, 21, 0, 0)
	stop = datetime(2009, 6, 14, 23, 0, 0) 
	time_split_hour(start,stop)


def time_split_hour(start,stop):
	""" Using a start and stop time return a list of allotted time by hour """

	TH_bg = start.replace(minute = 0, second = 0, microsecond = 0)
	# TH_end = stop
	# TH_end -= timedelta(minutes = stop.minute, seconds = stop.second, microseconds =  stop.microsecond)

	TH_end = stop - timedelta(minutes = stop.minute, seconds = stop.second, microseconds =  stop.microsecond)
	print 'TH_bg=',TH_bg
	print 'TH_end=',TH_end
	pass

def split_by_hour(start,stop):
	""" Using a START and STOP time return a list of hours with all of the time
	bucketed by hour """
	hour_list = return_hour_list(start,stop) # creates interval of every 1 hour based on start/stop
	ListEvents = [] # list used to store all the events which are by hour
	print "Hour List",hour_list

	for item in hour_list:
		temp_dict = {}
		# ev_bucket = item.strftime('%m/%d/%y %H:%M:%S')  #Format '06/14/09 19:00:00'
		TP_bg = item 
		TP_end = item + timedelta(hours=1)
		TH_bg = hour_list[0]
		TH_end = hour_list[-1]
		
		if TH_bg == TH_end:
			print "This is a completely closed case, must be single entry within same hour!"
			ev_dur = convert_timedelta(stop - start) # returns value in seconds
			temp_dict[TP_bg] = ev_dur # Store this single entry into dict, ONLY one so we are DONE
			ListEvents.append(temp_dict)
			return ListEvents

		if TH_bg == TH_end:
			print "This is a completely closed case, must be single entry within same hour!"
			ev_dur = convert_timedelta(stop - start) # returns value in seconds
			temp_dict[TP_bg] = ev_dur # Store this single entry into dict, ONLY one so we are DONE
			ListEvents.append(temp_dict)
			return ListEvents

def return_hour_list(start,stop):
	""" Returns a list of hours to check for when given a start and stop time """
			
	""" return INT_HB and INT_HE base on start and stop time  """
	INT_HB = start.replace(minute = 0, second = 0, microsecond = 0)
	# INT_HB -= timedelta(minutes = start.minute, seconds	= start.second, microseconds = start.microsecond)
	# print "INT_HB",INT_HB

	INT_HE = stop
	INT_HE -= timedelta(minutes = stop.minute, seconds = stop.second, microseconds =  stop.microsecond)
	# print "INT_HE",INT_HE

	""" Create a list of hours to check for time """
	hour_list = list(rrule(HOURLY, interval=1, dtstart = INT_HB, until = INT_HE))
	
	# print hour_list
	return hour_list

if __name__ == "__main__":   
	main()