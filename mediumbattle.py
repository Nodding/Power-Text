#import art to be used remember it's artfile.imagename
import asciiart
#time for animations
from time import sleep
#start by defining name of battle and what it will be affecting
def medbattle(fight, enemyHP, enemyattack, enemysprite, enemyattacksprite, enemyname, moneyforkill, HP, MaxHP, DP, bonusDP, specialuses, money, potions):
	# set fight FLAG to (true)
	fight = True
	#sets enemy images 
	enemysprite =  asciiart.goblin#IMAGE
	enemyattacksprite = asciiart.goblinattack #IMAGE
	#last but not least enemy name and money you get when you win
	enemyname = " gross goblin "
	moneyforkill = 100
	#print the enemy
	print enemysprite
	#prints the intro to fight
	print "A" + enemyname,"attacks with", enemyHP, "HP and", enemyattack, "attack power!"
	while(fight):
	    #so while the fight is happening
	    print "What will you do?"
	    #gathers users input
	    user = raw_input("\n> ")
	    #if they press s and hit enter
	    if user == "s" and specialuses > 0:
                #deals player damage times three
                enemyHP = enemyHP - ((DP + bonusDP)*3)
                print asciiart.personspecial
                sleep(2)
		#if it kills the enemy, you win! and fight is over
                if enemyHP <= 0:
                    fight = False
                    print "You won!"
                    money = money + moneyforkill
                    print "You have earned %s gold pieces!" % (moneyforkill)
                #else, it tells you how much health enemy has, and the amount of special uses you have
                else:
                    print "It has \033[1;33m%s\033[1;m HP left!" % (enemyHP)
                    print "You have \033[1;32m%s\033[1;m HP left!" % (HP)
                    specialuses = specialuses - 1 # takes special use away
                    print "You have", specialuses, "uses of your special attack left!"
            #if they do not have special attack points left
            elif user == "s" and specialuses <= 0:
                print "You are out of special attacks for now!"
            elif user == "a":
                enemyHP = enemyHP - (DP+bonusDP)
                print asciiart.personattack
                sleep(1)
                if enemyHP <= 0:
                    fight = False
        	    print "You won!"
        	    money = money + moneyforkill
        	    print "You have earned %s gold pieces!" % (moneyforkill)
                else:
        	    print "It has \033[1;33m%s\033[1;m HP left!" % (enemyHP)#print info
        	    print "You have \033[1;32m%s\033[1;m HP left!" % (HP)
	    elif user == "p":
		    # check to see if user still has potion uses left
		if potions > 0:
		# if health is below max, restore half of max health to current health up to total max health
                    if HP < maxHPplayer:
			print asciiart.potion
			print "You used a potion! Some of your health returns!"
			HP = maxHPplayer
			potions = potions - 1
		    else:
			print "Your health is full! You don't need a potion!"
		else: # if not more potions, dont restore health
			    print "You are out of potions!"
	    else:
		print "You stood there, confused at what your brain told you to do."
			
	if enemyHP > 0:# enemy's turn
		print enemyattacksprite
	    # attacks, does damage to current health, from half to whatever his max is
	   	HP = HP - ((random.randrange(enemyDP/2))+enemyDP/2)
	   	print "Your health is",HP
	    # if current health goes down to 0, end battle/game
	if HP <= 0:
	    print "You lost the battle!\n"
	    fight = False
	    	
	return fight, enemyHP, enemyattack, enemysprite, enemyattacksprite, enemyname, moneyforkill, HP, MaxHP, DP, bonusDP, specialuses, money, potions
