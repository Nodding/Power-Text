from time import sleep
import sys

#How to use readx(x). Have it read out the text by placing a string in the ().
def readx(x):
	for char in x:  #For characters in your sentence
		sleep(0.05)  #Time inbetween each print. Good speed is 0.05
		sys.stdout.write(char)  #Writes
		sys.stdout.flush()  #Moves right to next
	print ("") #newline it looks nicer

#defines the actual stores
def happyStore(money, happystickhave, swordhave):
	print ("WELCOME TO THE HAPPY STORE :D\n")
	#anything in readx is printed like a type writer
	readx("Mr.Happy: Welcome to the happy store :D")
	readx("Mr.H: We have many goods :D")
	sleep(0.2)
	print ("[happystick]: 50 Gold")
	print ("[sword]: 300 Gold")
	sleep(1)
	readx("What would you like? c:")
	choice = input("I want to buy...> ")
	if choice.lower() == "happystick" and happystickhave == False and money >= 50:
		print ("You have recieved the happy stick!")
		happystickhave = True
		money = money - 50
	elif choice.lower() == "happystick" and happystickhave == False and money < 50:
		print ("You do not have enough :D")
	elif choice.lower() == "happystick" and happystickhave == True:
		print ("You already bought that! Make sure you [equip] it!")
	elif choice.lower() == "sword" and swordhave == False and money >= 300:
		print ("You have bought the sword!")
		swordhave = True
		money = money - 300
	elif choice.lower() == "sword" and swordhave == False and money < 300:
		print ("You do not have enough! :D")
	elif choice.lower() == "sword" and swordhave == True:
		print ("You already have the sword! Go [equip] it if you haven't!")
	else:
		print ("I didn't understand that :C")
	return money, happystickhave, swordhave

	#INFO can buy golden pan here but it is not obvious
def HotHotGoods(money, swordhave, goldenpanhave):
	print("WELCOME TO HOT HOT GOODS")
	readx("OH GOD ARE THESE DEALS SO HOT!")
	sleep(0.5)
	print("\033[1;31mTAKE ADVANTAGE OF THEM BEFORE THEY ALL BURN UP!\033[1;m")
	sleep(0.5)
	print ("[sword]: 300 Gold")
	sleep(1)
	choice = input("I want to buy...> ")
	if choice.lower() == "sword" and swordhave == False and money >= 300:
		print ("You have bought the sword!")
		swordhave = True
		money = money - 300
	elif choice.lower() == "sword" and swordhave == False and money < 300:
		print ("You do not have enough for the sword!")
	elif choice.lower() == "sword" and swordhave == True:
		print ("You already have the sword! Go [equip] it if you haven't!")
	elif choice.lower() == "goldenpan" and goldenpanhave == False and money >= 300:
		print ("You have bought the GOLDEN PAN!")
		goldenpanhave = True
		money = money - 1000
	elif choice.lower() == "goldenpan" and goldenpanhave == False and money < 300:
		print ("What? Goldenpan? Nope never heard of one of those...")
	elif choice.lower() == "goldenpan" and goldenpanhave == True:
		print ("You already have the GoldenPan don't rub  it in...")
	return money,swordhave,goldenpanhave