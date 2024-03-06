# Hi there! To play War Wizards, copy paste this document into a python editor.
# DON'T MAKE ANY CHANGES TO THE TEXT!
# Game produced by Tyler R. Ellis (2021)

import time
import random

# defining variables
playerHP = 20  # actual player health
dragonHP = 45  # actual dragon health
MPAmount = 25  # how much mp the player has
MPBar = 25  # render MP
playerHealthBar = playerHP  # render player health
dragonHealthBar = dragonHP  # render dragon health
dbscaling = round(dragonHP / 25)  # render amount of bars for dragon health
if (dbscaling == 0):
    dbscaling = 1
potioncount = 5  # number of health potions
powdercount = 5  # number of poison powders
boostcount = 5  # number of mp boosts
playerchoice = 0  # doesn't mean anything. just making playerchoice a variable. this will decide what action the player used
inmenu = 0  # means nothing. making it a variable. this decides what menu the player is in
turn = "player"  # decides who's turn it is
turnnum = 1  # number of turns taken to beat the dragon
dragonchoice = 0  # placeholder. this decides what attack the dragon does
attackdamage = 0  # placeholder. this will be the base damage an attack deals
crit = 0  # placeholder. this will determine the random crit chance
usedpotion = False  # this is to prevent potion spam
usedpowder = False  # this is to prevent powder spam
usedspell = False  # this is to prevent spell spam
requiredMP = 0  # placeholder
paralyzed = 0  # used for Thunder. based on the crit variable
poisoned = 0  # used for Poison Powder.
summoningmeteor = -1  # used for meteor summoning
countering = False  # used for checking counters
credit = "Tyler Ellis"  # you better not change this
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Title Screen Code
variablethatletsthegamestart = input(
    "Hit enter to run the game, type H then hit enter to learn how to play, or type C then hit enter for a compatibility check! DO NOT TYPE ANYTHING WHILE TEXT IS LOADING OR THE GAME WILL BREAK! ONLY TYPE WHEN THE \":\" SYMBOL APPEARS!\n: ").lower()
if (variablethatletsthegamestart == "c"):
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print(
        "\nIf there is only 1 line above, then this console is large enough to render War Wizards properly.\nMake sure a monospaced font is also used. Please hit enter to run the game, or change to a larger console if multiple lines are displayed.\nTo learn how to play, type H then hit enter.")
    variablethatletsthegamestart = input(": ").lower()
    if (variablethatletsthegamestart == "h"):
        print(
            "To play War Wizards, you need to pick menu options by typing out the word and hitting enter (or typing the first letter.) This is not case sensitive.")
        time.sleep(6)
        print("To win, you need to drain the dragon's health to zero while keeping your own health above zero.")
        time.sleep(6)
        print(
            "To accomplish this, you have various items and attacks to help you out. They may be restricted in some ways however.")
        time.sleep(6)
        print(
            'While "Fight" moves are free, Bag Items are limited by count and can not be used multiple times in the same turn. Magic Spells are limited by MP.')
        time.sleep(7)
        print(
            "You can gain MP by attacking the dragon or using Mana Boosts. Moves can also crit, increasing their damage. \nEach menu option has a different effect when used in combat.")
        time.sleep(6)
        print("Type Y then hit enter for an explanation on each choice, or hit enter to proceed to the game.")
        variablethatletsthegamestart = input(": ").lower()
        if (variablethatletsthegamestart == "y"):
            print(
                "_Fight_\nPunch: A simple weak attack.\nTalk: Tell the dragon to leave. This has a small chance to work.\nCounter:Get in a defensive stance and counter the dragon if they attack on the next turn. If the dragon does something else, it will backfire.")
            time.sleep(10)
            print(
                "\n_Magic_\nThunder:Damages the dragon with lightning with a small chance to skip the dragon's turn. Costs 15MP.\nFireball: Shoots a ball of fire that does decent damage. Costs 10MP.\nMeteor: A very strong attack that takes multiple turns to charge. Costs All MP.")
            time.sleep(15)
            print(
                "\n_Bag_\nHealth Potion: Heals 5 HP.\nPoison Powder: Deals chip damage to both you and the dragon for 3 turns.\nMana Boost: Increases MP by 10, but uses up your turn.")
            time.sleep(10)
            print("\n_Run_\nYou can't.\n")
            time.sleep(2)
            variablethatletsthegamestart = input("Hit enter to run the game!").lower()

if (variablethatletsthegamestart == "h"):
    print(
        "To play War Wizards, you need to pick menu options by typing out the word and hitting enter (or typing the first letter.) This is not case sensitive.")
    time.sleep(6)
    print("To win, you need to drain the dragon's health to zero while keeping your own health above zero.")
    time.sleep(6)
    print(
        "To accomplish this, you have various items and attacks to help you out. They may be restricted in some ways however.")
    time.sleep(6)
    print(
        'While "Fight" moves are free, Bag Items are limited by count and can not be used multiple times in the same turn. Magic Spells are limited by MP.')
    time.sleep(7)
    print(
        "You can gain MP by attacking the dragon or using Mana Boosts. Moves can also crit, increasing their damage. \nEach menu option has a different effect when used in combat.")
    time.sleep(6)
    print("Type Y then hit enter for an explanation on each choice, or hit enter to proceed to the game.")
    variablethatletsthegamestart = input(": ").lower()
    if (variablethatletsthegamestart == "y"):
        print(
            "_Fight_\nPunch: A simple weak attack.\nTalk: Tell the dragon to leave. This has a small chance to work.\nCounter:Get in a defensive stance and counter the dragon if they attack on the next turn. If the dragon does something else, it will backfire.")
        time.sleep(10)
        print(
            "\n_Magic_\nThunder:Damages the dragon with lightning with a small chance to skip the dragon's turn. Costs 15MP.\nFireball: Shoots a ball of fire that does decent damage. Costs 10MP.\nMeteor: A very strong attack that takes multiple turns to charge. Costs All MP.")
        time.sleep(15)
        print(
            "\n_Bag_\nHealth Potion: Heals 5 HP.\nPoison Powder: Deals chip damage to both you and the dragon for 3 turns.\nMana Boost: Increases MP by 10, but uses up your turn.")
        time.sleep(10)
        print("\n_Run_\nYou can't.\n")
        time.sleep(2)
        variablethatletsthegamestart = input(
            "Hit enter to run the game, or type C then hit enter for a compatibility check!").lower()
        if (variablethatletsthegamestart == "c"):
            print(
                "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            print(
                "\nIf there is only 1 line above, then this console is large enough to render War Wizards properly.\nMake sure a monospaced font is also used. Please hit enter to run the game, or change to a larger console if multiple lines are displayed.")
            variablethatletsthegamestart = input(": ")


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Regular Message Display
def printmessage(message):
    for x in (str(message)):
        print(x, end="")
        time.sleep(0.02)
    print("\n", end="")


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Damage Message Display
def printattack(message1, message2, message3):
    global attackdamage
    global paralyzed
    for x in (str(message1) + str(message2) + str(message3)):
        print(x, end="")
        time.sleep(0.03)
    print("\n", end="")


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Title Screen Code
def title_screen():
    global credit

    print(" /■■      /■■                           /■■      /■■ /■■                                    /■■          ")
    time.sleep(0.1)
    print("| ■■  /■ | ■■                          | ■■  /■ | ■■|__/                                   | ■■          ")
    time.sleep(0.1)
    print("| ■■ /■■■| ■■  /■■■■■■   /■■■■■■       | ■■ /■■■| ■■ /■■ /■■■■■■■■  /■■■■■■   /■■■■■■  /■■■■■■■  /■■■■■■■")
    time.sleep(0.1)
    print("| ■■/■■ ■■ ■■ |____  ■■ /■■__  ■■      | ■■/■■ ■■ ■■| ■■|____ /■■/ |____  ■■ /■■__  ■■/■■__  ■■ /■■_____/")
    time.sleep(0.1)
    print("| ■■■■_  ■■■■  /■■■■■■■| ■■  \__/      | ■■■■_  ■■■■| ■■   /■■■■/   /■■■■■■■| ■■  \__/ ■■  | ■■|  ■■■■■■ ")
    time.sleep(0.1)
    print("| ■■■/ \  ■■■ /■■__  ■■| ■■            | ■■■/ \  ■■■| ■■  /■■__/   /■■__  ■■| ■■     | ■■  | ■■ \____  ■■")
    time.sleep(0.1)
    print("| ■■/   \  ■■|  ■■■■■■■| ■■            | ■■/   \  ■■| ■■ /■■■■■■■■|  ■■■■■■■| ■■     |  ■■■■■■■ /■■■■■■■/")
    time.sleep(0.1)
    print("|__/     \__/ \_______/|__/            |__/     \__/|__/|________/ \_______/|__/      \_______/|_______/ ")
    print("                                                                                  ", end="")
    for x in ("Terminal Edition\nby " + credit + "\nVer. 1.1 \n"):
        print(x, end="")
        time.sleep(0.1)
    if (credit != "Tyler Ellis"):
        quit()
    time.sleep(0.5)
    printmessage("Press Enter to Start!")
    gamestart = input(":")


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Loading Bar Code
def loading():
    print("loading...\n")
    for x in ("█████████████████████████████████████████████"):
        print(x, end="")
        time.sleep(0.05)
    time.sleep(0.5)
    printmessage(" Done!")
    global playername
    playername = input("Enter the Name of Your Hero: ")
    printmessage("Starting Quest...")
    time.sleep(1.5)
    print("╔═══════════════════════════════╗")  # Dragon Appears popup
    time.sleep(0.02)
    print("║     A WILD DRAGON APPEARS!    ║")
    time.sleep(0.02)
    print("╚═══════════════════════════════╝")
    time.sleep(2)


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Draws the Dragon and its HP
def drawdragon():
    global dragonHealthBar
    global dragonHP
    global dbscaling
    dragonHealthBar = dragonHP

    if (dragonHP < 0):
        dragonHP = 0

    if (dragonHP > 0):
        print("                                                     /===-_---~~~~~~~~~------____")
        time.sleep(0.01)
        print("                                                  /-~___                _,-'")
        time.sleep(0.01)
        print("                 -==\\                         `//~\\   ~~~~`---.___.-~~")
        time.sleep(0.01)
        print("             ______-==|                         | |  \\           _-~`")
        time.sleep(0.01)
        print("       __--~~~  ,-/-==\\                        | |   `\        ,'")
        time.sleep(0.01)
        print("    _-~       /'    |  \\                      / /      \      /")
        time.sleep(0.01)
        print("  .'        /       |   \\                   /' /        \   /'")
        time.sleep(0.01)
        print(" /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'")
        time.sleep(0.01)
        print("/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`")
        time.sleep(0.01)
        print("                  \_|      /        _)   ;  ),   __--~~")
        time.sleep(0.01)
        print(
            "                    '~~--_/      _-~/-  / \   '-~ \\")  # this line is wonky. forward slash is messing with quote
        time.sleep(0.01)
        print("                   {\__--_/}    / \\_>- )<__\       \\")  # same here
        time.sleep(0.01)
        print("                   /'   (_/  _-~  | |__>--<__|      \\")
        time.sleep(0.01)
        print("                  |0  0 _/) )-~     | |__>--<__|     |", end="")
        print("     DRAGON: ", end="")
        while (dragonHealthBar > 0):
            print("▌", end="")
            dragonHealthBar = dragonHealthBar - dbscaling
        print(dragonHP)
        time.sleep(0.01)
        print("                  / /~ ,_/       / /__>---<__/      /")
        time.sleep(0.01)
        print("                 o o _//        /-~_>---<__-~      /")
        time.sleep(0.01)
        print("                 (^(~          /~_>---<__-      _-~")
        time.sleep(0.01)
        print("                ,/|           /__>--<__/     _-~")
        time.sleep(0.01)
        print("             ,//('(          |__>--<__|     /                  .----_")
        time.sleep(0.01)
        print("            ( ( '))          |__>--<__|    |                 /' _---_~\\")  # very wonky
        time.sleep(0.01)
        print("         `-)) )) (           |__>--<__|    |               /'  /     ~\`\\")  # wonky line
        time.sleep(0.01)
        print("        ,/,'//( (             \__>--<__\    \            /'  //        ||")
        time.sleep(0.01)
        print("      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'")
        time.sleep(0.01)
        print("    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/")
        time.sleep(0.01)
        print("  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~")
        time.sleep(0.01)
        print("       '   '  `                             ~~~~~~~~~~")
        dragonHealthBar = dragonHP


if (credit.lower() != "tyler ellis" or credit.upper() != "TYLER ELLIS"):
    quit()


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# This ASCII pic can be found at
# https://asciiart.website/index.php?art=creatures/dragons
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Counter Code
def countered(attacking):
    global countering
    global attackdamage
    global dragonHP
    global turn
    global playerHP
    global MPAmount
    if (countering == True):
        if (attacking == True):
            time.sleep(0.5)
            printmessage("COUNTERED THE DRAGON!")
            time.sleep(0.5)
            attackdamage = round(attackdamage * 1.2)
            dragonHP = dragonHP - attackdamage
            printattack("DEALT ", attackdamage, " DAMAGE!")
            MPAmount = MPAmount + 3
            countering = False
            time.sleep(0.5)
            turn = "player"
            drawdragon()
            drawmenu()

        else:
            time.sleep(0.5)
            printmessage("THE COUNTER FAILED!")
            countering = False
            time.sleep(0.5)
            playerHP = playerHP - 10
            printmessage("TOOK 10 DAMAGE!")
            time.sleep(0.5)
            turn = "player"
            drawdragon()
            drawmenu()


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Code For Player Input
def playerinput():
    global playerchoice
    global playerHP
    global dragonHP
    global potioncount
    global powdercount
    global inmenu
    global turn
    global attackdamage
    global crit
    global usedpotion
    global usedpowder
    global turnnum
    global MPAmount
    global boostcount
    global paralyzed
    global poisoned
    global countering
    global summoningmeteor

    if (summoningmeteor > 0):
        printmessage("Charging Meteor... " + str(summoningmeteor) + " Turns Remaining.")
        time.sleep(0.5)
        turn = "dragon"
        summoningmeteor = summoningmeteor - 1
        drawmenu()
    elif (summoningmeteor == 0):
        printmessage("THE METEOR STRUCK THE BATTLEFIELD!")
        time.sleep(1)
        printattack("DEALT ", round(MPAmount * 1.5), " DAMAGE!")
        time.sleep(1)
        dragonHP = dragonHP - round(MPAmount * 1.5)
        MPAmount = 0
        turn = "player"
        summoningmeteor = -1
        drawdragon()
        drawmenu()

    if (inmenu == "main"):
        playerchoice = input(": ").lower()
    else:
        playerchoice = inmenu
    if (playerchoice == "run" or playerchoice == "r"):  # Run Choice
        printmessage("You're too out of shape to run away.")
        time.sleep(1)
        drawmenu()

    if (playerchoice == "fight" or playerchoice == "f"):  # Fight Choice
        inmenu = "fight"
        print("╔═══════════════════════════════╗")
        time.sleep(0.01)
        print("║ Punch           Counter       ║")
        time.sleep(0.01)
        print("║ Talk            Back          ║")
        time.sleep(0.01)
        print("╚═══════════════════════════════╝")
        playerchoice = input(": ").lower()

        if (playerchoice == "back" or playerchoice == "b"):
            drawmenu()

        if (playerchoice == "punch" or playerchoice == "p"):  # Punch Subchoice
            printmessage("You threw hands with the dragon!")
            time.sleep(0.5)
            attackdamage = random.randint(1, 6)
            crit = random.randint(0, 9)
            if (crit == 9):
                attackdamage = attackdamage * 2
                printattack("DEALT ", attackdamage, " DAMAGE!")
                printmessage("CRITICAL HIT!")
                dragonHP = dragonHP - attackdamage
                MPAmount = MPAmount + 10
                turn = "dragon"
                time.sleep(1)
                drawmenu()

            elif (crit == 0):
                printmessage("THE ATTACK MISSED!")
                time.sleep(0.5)
                turn = "dragon"
                time.sleep(1)
                drawmenu()
            else:
                printattack("DEALT ", attackdamage, " DAMAGE!")
                dragonHP = dragonHP - attackdamage
                turn = "dragon"
                time.sleep(1)
                drawmenu()

        if (playerchoice == "talk" or playerchoice == "t"):  # Talk Subchoice
            printmessage("You asked the dragon to leave.")
            time.sleep(0.5)
            attackdamage = random.randint(1, 25)
            if (attackdamage == 25):
                printmessage("The dragon agreed to leave!")
                time.sleep(1)
                print("╔═══════════════════════════════╗")
                time.sleep(0.05)
                print("║            YOU WIN!           ║")
                time.sleep(0.05)
                print("╚═══════════════════════════════╝")
                time.sleep(0.05)
                print("Turns Taken: ", turnnum)
                printmessage("Type R Then Enter To Try Again!: ")
                restart(input().lower())

            else:
                printmessage("The dragon said no.")
                turn = "dragon"
                time.sleep(1)
                drawmenu()

        if (playerchoice == "counter" or playerchoice == "c"):  # Talk Subchoice
            printmessage("Got in counter position!")
            time.sleep(0.5)
            countering = True
            turn = "dragon"
            time.sleep(1)
            drawmenu()

        if (
                inmenu == "fight" and playerchoice != "t" and playerchoice != "talk" and playerchoice != "p" and playerchoice != "punch" and playerchoice != "c" and playerchoice != "counter" and playerchoice != "b" and playerchoice != "back" and playerHP > 0):
            printmessage("Invalid option! Please try again!")
            time.sleep(0.5)
            playerinput()

    if (playerchoice == "magic" or playerchoice == "m"):  # Fight Choice
        inmenu = "magic"
        print("╔═══════════════════════════════╗")
        time.sleep(0.01)
        print("║ Thunder 15MP  Fireball 10MP   ║")
        time.sleep(0.01)
        print("║ Meteor  ALL MP         Back   ║")
        time.sleep(0.01)
        print("╚═══════════════════════════════╝")
        playerchoice = input(": ").lower()

        if (playerchoice == "back" or playerchoice == "b"):
            drawmenu()

        if (playerchoice == "fireball" or playerchoice == "f"):
            if (MPAmount <= 9):
                printmessage("You don't have enough MP to use that!")
                drawmenu()

            printmessage("Used Fireball!")
            time.sleep(0.5)
            attackdamage = 7
            crit = random.randint(0, 9)

            if (crit == 9):
                attackdamage = attackdamage + 5
                printattack("DEALT ", attackdamage, " DAMAGE!")
                printmessage("CRITICAL HIT!")
                dragonHP = dragonHP - attackdamage
                MPAmount = MPAmount - 10
                turn = "dragon"
                time.sleep(1)
                drawmenu()
            elif (crit == 0):
                printmessage("THE ATTACK MISSED!")
                MPAmount = MPAmount - 10
                turn = "dragon"
                time.sleep(1)
                drawmenu()
            else:
                printattack("DEALT ", attackdamage, " DAMAGE!")
                dragonHP = dragonHP - attackdamage
                MPAmount = MPAmount - 10
                turn = "dragon"
                time.sleep(1)
                drawmenu()

        if (playerchoice == "thunder" or playerchoice == "t"):
            if (MPAmount <= 14):
                printmessage("You don't have enough MP to use that!")
                drawmenu()

            printmessage("Used Thunder!")
            time.sleep(0.5)
            attackdamage = random.randint(4, 7)
            crit = random.randint(0, 9)
            paralyzed = random.randint(1, 6)

            if (crit == 9):
                attackdamage = attackdamage + 4
                printattack("DEALT ", attackdamage, " DAMAGE!")
                printmessage("CRITICAL HIT!")
                dragonHP = dragonHP - attackdamage
                MPAmount = MPAmount - 15
                if (paralyzed < 4):
                    paralyzed = random.randint(4, 6)
                    printattack("PARALYZED THE DRAGON FOR ", paralyzed - 3, " TURNS!")
                turn = "dragon"
                time.sleep(1)
                drawmenu()

            elif (crit == 0):
                printmessage("THE ATTACK MISSED!")
                MPAmount = MPAmount - 15
                paralyzed = 1
                turn = "dragon"
                time.sleep(1)
                drawmenu()
            else:
                printattack("DEALT ", attackdamage, " DAMAGE!")
                dragonHP = dragonHP - attackdamage
                MPAmount = MPAmount - 15
                if (paralyzed > 3):
                    printattack("PARALYZED THE DRAGON FOR ", paralyzed - 3, " TURNS!")
                turn = "dragon"
                time.sleep(1)
                drawmenu()

        if (playerchoice == "meteor" or playerchoice == "m"):
            if (MPAmount == 0):
                printmessage("You don't have enough MP to use that!")
                drawmenu()
            else:
                printmessage("USED METEOR!!!")
                time.sleep(1)
                printmessage("The sky is shaking.")
                time.sleep(1)
                printmessage("And the earth is quaking.")
                time.sleep(1)
                summoningmeteor = round(MPAmount / 15)
                if (summoningmeteor == 0):
                    summoningmeteor = 1
                turn = "dragon"
                drawmenu()

        if (
                inmenu == "magic" and playerchoice != "t" and playerchoice != "thunder" and playerchoice != "f" and playerchoice != "fireball" and playerchoice != "meteor" and playerchoice != "m" and playerchoice != "b" and playerchoice != "back" and playerHP > 0):
            printmessage("Invalid option! Please try again!")
            time.sleep(0.5)
            playerinput()

    if (playerchoice == "bag" or playerchoice == "b"):  # Bag Choice
        inmenu = "bag"
        print("╔═══════════════════════════════╗")
        time.sleep(0.01)
        print("║ Health Potion     x " + str(potioncount) + "         ║")
        time.sleep(0.01)
        print("║ Poison Powder     x " + str(powdercount) + "         ║")
        time.sleep(0.01)
        print("║ Mana Boost        x " + str(boostcount) + "         ║")
        time.sleep(0.01)
        print("║                        Back   ║")
        time.sleep(0.01)
        print("╚═══════════════════════════════╝")
        playerchoice = input(": ").lower()

        if (playerchoice == "hp" or playerchoice == "health potion" or playerchoice == "h"):
            if (potioncount > 0 and usedpotion == False):
                printmessage("Used Health Potion!")
                potioncount = potioncount - 1
                playerHP = playerHP + 5
                usedpotion = True
                turn = "player"
                time.sleep(0.5)
                drawmenu()
            elif (potioncount > 0 and usedpotion == True):
                printmessage("Already Used A Health Potion This Turn!")
                time.sleep(0.5)
                drawmenu()
            else:
                printmessage("Out of Potions!")
                potioncount = 0
                time.sleep(0.5)
                drawmenu()

        if (playerchoice == "mb" or playerchoice == "mana boost" or playerchoice == "m"):
            if (boostcount > 0):
                printmessage("Used Mana Boost!")
                boostcount = boostcount - 1
                MPAmount = MPAmount + 10
                turn = "dragon"
                time.sleep(0.5)
                drawmenu()
            else:
                printmessage("Out of Boosts!")
                boostcount = 0
                time.sleep(0.5)
                drawmenu()

        if (playerchoice == "pp" or playerchoice == "poison powder" or playerchoice == "p"):
            if (powdercount > 0 and usedpowder == False):
                printmessage("Used Poison Powder!")
                powdercount = powdercount - 1
                poisoned = poisoned + 3
                time.sleep(0.5)
                printmessage("Poisoned The Battlefield For " + str(poisoned) + " Turns!")
                usedpowder = True
                turn = "player"
                time.sleep(0.5)
                drawmenu()
            elif (powdercount > 0 and usedpowder == True):
                printmessage("Already Used Poison Powder This Turn!")
                time.sleep(0.5)
                drawmenu()
            else:
                printmessage("Out of Powder!!")
                powdercount = 0
                time.sleep(0.5)
                drawmenu()

        if (playerchoice == "back" or playerchoice == "b"):
            drawmenu()

        if (
                inmenu == "bag" and playerchoice != "h" and playerchoice != "hp" and playerchoice != "health potion" and playerchoice != "mb" and playerchoice != "mana boost" and playerchoice != "m" and playerchoice != "pp" and playerchoice != "poison powder" and playerchoice != "p" and playerchoice != "b" and playerchoice != "back" and playerHP > 0):
            printmessage("Invalid option! Please try again!")
            time.sleep(0.5)
            playerinput()

    if (
            inmenu == "main" and playerchoice != "fight" and playerchoice != "f" and playerchoice != "magic" and playerchoice != "m" and playerchoice != "bag" and playerchoice != "b" and playerchoice != "run" and playerchoice != "r" and playerHP > 0):
        printmessage("Invalid option! Please try again!")
        time.sleep(0.5)
        playerinput()


# ----------------------------------------------------------------------------------------------------------------------------------------------------
if (credit.swapcase() != "tYLER eLLIS"):
    quit()


# Menu Draw Code
def drawmenu():
    global playerchoice
    global playerHealthBar
    global playerHP
    global dragonHP
    global inmenu
    global turn
    global MPAmount
    global MPBar
    global turnnum
    if (playerHP <= 0):
        print("╔═══════════════════════════════╗")
        time.sleep(0.01)
        print("║        OH NO! YOU LOST!       ║")
        time.sleep(0.01)
        print("╚═══════════════════════════════╝")
        printmessage("Type R Then Enter To Try Again!: ")
        restart(input().lower())
    if (dragonHP <= 0):
        print("╔═══════════════════════════════╗")
        time.sleep(0.01)
        print("║            YOU WIN!           ║")
        time.sleep(0.01)
        print("╚═══════════════════════════════╝")
        time.sleep(0.01)
        print("Turns Taken:", turnnum)
        printmessage("Type R Then Enter To Try Again!: ")
        restart(input().lower())
    if (MPAmount < 0):
        MPAmount = 0

    if (turn == "player"):
        inmenu = "main"
        print("[", playername.upper(), "]", "\nHP:", end="")
        playerHealthBar = playerHP
        while (playerHealthBar > 0):
            print("▌", end="")
            playerHealthBar = playerHealthBar - 1
        print(playerHP)
        playerHealthBar = playerHP
        print("MP:", end="")
        MPBar = MPAmount
        while (MPBar > 0):
            print("▌", end="")
            MPBar = MPBar - 1
        print(MPAmount)
        MPBar = MPAmount
        if (summoningmeteor < 0):
            print("╔═══════════════════════════════════════╗╔═══════════════════════════════╗")
            time.sleep(0.01)
            print("║           What will you do?           ║║ Fight           Magic         ║")
            time.sleep(0.01)
            print("║                                       ║║ Bag             Run           ║")
            time.sleep(0.01)
            print("╚═══════════════════════════════════════╝╚═══════════════════════════════╝")
        playerinput()
    else:
        dragonturn()


# ----------------------------------------------------------------------------------------------------------------------------------------------------
if (credit.startswith("T") == False or credit.endswith("s") == False):
    quit()


# Dragon's Attack Code
def dragonturn():
    global turn
    global dragonchoice
    global playerHP
    global dragonHP
    global usedpotion
    global usedpowder
    global turnnum
    global playerHealthBar
    global attackdamage
    global paralyzed
    global countering
    global poisoned

    if (turn == "dragon"):
        dragonchoice = random.randint(1, 10)
        usedpotion = False
        usedpowder = False
        turnnum = turnnum + 1
        if (poisoned > 0):
            poisoned = poisoned - 1
            printmessage("EVERYONE TOOK 2 DAMAGE FROM THE POISON! " + str(poisoned) + " Turns Remaining.")
            dragonHP = dragonHP = dragonHP - 2
            playerHP = playerHP - 2
            time.sleep(0.5)

        if (paralyzed > 3):
            paralyzed = paralyzed - 1
            printmessage("THE DRAGON IS PARALYZED AND UNABLE TO MOVE! " + str(paralyzed) + " Turns Remaining.")
            time.sleep(0.5)
            turn = "player"
            countered(False)
            drawmenu()

    if (dragonchoice == 1):
        printmessage("DRAGON USED FIRE BREATH!")
        attackdamage = 5
        countered(True)
        time.sleep(0.5)
        printmessage("TOOK 5 DAMAGE!")
        playerHP = playerHP - 5
        time.sleep(1.5)
        turn = "player"
        drawdragon()
        drawmenu()

    if (dragonchoice == 2):
        printmessage("DRAGON ROARED AGRESSIVELY!")
        countered(False)
        time.sleep(1.5)
        turn = "player"
        drawdragon()
        drawmenu()

    if (dragonchoice == 3):
        printmessage("DRAGON SNEEZED ON YOU!")
        attackdamage = 1
        countered(True)
        time.sleep(0.5)
        printmessage("TOOK 1 DAMAGE!")
        playerHP = playerHP - 1
        time.sleep(1.5)
        turn = "player"
        drawdragon()
        drawmenu()

    if (dragonchoice == 4):
        printmessage("DRAGON USED TORNADO!")
        attackdamage = 7
        countered(True)
        time.sleep(0.5)
        printmessage("TOOK 7 DAMAGE!")
        playerHP = playerHP - 7
        time.sleep(1.5)
        turn = "player"
        drawdragon()
        drawmenu()

    if (dragonchoice == 5):
        printmessage("DRAGON FAKED YOU OUT!")
        countered(False)
        time.sleep(1.5)
        turn = "player"
        drawdragon()
        drawmenu()

    if (dragonchoice == 6):
        printmessage("DRAGON USED FIRE BREATH!")
        attackdamage = 5
        countered(True)
        time.sleep(0.5)
        printmessage("TOOK 5 DAMAGE!")
        playerHP = playerHP - 5
        time.sleep(1.5)
        turn = "player"
        drawdragon()
        drawmenu()

    if (dragonchoice == 7):
        printmessage("DRAGON USED TAIL STAB!")
        attackdamage = 4
        countered(True)
        time.sleep(0.5)
        printmessage("TOOK 4 DAMAGE!")
        playerHP = playerHP - 4
        time.sleep(1.5)
        turn = "player"
        drawdragon()
        drawmenu()

    if (dragonchoice == 8):
        printmessage("DRAGON TOOK A NAP!")
        countered(False)
        time.sleep(1.5)
        turn = "player"
        drawdragon()
        drawmenu()

    if (dragonchoice == 9):
        printmessage("DRAGON USED CLAW STRIKE!")
        attackdamage = 4
        countered(True)
        time.sleep(0.5)
        printmessage("TOOK 4 DAMAGE!")
        playerHP = playerHP - 4
        time.sleep(1.5)
        turn = "player"
        drawdragon()
        drawmenu()

    if (dragonchoice == 10):
        dragonchoice = random.randint(1, 10)
        if (dragonchoice == 5):
            attackdamage = playerHP - 1
            printmessage("DRAGON USED BODY SLAM!")
            if (attackdamage == 0):
                time.sleep(0.5)
                printmessage("THE ATTACK MISSED!")
                countered(False)
            else:
                countered(True)
                printattack("TOOK ", attackdamage, " DAMAGE!")
            playerHP = playerHP - attackdamage
            time.sleep(3)
            turn = "player"
            drawdragon()
            drawmenu()
        if (dragonchoice == 2):
            printmessage("DRAGON USED SOUL SWAP!")
            time.sleep(0.5)
            printmessage("SWAPPED HP WITH THE DRAGON!")
            countered(False)
            playerHealthBar = playerHP
            playerHP = dragonHP
            dragonHP = playerHealthBar
            time.sleep(1.5)
            turn = "player"
            drawdragon()
            drawmenu()
        else:
            printmessage("DRAGON USED HURRICANE!")
            attackdamage = 12
            countered(True)
            time.sleep(0.5)
            printmessage("TOOK 12 DAMAGE!")
            playerHP = playerHP - 12
            turn = "player"
            drawdragon()
            drawmenu()


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Restart Code
def restart(restartchoice):
    if (restartchoice == "r"):
        global playerHP
        global dragonHP
        global MPAmount
        global MPBar
        global playerHealthBar
        global dragonHealthBar
        global dbscaling
        global potioncount
        global powdercount
        global boostcount
        global playerchoice
        global inmenu
        global turn
        global turnnum
        global dragonchoice
        global attackdamage
        global crit
        global usedpotion
        global usedpowder
        global usedspell
        global requiredMP
        global paralyzed
        global poisoned
        global summoningmeteor
        global countering
        global credit

        playerHP = 20  # actual player health
        dragonHP = 45  # actual dragon health
        MPAmount = 25  # how much mp the player has
        MPBar = 25  # render MP
        playerHealthBar = playerHP  # render player health
        dragonHealthBar = dragonHP  # render dragon health
        dbscaling = round(dragonHP / 25)  # render amount of bars for dragon health
        if (dbscaling == 0):
            dbscaling = 1
        potioncount = 5  # number of health potions
        powdercount = 5  # number of poison powders
        boostcount = 5  # number of mp boosts
        playerchoice = 0  # doesn't mean anything. just making playerchoice a variable. this will decide what action the player used
        inmenu = 0  # means nothing. making it a variable. this decides what menu the player is in
        turn = "player"  # decides who's turn it is
        turnnum = 1  # number of turns taken to beat the dragon
        dragonchoice = 0  # placeholder. this decides what attack the dragon does
        attackdamage = 0  # placeholder. this will be the base damage an attack deals
        crit = 0  # placeholder. this will determine the random crit chance
        usedpotion = False  # this is to prevent potion spam
        usedpowder = False  # this is to prevent powder spam
        usedspell = False  # this is to prevent spell spam
        requiredMP = 0  # placeholder
        paralyzed = 0  # used for Thunder. based on the crit variable
        poisoned = 0  # used for Poison Powder.
        summoningmeteor = -1  # used for meteor summoning
        countering = False  # used for checking counters
        credit = "Tyler Ellis"  # you better not change this

        drawdragon()
        drawmenu()


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# The Game actually starts here
if (
        variablethatletsthegamestart == "d" or variablethatletsthegamestart == "debug"):  # lets you skip past the title screen and loading for coding purposes
    playername = "debug"
if (variablethatletsthegamestart == "hard"):
    printmessage("You made the dragon scarier!")
    time.sleep(1)
    dragonHP = 100
    dbscaling = round(dragonHP / 25)

if (variablethatletsthegamestart != "d" and variablethatletsthegamestart != "debug"):
    title_screen()
    loading()
drawdragon()
drawmenu()
