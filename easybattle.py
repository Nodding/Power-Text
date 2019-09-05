import asciiart
from time import sleep
import random
def simplebattle(fight, enemyHP, enemyattack, enemysprite, enemyattacksprite, enemyname, moneyforkill, HP, MaxHP, DP, bonusDP, specialuses, money, potions, EXP, earnEXP):
        # set fight FLAG to (true)
        fight = True
        #print the enemy
        print (enemysprite)
        #prints the intro to fight
        print ("A" + enemyname + " attacks with " + str(enemyHP) + " HP and " + str(enemyattack) + " attack power!")

        # dumb variables to go to python 3
        halfattack = int(enemyattack/2)
        attackminusone = enemyattack-1
        HP = HP - random.randint(halfattack, attackminusone)
        while(fight):
                #so while the fight is happening
                print ("What will you do?")
                #gathers users input
                user = input("\n> ")
                #if they press s and hit enter
                if user == "s" and specialuses > 0:
                        enemyHP = enemyHP - ((DP + bonusDP)*3)
                        print (asciiart.personspecial)
                        sleep(2)
                        print ("It has " + str(enemyHP) + " HP left!")
                        #if it kills the enemy, you win! and fight is over
                        if enemyHP <= 0:
                                fight = False
                                money = money + moneyforkill
                                print ("You won!")
                                print ("You have earned " + str(moneyforkill) + " gold pieces!")
                                print ("And " + str(earnEXP) + " EXP!")
                                EXP = EXP + earnEXP
                        elif enemyHP > 0:
                                # enemy's turn
                                print (enemyattacksprite)
                                # attacks, does damage to current health, from half to whatever his max is
                                HP = HP - random.randint(halfattack, attackminusone)
                                print ("You have " + str(HP) + " HP left!")
                                # if current health goes down to 0, end battle/game
                                if HP <= 0:
                                        print ("You lost the battle!\n")
                                        fight = False
                                else:
                                        print ("It has " + str(enemyHP) + " HP left!")
                                        print ("You have " + str(HP) + " HP left!")
                                        specialuses = specialuses - 1 # takes special use away
                                        print ("You have " + str(specialuses) + " uses of your special attack left!")
                elif user == "s" and specialuses <= 0:
                        print ("You are out of special attacks!")
                        if enemyHP > 0:
                                # enemy's turn
                                print (enemyattacksprite)
                                print ("The enemy attacks in this moment of your stupidity!")
                                # attacks, does damage to current health, from half to whatever his max is
                                HP = HP - random.randint(halfattack, attackminusone)
                                print ("You have " + str(HP) + " HP left!")
                                # if current health goes down to 0, end battle/game
                                if HP <= 0:
                                        print ("You lost the battle!\n")
                                        fight = False
                elif user == "a":
                        enemyHP = enemyHP - (DP+bonusDP)
                        print (asciiart.personattack)
                        sleep(1)
                        print ("It has " + str(enemyHP) + " HP left!")
                        if enemyHP <= 0:
                                fight = False
                                print ("You won!")
                                money = money + moneyforkill
                                print ("You have earned " + str(moneyforkill) + " gold pieces!")
                                print ("And " + str(earnEXP) + " EXP!")
                                EXP = EXP + earnEXP
                        else:
                                # enemy's turn
                                print (enemyattacksprite)
                                # attacks, does damage to current health, from half to whatever his max is
                                HP = HP - random.randint(halfattack, attackminusone)
                                #current health goes down to 0, end battle/game
                                if (HP <= 0):
                                        print ("You lost the battle!\n")
                                        fight = False
                                print ("You have " + str(HP) + " HP left!")
                elif user == "p":
                        # check to see if user still has potion uses left
                        if potions > 0:
                                if HP < MaxHP:
                                        print (asciiart.potion)
                                        print ("You used a potion! All of your health returns!")
                                        HP = MaxHP
                                        potions = potions - 1
                                else:
                                        print ("Your health is full! You didn't need a potion!")
                        else: # if not more potions, dont restore health
                                print ("You are out of potions!")
                else:
                        print ("You stood there, confused at what your brain told you to do.")
        if enemyHP > 0:# enemy's turn
                print (enemyattacksprite)
                # attacks, does damage to current health, from half to whatever his max is
                HP = HP - (random.randint((enemyattack/2), (enemyattack-1)))
                print ("Your health is " + str(HP))
                # if current health goes down to 0, end battle/game
        if HP <= 0:
                print ("You lost the battle!\n")
                fight = False
        return fight, enemyHP, enemyattack, enemysprite, enemyattacksprite, enemyname, moneyforkill, HP, MaxHP, DP, bonusDP, specialuses, money, potions, EXP, earnEXP

