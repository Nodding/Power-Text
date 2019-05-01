import asciiart
from time import sleep
import random
def simplebattle(fight, enemyHP, enemyattack, enemysprite, enemyattacksprite, enemyname, moneyforkill, HP, MaxHP, DP, bonusDP, specialuses, money, potions, EXP, earnEXP):
	# set fight FLAG to (true)
	fight = True
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
			enemyHP = enemyHP - ((DP + bonusDP)*3)
			print asciiart.personspecial
			sleep(2)
			#if it kills the enemy, you win! and fight is over
			if enemyHP <= 0:
				fight = False
				money = money + moneyforkill
				print "You won!"
				print "You have earned %s gold pieces!" % (moneyforkill)
				print "And %s EXP!" % (earnEXP)
				EXP = EXP + earnEXP
			elif enemyHP > 0:# enemy's turn
				print enemyattacksprite
				# attacks, does damage to current health, from half to whatever his max is
				HP = HP - ((random.randrange(enemyattack/2))+enemyattack/2)
				print "You have %s HP left!" % (HP)
				# if current health goes down to 0, end battle/game
				if HP <= 0:
					print "You lost the battle!\n"
					fight = False
			else:
				print "It has %s HP left!" % (enemyHP)
				print "You have %s HP left!" % (HP)
				specialuses = specialuses - 1 # takes special use away
				print "You have", specialuses, "uses of your special attack left!"
		elif user == "s" and specialuses <= 0:
			print "You are out of special attacks!"
			if enemyHP > 0:# enemy's turn
				print enemyattacksprite
				print "The enemy attacks in this moment of your stupidity!"
				# attacks, does damage to current health, from half to whatever his max is
				HP = HP - ((random.randrange(enemyattack/2))+enemyattack/2)
				print "You have %s HP left!" % (HP)
				# if current health goes down to 0, end battle/game
				if HP <= 0:
					print "You lost the battle!\n"
					fight = False
		elif user == "a":
			enemyHP = enemyHP - (DP+bonusDP)
			print asciiart.personattack
			sleep(1)
			if enemyHP <= 0:
				fight = False
				print "You won!"
				money = money + moneyforkill
				print "You have earned %s gold pieces!" % (moneyforkill)
				print "And %s EXP!" % (earnEXP)
				EXP = EXP + earnEXP
			elif enemyHP > 0:# enemy's turn
				print enemyattacksprite
				# attacks, does damage to current health, from half to whatever his max is
				HP = HP - ((random.randrange(enemyattack/2))+enemyattack/2)
				print "You have %s HP left!" % (HP)
				# if current health goes down to 0, end battle/game
				if HP <= 0:
					print "You lost the battle!\n"
					fight = False
	 		else:
				print "It has %s HP left!" % (enemyHP)#print info
				print "You have %s HP left!" % (HP)
		elif user == "p":
			# check to see if user still has potion uses left
			if potions > 0:
			# if health is below max, restore half of max health to current health up to total max health
				if HP < MaxHP:
					print asciiart.potion
					print "You used a potion! Some of your health returns!"
					HP = MaxHP
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
		HP = HP - ((random.randrange(enemyattack/2))+enemyattack/2)
		print "Your health is",HP
		# if current health goes down to 0, end battle/game
	if HP <= 0:
		print "You lost the battle!\n"
		fight = False
	return fight, enemyHP, enemyattack, enemysprite, enemyattacksprite, enemyname, moneyforkill, HP, MaxHP, DP, bonusDP, specialuses, money, potions, EXP, earnEXP
