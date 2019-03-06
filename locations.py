#imports
from time import sleep
import sys
import asciiart
#How to use readx(x). Have it read out the text by placing a string in the ().
def readx(x):
	for char in x:  #For characters in your sentence
		sleep(0.05)  #Time inbetween each print. Good speed is 0.05
		sys.stdout.write(char)  #Writes
		sys.stdout.flush()  #Moves right to next
	print "" #newline it looks nicer

#inital available locations
availablelocation1 = "Allerteration Admin Alley"
availablelocation2 = "Allerteration Admin Alley"
availablelocation3 = "Allerteration Admin Alley"
availablelocation4 = "Allerteration Admin Alley"
availablelocation5 = "Allerteration Admin Alley"

#All locations
location0 = "Allerteration Admin Alley"
location1 = "Shiverton Village"
location2 = "Magma Lane"
location3 = "Vile Valley"
location4 = "Greentree Grove"
location5 = "Terror Castle"
def availablelocations(availablelocation1, availablelocation2, availablelocation3, availablelocation4, availablelocation5):
	if currentplace == "Shiverton Village":
		availablelocation1 = "Magma Lane"
		availablelocation2 = "Allerteration Admin Alley"
		availablelocation3 = "Allerteration Admin Alley"
	elif currentplace == "Magma Lane":
		availablelocation1 = "Shiverton Village"
		availablelocation2 = "Vile Valley"
		availablelocation3 = "Greentree Grove"
		availablelocation4 = "Allerteration Admin Alley"
	else:
		availablelocation1 = "Allerteration Admin Alley"
		availablelocation2 = "Allerteration Admin Alley"
		availablelocation3 = "Allerteration Admin Alley"
		availablelocation4 = "Allerteration Admin Alley"
		availablelocation5 = "Allerteration Admin Alley"
	return availablelocation1, availablelocation2, availablelocation3, availablelocation4, availablelocation5
def checktravel(place):
	print "Ah yes, you want to go to %s..." % (place)
	if (place != availablelocation1 or place != availablelocation2 or place != availablelocation3 or place != availablelocation4 or place != availablelocation5):
		print "That isn't in my reach to walk! I should check my [map]"

def printmap(currentplace):
	if currentplace == "Shiverton Village":
		print asciiart.map1
	elif currentplace == "Magma Lane":
		print asciiart.map2
	else:
		print asciiart.mapCommands
def travelhorse():
	print "A man in a horse and buggy pulls up beside you, and asks where you would like to go."
	sleep(0.5)
	print "You tell the man..."
	traveldesination = raw_input("Desintation> ")
def travelfoot():
	print "Where will you head now?"
	heading = raw_input()
	if heading.upper() == "SHIVERTON VILLAGE":
		print "You set a goal to walk to Shiverton Village by foot."
def placesdiscover():
	print "You have discovered %s!" % (area)
	print ""
