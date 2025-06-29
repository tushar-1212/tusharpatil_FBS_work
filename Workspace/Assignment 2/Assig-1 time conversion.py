#Convert the time entered in hh,min and sec into seconds.
hrs=int(input("Enter the time in hh: "))
mins=int(input("Enter the time in mm: "))
sec=int(input("Enter the time in ss: "))
total_seconds = (hrs * 3600) + (mins * 60) + sec
print("Total time in seconds:", total_seconds)
