import sys
import random
from time import sleep
import easybattle
import asciiart
import mediumbattle
import shops
import upgrade
import locations

#----This is the default player values
#player health is dealt in HP or hitpoints
MaxHP = 35
HP = 35
#player damage points
DP = 10
bonusDP = 0
specialuses = 10
#player strength points and exp points
STR = 0
EXP = 0
#sets flag for upgrade god introdialogue
ufirst = True
#player money, to buy potions and new weapons
money = 10
goal = "Magma Valley"
days = 20
#----This is a variable that tells the game if the player is in a fight or not.
fight = False
#----This is default enemy HP, DP and name.
enemyHP = 30
enemyDP = 10
enemyname = " "
#--money given for killing this enemy
moneyforkill = 10
#----This is the special melee attack variables. Its a magic sword that only has a certain amount of uses
special = 30
specialuses = 10
#----Potions are used to restore health to the player when they are in need
potions = 5
#----These set the players location
currentplace = "Shiverton Village"
#----This is a d6 roll, for random battles usually
roll = random.randrange(1, 7)
#def weapon types im thinking melees and guns - guns do more damage but need to have ammo and be reloaded every few turns
#----This is if they have melee weapons
happystickhave = False #weak melee weapon
swordhave = False #good melee
goldpanhave = False #best melee super rare

#----This is if they have any guns
rustyhave = False  #a rusty 6 shooter
sixshoothave = False  #regular 6 shooter
kissofdeathhave = False  #crazy good 6 shooter
#----This is variables for guns, should ammo types be considered?
clip = 0

#----This is where you can rename the weapon
weapon = "hand"
#All ascii graphics used to be here but are now stored in the ascii art file

#Enemy stats defined here, but can be changed based on battle you want.
enemyHP = 10
enemyattack = 2
enemysprite = " "
enemyattacksprite = " "


#How to use readx(x). Have it read out the text by placing a string in the ().
def readx(x):
	for char in x:  #For characters in your sentence
		sleep(0.05)  #Time inbetween each print. Good speed is 0.05
		sys.stdout.write(char)  #Writes
		sys.stdout.flush()  #Moves right to next


def youOwn(happystickhave, swordhave, goldpanhave):
	print "You have..."
	if (happystickhave):
		print "...The [happystick]..."
	if (swordhave):
		print "...A nice steel [sword]..."
	if (goldpanhave):
		print "...The lengendary [goldenpan]!?..."
	print "... and your bare [hands]."


def equip(weapon, happystickhave, swordhave, goldpanhave):
	print "--EQUIP--"
	print "You assess your inventory to equip the best weapon."
	youOwn(happystickhave, swordhave, goldpanhave)
	print "What do you want to equip?"
	equipThis = raw_input("Equip> ")
	if ((equipThis == "happystick") and (happystickhave)):
		weapon = "happystick"
	elif (equipThis == "sword") and (swordhave):
		weapon = "sword"
	elif (equipThis == "goldenpan") and (goldpanhave):
		weapon = "goldenpan"
	else:
		weapon = "hand"
	return weapon, happystickhave, swordhave, goldpanhave


def givehelp():
	print "--Help--"
	print "You can use [map] to show the surrounding area."
	print "You can use [potion] to restore some HP."
	print "You can use [walk] to walk for a day over to %s." % (goal)
	print "You can use [equip] to equip weapons found or bought"
	print "You can use [goods] to eat food and look at your inventory"
	print "You can use [stats] for you stats."
	print "--------------"
	print "Any questions?"
	questions = raw_input("> ")
	if questions == "yes":
		print "About what?"
		questions1 = raw_input("I have a question about> ")
		if questions1.lowercase() == "potion":
			print "Potion - using one of your potions, restores all your health. You can buy more potions at most shops."
		elif questions1.lowercase() == "shop":
			print "Shopping - Different in any town. To buy, type what you want, all lowercase. To leave, buy 1 thing or say 'goodbye.'"
		elif questions1.lowercase() == "walk":
			print "Walking - Walk towards the next objective. You may encounter an enemy on the road, so be careful!"
		elif questions1.lowercase() == "equip":
			print "Equiping - Equips the best weapon you have. There are 3. You must have every weapon before the others in order to equip the next best. For example, you must have the happystick before you can get the sword. And you must have both of those before you can get the secret weapon!"
		elif questions1.lowercase() == "goods":
			print "Goods - You can view and use items here. It tells you everything you have in your backpack. You always start with 1 banana and 100 dollars."
		elif questions1.lowercase() == "stats":
			print "Stats - Very simple, they just show your current health out of your maxium health, and how much damage or DP you do."
		elif questions1.lowercase() == "map":
			print "Map - See the current place you are in, and where you can travel from here."
		elif questions1.lowercase() == "travel":
			print "Travel - Allows you to travel to the available areas. You can see what is avaible by checking the map."
		else:
			print "Can't help you with that, did you mispell it?"
	elif questions == "no":
		print "Alright, good luck!"
	else:
		print "[yes] or [no] next time!"


def dpBonus(bonusDP):
	if (weapon == "happystick"):
		bonusDP = 5
	elif (weapon == "sword"):
		bonusDP = 25
	elif (weapon == "goldenpan"):
		bonusDP = 50
	else:
		bonusDP = 0
	return bonusDP
def showStats(bonusDP):
	print "Pulling out a mirror, you assess yourself."
	print "--STATS--"
	print "Your total EXP points: %s" % (EXP)
	print "HP as of now: %s" % (HP)
	print "Max HP: %s" % (MaxHP)
	print "DP w/o weapon bonus: %s" % (DP)
	bonusDP = dpBonus(bonusDP)
	print "DP w/ weapon bonus: %s" % (DP + bonusDP)
	print "STR points: %s" % (STR)
	print "Total gold coins: %s" % (money)

gamestart = True
print "You are the chosen hero of Teltactica!"
print "Travel the world, to ultimately destroy the evil wizard of Terror Castle."
while (gamestart and days != 0):
	action = raw_input("Action> ")
	if action == "equip":
		weapon, happystickhave, swordhave, goldpanhave = equip(
		    weapon, happystickhave, swordhave, goldpanhave)
	elif action == "help":
		givehelp()
	elif action == "stats":
		showStats(bonusDP)
	elif action == "walk":
		print "you walk to example castle"
		days = days - 1
		roll = random.randrange(1, 3)
		if roll == 2:
			print "A figure appears before you!"
			print "FIGHT!"
			bonusDP = dpBonus(bonusDP)
			fight, enemyHP, enemyattack, enemysprite, enemyattacksprite, enemyname, moneyforkill, HP,MaxHP, DP, bonusDP, specialuses, money, potions, EXP, earnEXP = easybattle.simplebattle(fight, 15, 5, enemysprite, enemyattacksprite, "n imp", 10, HP, MaxHP, DP, bonusDP, specialuses, money, potions, EXP, 20)
			print "You now have %sEXP, and now have %s gold!" % (EXP, money)
	elif action == "shop":
		print "A sign at a local shop catches your eye, and you enter."
		if currentplace == "Shiverton Village":
			print asciiart.happyshop
			sleep(1)
			money, happystickhave, swordhave = shops.happyStore(money, happystickhave, swordhave)
		else:
			print "Wha..? If you see this yell at Lucca."
	elif action == "potion":
		if (potions > 0):
			print "You grab a red vile out of your pocket."
			print "Uncorking the top, you take a swig from a potion"
			HP = MaxHP
			potions = potions - 1
			print "You have %sHP!" % (HP)
		else:
			print "You reach for the potion section in your bag to find none are there :c."
			print "Go buy some from a local [shop]!"
	elif action == "map":
		print "You pull out and assess you map."
		locations.printmap(currentplace)
	elif action == "travel":
		print "Would you [walk] there, or [pay] 100 gold to get there now?"
		travelanswer = raw_input("I would like to...> ")
		if travelanswer == "walk":
			locations.travelfoot()

	elif action == "upgrade":
		EXP, HP, maxHP, STR, money, ufirst = upgrade.upgradeGod(EXP, HP, MaxHP, STR, money, ufirst)
	else:
		print "Not an action I thought youd say!"
print "You have adventured all the way to Terror Castle! Now you face off THE DESERT WIZARD WARDOOM!"
#insert the final boss here
print "You defeated the FINAL BOSS!!!! Congradulations! If you'/d now like, you should write your own story by forking this code! If you do, I'/d love to see what you create."
