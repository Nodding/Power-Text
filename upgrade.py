from time import sleep
import sys

#How to use readx(x). Have it read out the text by placing a string in the ().
def readx(x):
	for char in x:  #For characters in your sentence
		sleep(0.05)  #Time inbetween each print. Good speed is 0.05
		sys.stdout.write(char)  #Writes
		sys.stdout.flush()  #Moves right to next
	print ("") #new line after the text has finished

#defines the upgrade
def upgradeGod(EXP, HP, maxHP, STR, money, ufirst):
	readx("You clasp your hands and pray up to the Gods.")
	sleep(1)
	if(ufirst): readx("You hear a whisper from above.")
	if(ufirst): sleep(0.5)
	if(ufirst): readx("Upgrade God: Hey there warrior it is me, God. No not that one, the other one. The upgrade one!\n")
	if(ufirst): sleep(0.5)
	print ("You have " + str((EXP/100)*1) + " points to spend on upgrading yourself, since you have " + EXP + " EXP!\n")
	if(ufirst): sleep(3)
	if(ufirst): readx("UG: So, what do you want me to enhance? If you forgot, just pray the words [help] back.\n")
	ufirst = False
	prayer = input("I pray to you, Upgrade God...")
	if prayer == "help":
		readx("UG: You can upgrade your [HP] or [STR].")
		sleep(0.5)
		readx("UG: If you are really greedy, you can even sell all of your EXP to me for a 1:1 ratio of [gold]!")
		sleep(0.5)
	elif (prayer == "HP"):
		if EXP >= 100:
			readx("UG: Ah [HP]! I'll add another semi-useless organ to your body!\n")
			maxHP = maxHP + 5
			HP = maxHP
			EXP = EXP - 100
			print ("You now have a maxium of " + maxHP +  "HP!")
			readx("UG: Good for you!")
		else:
			print ("UG: You don't have enough EXP!")
	elif (prayer == "STR"):
		if EXP >= 100:
			readx("UG: [STR]! I'll add more muscle tissue to your body!")
			STR = STR + 1
			EXP = EXP - 100
			print ("You now have " + str(STR) + " STR!")
			readx("UG: Hooray!")
		else:
			print ("UG: You don't have enough EXP!")
	elif (prayer == "gold"):
		if (EXP > 1):
			readx("UG: [gold?] Ok, let me just grab that green visor you see most mob boss accountants use andddddd...")
			sleep(1)
			money += EXP*1
			EXP = 0
			print ("Cha-ching! You have " + str(money) + " gold!")
			sleep(1)
			readx("UG: Look at you Mr.Money-Bags!")
		else:
			print ("UG: Hey! You need at least 1 EXP to exchange for gold!")
	else:
		print ("UG: I didn't understand that... I think you are praying to the wrong God.")

	return EXP, HP, maxHP, STR, money, ufirst
