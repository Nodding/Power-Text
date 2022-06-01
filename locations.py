#imports
from time import sleep
import sys
import asciiart
#How to use readx(x). Have it read out the text by placing a string in the ().
def readx(x):
	for char in x:  #For characters in your sentence
		sleep(0.03)  #Time inbetween each print. Good speed is 0.05
		sys.stdout.write(char)  #Writes
		sys.stdout.flush()  #Moves right to next
	print ("") #newline it looks nicer

#the variables were getting very long. So AL# means availablelocation number whatever. k# means knowing that number of location.

#All locations
location0 = "Allerteration Admin Alley"
k0 = False
location1 = "Shiverton Village"
k1 = False
location2 = "Magma Lane"
k2 = False
location3 = "Vile Valley"
k3 = False
location4 = "Greentree Grove"
k4 = False
location5 = "Terror Castle"
k5 = False

#initating variables
al1 = ""
al2 = ""
al3 = ""
al4 = ""
al5 = ""

def availablelocations(curpla, al1, al2, al3, al4, al5):
	# INFO Shiverton > Magma Magma > Greentree or Vile Greentree > Vile or Magma Vile > Greentree or Terror Terror > Vile
	if curpla == "Shiverton Village":
		al1 = "Magma Lane"
		al2 = "Allerteration Admin Alley"
		al3 = "Allerteration Admin Alley"
		al4 = "Allerteration Admin Alley"
		al5 = "Allerteration Admin Alley"
	elif curpla == "Magma Lane":
		al1 = "Shiverton Village"
		al2 = "Vile Valley"
		al3 = "Greentree Grove"
		al4 = "Allerteration Admin Alley"
		al5 = "Allerteration Admin Alley"
	elif curpla == "Greentree Groove":
		al1 = "Magma Lane"
		al2 = "Vile Valley"
		al3 = "Allerteration Admin Alley"
		al4 = "Allerteration Admin Alley"
		al5 = "Allerteration Admin Alley"
	elif curpla == "Vile Valley":
		al1 = "Greentree Grove"
		al2 = "Terror Castle"
		al3 = "Allerteration Admin Alley"
		al4 = "Allerteration Admin Alley"
		al5 = "Allerteration Admin Alley"
	elif curpla == "Terror Castle":
		al1 = "Vile Valley"
		al2 = "Allerteration Admin Alley"
		al3 = "Allerteration Admin Alley"
		al4 = "Allerteration Admin Alley"
		al5 = "Allerteration Admin Alley"
	
	else:
		al1 = "Allerteration Admin Alley"
		al2 = "Allerteration Admin Alley"
		al3 = "Allerteration Admin Alley"
		al4 = "Allerteration Admin Alley"
		al5 = "Allerteration Admin Alley"
	return curpla, al1, al2, al3, al4, al5

def printmap(curpla):
	if curpla == "Shiverton Village":
		print (asciiart.map1)
	elif curpla == "Magma Lane":
		print (asciiart.map2)
	else:
		print (asciiart.mapCommands)

def placesdiscover(curpla, k0, k1, k2, k3, k4, k5):
	if curpla == "Shiverton Village" and k1 == False:
		readx("You awake in Shiverton Village. Its cold climate sends shivers down your spine, but you shake it off, knowing you must push through here to get to the castle.")
		k1 = True
	if curpla == "Magma Lane" and k2 == False:
		readx("You arrive in Magma Lane. The blistering heat almost overwhelms you. You power through on your mission to the castle.")
		k2 = True
	if curpla == "Vile Vallet" and k3 == False:
		readx("You step foot in Vile Valley. An overwhelming vile fog clouds a lot of your view.")
	if curpla == "Greentree Grove" and k4 == False:
		readx("You make it to Green Grove. Dense jungles surround you.")
	if curpla == "Terror Castle" and k5 == False:
		readx("You finally arrive at Terror Castle. Screaming is heard from the top of the tower!")
	return curpla, k0, k1, k2, k3, k4, k5
def printLocations(curpla):
		print (al1, al2, al3, al4, al5)
		print (curpla)
def traveltime(curpla):
	#initating variables
	al1 = ""
	al2 = ""
	al3 = ""
	al4 = ""
	al5 = ""

	print ("Where would you like to go?")
	curpla, al1, al2, al3, al4, al5 = availablelocations(curpla, al1, al2, al3, al4, al5)
	#printLocations(curpla)
	wanttogo = input("Travel to> ")
	if wanttogo == al1 or wanttogo == al2 or wanttogo == al3 or wanttogo == al4 or wanttogo == al5:
		print ("You turn towards your new goal.")
		return wanttogo
	else:
		print ("That is not in range. Check your [map]!")
		return "[You have no goal, use [travel] to set it!]"
