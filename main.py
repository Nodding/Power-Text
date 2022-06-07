import sys
import random
from time import sleep
import battle
import asciiart
import shops
import upgrade
import locations

#----This is the default player values
#player health is dealt in HP or hitpoints
maxHP = 35
HP = 35
#player damage points
DP = 10
bonusDP = 0
specialuses = 3
#player strength points and exp points
STR = 0
EXP = 0

#player money, to buy potions and new weapons
money = 10
goal = "[You have no goal, use [travel] to set it!]"
days = 10
#----This is default enemy HP, DP and name.
enemyHP = 30
enemyDP = 10
enemyname = "Baddie"
#--money given for killing this enemy
moneyforkill = 10
#----This is the special melee attack variables. Its a magic sword that only has a certain amount of uses
special = 30
specialuses = 10
#----Potions are used to restore health to the player when they are in need
potions = 5
#----These set the players location
currentplace = "Shiverton Village"
#----places they have discovered
k0 = False
k1 = False
k2 = False
k3 = False
k4 = False
k5 = False
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
		sleep(0.03)  #Time inbetween each print. Good speed is 0.05
		sys.stdout.write(char)  #Writes
		sys.stdout.flush()  #Moves right to next


def youOwn(happystickhave, swordhave, goldpanhave):
	print ("You have...")
	if (happystickhave):
		print ("...The [happystick]...")
	if (swordhave):
		print ("...A nice steel [sword]...")
	if (goldpanhave):
		print ("...The lengendary [goldenpan]!?...")
	print ("... and your bare [hands].")


def equip(weapon, happystickhave, swordhave, goldpanhave):
	print ("--EQUIP--")
	print ("You assess your inventory to equip the best weapon.")
	youOwn(happystickhave, swordhave, goldpanhave)
	print ("What do you want to equip?")
	equipThis = input("Equip> ")
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
	print ("--Help--")
	print ("You can use [map] to show the surrounding area, including places to walk to.")
	print ("You can use [travel] to set the place you will walk to.")
	print ("You can use [potion] to restore some HP.")
	print ("You can use [walk] to walk for a day over to " + goal + ".")
	print ("You can use [equip] to equip weapons found or bought")
	print ("You can use [goods] to eat food and look at your inventory")
	print ("You can use [stats] for you stats.")
	print ("You can use [upgrade] to increase stats with enough EXP")
	print ("--------------")
	print ("Any questions? Use [yes] or [no].")
	questions = input("> ")
	if questions.lower() == "yes":
		print ("About what?")
		questions1 = input("I have a question about> ")
		if questions1.lower() == "potion":
			print ("Potion - using one of your potions, restores all your health. You can buy more potions at most shops.")
		elif questions1.lower() == "shop":
			print ("Shopping - Different in any town. To buy, type what you want, all lower. To leave, buy 1 thing or say 'goodbye.'")
		elif questions1.lower() == "walk":
			print ("Walking - Walk towards the next objective. You may encounter an enemy on the road, so be careful!")
		elif questions1.lower() == "equip":
			print ("Equiping - Equips the best weapon you have. There are 3. You must have every weapon before the others in order to equip the next best. For example, you must have the happystick before you can get the sword.")
		elif questions1.lower() == "goods":
			print ("Goods - You can view and use items here. It tells you everything you have in your backpack. You always start with 1 banana and 100 dollars.")
		elif questions1.lower() == "stats":
			print ("Stats - Very simple, they just show your current health out of your maxium health, and how much damage or DP you do.")
		elif questions1.lower() == "map":
			print ("Map - See the current place you are in, and where you can travel from here.")
		elif questions1.lower() == "travel":
			print ("Travel - Allows you to travel to the available areas. You can see what is avaible by checking the [map].")
		elif questions1.lower() == "upgrade":
			print ("Upgrade - Pray to the upgrade god. You can then choose [HP] , [STR] or [GOLD] to spend EXP on.")
		else:
			print ("Can't help you with that, did you mispell it?")
	elif questions == "no":
		print ("Alright, good luck!")
	else:
		print ("You were supposed to use [yes] or [no]!")


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
	print ("Pulling out a mirror, you assess yourself.")
	print ("--STATS--")
	print ("Your total EXP points: " + str(EXP))
	print ("HP as of now: " + str(HP))
	print ("Max HP: " + str(maxHP))
	print ("DP w/o weapon bonus: " + str(DP))
	bonusDP = dpBonus(bonusDP)
	print ("DP w/ weapon bonus: " + str(DP + bonusDP))
	print ("STR points: " + str(STR))
	print ("Total gold coins: " + str(money))
	print ("You have access to the places in "+ str(currentplace) + ", and are currently traveling to " + str(goal))

def what_enemy(enemy):
	if enemy == "road_imp":
		enemyHP = 40
		enemyattack = 5
		enemysprite = asciiart.imp
		enemyattacksprite = asciiart.impattack
		enemyname = "n imp"
		moneyforkill = random.randrange(10, 30, 5)
		earnXP = 20
		
#Variables used for the first time the player goes through something
helpexplain = True
helpfight = True
gamestart = True
magmafirst = True
ufirst = True

print ("You are the chosen hero of Teltactica!")
print ("Travel the world, to ultimately destroy the evil wizard of Terror Castle.")
while (gamestart):
	currentplace, k0, k1, k2, k3, k4, k5 = locations.placesdiscover(currentplace, k0, k1, k2, k3, k4, k5)
	if (helpexplain):
		print ("First, you should use [map] to see any available locations. Then use [travel] to set that as your goal!")
		sleep(1)
		print ("Use the [help] command to learn commands.")
		helpexplain = False
	action = input("Action> ")
	if days == 0:
		print ("You have arrived at " + goal)
		currentplace = goal
		if goal == "Magma Lane" and magmafirst == True:
			readx ("HALT! IT IS I!\n")
			sleep(1)
			readx ("FIREY FRANCESO! DEFENDER OF THE ENTRANCE TO MAGMA LANE!\n")
			sleep(1)
			readx ("NOW WE SHALL... DO BATTLE! YES! THAT IS WHAT WE SHALL DO!\n")
			sleep(1)
			#TODO battle with firey franceso before entering magma lane for the first time
			readx("You have bested me... I shall begrudgeingly grant thee access to Magma Lane.\n")
			readx("Maybe you can help the townspeople with their issues in the temple... you can only go there if you are worthy.\n")
			magmafirst = False
	if action == "equip":
		weapon, happystickhave, swordhave, goldpanhave = equip(
		    weapon, happystickhave, swordhave, goldpanhave)
	elif action == "help":
		givehelp()
	elif action == "stats":
		showStats(bonusDP)
	elif action == "walk":
		print ("You walk towards your current goal " + goal)
		days = days - 1
		roll = 1
		roll = random.randrange(1, 3)
		if roll == 2:
			print ("A figure appears before you!")
			print ("FIGHT!")
			if helpfight:
				readx("You are about to fight!\n")
				readx("Use [a] to attack normally.\n\n")
				readx("Use [s] for a special attack.\n")
				readx("You can only special attack a certain amount in a battle. Make sure you read the counter!\n\n")
				readx("Lastly, you can use [p] to use a potion.\n")
				sleep(4)
				print ("NOW FIGHT!")
				helpfight = False
			bonusDP = dpBonus(bonusDP)
			what_enemy("road_imp")
			enemyHP, enemyattack, enemysprite, enemyattacksprite, enemyname, moneyforkill, HP,maxHP, DP, bonusDP, specialuses, money, potions, EXP, earnXP = battle.battle(enemyHP, enemyattack, enemysprite, enemyattacksprite, enemyname, moneyforkill, HP,maxHP, DP, bonusDP, specialuses, money, potions, EXP, earnXP)
			print ("You now have "+ str(EXP) + " EXP, and " + str(money) + " gold!")
	elif action == "shop":
		print ("A sign at a local shop catches your eye, and you enter.")
		if currentplace == "Shiverton Village":
			print (asciiart.happyshop)
			sleep(1)
			money, happystickhave, swordhave = shops.happyStore(money, happystickhave, swordhave)
		elif currentplace == "Magma Lane":
			#TODO hot hot goods art
			sleep(1)
			money,swordhave,goldpanhave = shops.HotHotGoods(money,swordhave,goldpanhave)
		else:
			print ("Wha..? If you see this yell at Lucca.")
	elif action == "potion":
		if (potions > 0):
			print ("You grab a red vile out of your pocket.")
			print ("Uncorking the top, you take a swig from a potion")
			HP = maxHP
			potions = potions - 1
			print ("You have " + str(HP) + " HP!")
		else:
			print ("You reach for the potion section in your bag to find none are there :c.")
			print ("Go buy some from a local [shop]!")
	elif action == "map":
		print ("You pull out and assess you map.")
		locations.printmap(currentplace)
	elif action == "travel":
		goal = locations.traveltime(currentplace)
		print ("Your goal is now " + goal)
		if goal == "Magma Lane":
			days = 10
		elif goal == "Shiverton Village":
			days = 10
		elif goal == "Vile Valley":
			days == 20
		if goal != "[You have no goal, use [travel] to set it!]":
			print ("It will take " + str(days) + " days to get to your goal.")
	elif action == "upgrade":
		EXP, HP, maxHP, STR, money, ufirst = upgrade.upgradeGod(EXP, HP, maxHP, STR, money, ufirst)
	else:
		print ("Not a command.")
