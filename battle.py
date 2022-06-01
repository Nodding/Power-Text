import asciiart
from time import sleep
import random

def battle(enemyHP, enemyAttack, enemySprite, enemyAttackSprite, enemyName, moneyforkill, HP, MaxHP, DP, bonusDP, specialuses, money, potions, EXP, earnEXP):
    fighting = True
    print (enemySprite)
    print ("A" + enemyName + " attacks with " + str(enemyHP) + " HP and " + str(enemyAttack) + " attack power!")
    while (fighting):
        #so while the fight is happening
        print ("What will you do?")
        #gathers users input
        user = input("\n> ")
        if user == "a":
            enemyHP = enemyHP - (DP+bonusDP)
            print (asciiart.personattack)
            sleep(1)
            print ("It has " + str(enemyHP) + " HP left!")
            if enemyHP <= 0:
                    fighting = False
                    print ("You won!")
                    money = money + moneyforkill
                    print ("You have earned " + str(moneyforkill) + " gold pieces!")
                    print ("And " + str(earnEXP) + " EXP!")
                    EXP = EXP + earnEXP
            else:
                enemyAttacks()
        elif user == "p":
                # check to see if user still has potion uses left
                if potions > 0:
                    if HP < MaxHP:
                        print (asciiart.potion)
                        print ("You used a potion! All of your health returns!")
                        HP = MaxHP
                        potions = potions - 1
                    else:
                        print ("Your health is full! You didn't need a potion! You wasted a turn!")
                    sleep(1)
                else: # if not more potions, dont restore health
                    print ("You are out of potions!")
        elif user == "s" and specialuses > 0:
            enemyHP = enemyHP - ((DP + bonusDP)*3)
            print (asciiart.personspecial)
            specialuses -= 1
            sleep(2)
            print ("You have " + str(specialuses) + " special uses left.")
            print ("It has " + str(enemyHP) + " HP left!")
        elif user == "s" and specialuses <= 0:
            print ("You are out of special uses! You waste your turn!")
            sleep(1)
        else:
            print ("You stood there, confused at what your brain told you to do.")
        sleep(1)
        #enemy's turn!
        if enemyHP > 0:
            print ("The " + enemyName + " attacks!")
            HP = HP - enemyAttacks(enemyAttack, enemyAttackSprite)
        else:
            fighting = False
    print ("You won!")
    print ("You have earned " + str(moneyforkill) + " gold pieces!")
    print ("And " + str(earnEXP) + " EXP!")
    EXP = EXP + earnEXP
    money = money + moneyforkill

    return enemyHP, enemyAttack, enemySprite, enemyAttackSprite, enemyName, moneyforkill, HP, MaxHP, DP, bonusDP, specialuses, money, potions, EXP, earnEXP
    

def enemyAttacks(enemyAttack, enemyAttackSprite):
    halfattack = int(enemyAttack/2)
    attackminusone = enemyAttack-1
    print (enemyAttackSprite)
    # attacks, does damage to current health, from half to whatever his max is
    return random.randint(halfattack, attackminusone)