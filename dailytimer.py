from datetime import datetime
def dtimer(start_time_h, start_time_m, end_time_h, end_time_m):
	start_time = int(start_time_h)*60 + int(start_time_m)
	#print "start_time:", start_time
	end_time = int(end_time_h)*60 + int(end_time_m)
	#print "end_time:", end_time
	current_time =  datetime.now().hour*60 +datetime.now().minute
	#current_time = 23*60+14
	if (start_time <= end_time):
	    #print "opcja 1"
	    if start_time <= current_time and end_time >= current_time:
	        print "run"
	    else:
	        print "no run"
	else:
	    #print "opcja 2"
	    if (current_time < end_time):
	        #po polnocy - dodaje przedluzenie doby
	        current_time = current_time + 1440
	    end_time = end_time + 1440
	    #print "start_time:", start_time
	    #print "end_time:", end_time
	    #print "current_time:", current_time
	    if start_time <= current_time and end_time >= current_time:
	        print "run"
	    else:
	        print "no run"
	#start 22, end 15, current - 13 dodac
	#start 22, end 10, current 23 nie dodawac
