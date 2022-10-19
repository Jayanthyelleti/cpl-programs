# Python program that prompts the user to enter a time in seconds and outputs the entered time as days, hours, minutes and seconds.
#Jayanth Adithya Yelleti(jay26@njit.edu)
time = float(input("Enter time in seconds: "))
print()
print("%d seconds is:\n" % (time))
day=time//(24*3600)
time= time%(24*3600)
hour= time//3600
time %=3600
minutes=time//60
time %=60
seconds=time
print("%d days" % (day))
print("%d hours" % (hour))
print("%d minutes" % (minutes))
print("%d seconds" % ( seconds))
