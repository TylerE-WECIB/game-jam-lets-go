import os
import time
import random
import proj
import mother


def main():
    # Assigns default player statistics for all game scene functions
    player_health, player_sanity, player_position, player_money, player_inventory, grocery = 10, 10, 0, 20, [], False
    player_name = input('Who are ya?: ').capitalize()
    time.sleep(0.5)
    os.system('cls')
    print(f'In a world...where groceries must be purchased, only {player_name} can buy them!', end="")
    input()
    os.system('cls')
    print("unfortunately, you live in new york. good luck bozo")
    time.sleep(2)
    input("[TAP] Enter to start!")
    os.system('cls')
    print('')
    scene1(player_health, player_sanity, player_name, player_inventory, player_money)
    scene2(player_health, player_sanity, player_inventory, player_name)

def inventory_ui(inventory, health, money):
    print(inventory)
    player_choice = input('1. Use   2. Modify  x. Close').lower()
    while player_choice:
        os.system('cls')
        if player_choice == '1':
            print(inventory)
            player_choice = input('[Enter] item name to use  x. Close\n: ').lower()
            if player_choice in inventory:
                if player_choice == 'pizza':
                    print('You used pizza')
                    inventory.remove('pizza')
                    health += 5
                elif player_choice == 'cheese':
                    print('You used cheese')
                    inventory.remove('cheese')
                    health += 2
                elif player_choice == 'wallet':
                    print('You added $50 to your pocket')
                    inventory.remove('wallet')
                    money += 50
                elif player_choice == 'weapon':
                    print('You dropped the weapon on your foot')
                    inventory.remove('weapon')
                    health -= 3
                else:
                    print(f'You can use that item.')
                    player_choice = input(': ').lower()
            elif player_choice == 'x':
                break
            else:
                print(f'{player_choice} not in inventory')
                player_choice = input(': ').lower()

        elif player_choice == '2':
            player_choice = input('[Enter] item name to remove  x. Close\n: ').lower()
            if player_choice in inventory:
                inventory.remove(player_choice)
                print(inventory)
            elif player_choice == 'x':
                break
            else:
                print(f'{player_choice} not in inventory')
                player_choice = input(': ').lower()

        elif player_choice == 'x':
            break

        else:
            player_choice = input('1. Use   2. Modify  x. Close').lower()


# Scene 1: home, user may enter room and kitchen
def scene1(health, sanity, name, inventory, money):
    room, fridge = ['weapon', 'pizza', 'wallet'], ['cheese', 'pizza']
    grocery_list = ['bread', 'milk', 'eggs', 'cheese', 'yogurt']

    # objective = False until an objective has been met
    objective = False  # Objective: Defeat Peter Griffin
    os.system('cls')
    time.sleep(.5)
    game_time = '6:30 pm'
    for i in game_time:
        print(i, end='')
        time.sleep(.2)
    print('\n')

    print(
        '     It was the middle of summer and you\'re playing Fortnite zero build with your friends,', end=''), input()
    print(
        '     Your mother already left for work this afternoon, which means you\'re home alone for the night'), input()
    os.system('cls')
    print(
        '     There\'s 1 squad left and you\'re on your way to Reckless to meet up with your squad', end=''), input()
    print('     You spot Peter Griffin looting the nearby train, currently heading in the same direction as your team')
    time.sleep(1)

    # player choice 1 : Fight Peter Griffin to obtain useful item for later
    player_choice = input('\n1. Push, they\'re a bot   2. Warn your squad   i. Check inventory\n: ').lower()
    while player_choice:
        os.system('cls')

        # If player fights, player has .4% success chance
        if player_choice == '1':
            outcome = random.randint(1, 5)

            # if random number even, user completes objective and receives reward
            if outcome % 2 == 0:
                print(
                    '     You managed to successfully finish him off', end=''), input()
                print('     Your friends were able to kill the rest of Peter Griffin\'s teammates\n')
                time.sleep(1)
                print('     Victory Royale!')
                time.sleep(.5)
                inventory.append('Crown')
                print('\nCrown added to inventory.')
                time.sleep(1)

                objective = True
                break

            # if random number odd, user did not complete objective
            else:
                print('     Deciding to instigate, you impulse yourself onto the train.', end=''), input()
                print('     Suddenly, Peter Griffin places 3 turrets and one taps you with a frenzy',
                      end=''), input()
                print('     He begins dancing on you.'), input()
                os.system('cls')
                print('     While you were getting cooked, your team was jumped by his other squad members',
                      end=''), input()
                print('     Since you did\'nt warn your friends and died, they blamed you for selling the game',
                      end=''), input()
                print('     and kicked you from the discord server.')
                time.sleep(1)
                print('\nThis action will have consequences...')
                time.sleep(.5)
                print(f'sanity: {sanity}')
                sanity -= 2
                time.sleep(1)
                print(f'sanity: {sanity}')
                time.sleep(.5)
                break

        # If player does not fight, player has 100% success chance
        elif player_choice == '2':
            print('     You decide to continue with your original plan and head back to your team.',
                  end=''), input()
            print('     You and your friends managed to kill Peter Griffin and the rest of his squad members\n')
            time.sleep(.5)
            print('     Victory Royale!')
            time.sleep(.5)
            inventory.append('crown')
            print('\nCrown added to inventory.')
            time.sleep(1)

            objective = True
            break

        elif player_choice == 'i':
            inventory_ui(inventory, health, money)
            player_choice = input('\n1. Push, they\'re a bot   2. Warn your squad   i. Check inventory\n: ').lower()

        else:
            player_choice = input('\n1. push, they\'re a bot   2. Warn your squad\n: ').lower()
    os.system('cls')

    # display ending based on user's prior choice
    if not objective:
        print(
            '     You feel the sudden urge to fight your friend as you slam your keyboard', end=''), input()
        print('     As your key cap fly across the room and glance to their direction', end=''), input()
        print('     You notice you have\'nt closed your curtains yet')
        time.sleep(.5)

    else:
        print('     After your victory, You decide to hop off for the night', end=''), input()
        print('     Taking in your room, you notice how dark it is outside since you started playing')
        time.sleep(1)

    # player choice 2 : Close Curtains to sustain sanity level
    player_choice = input('\nClose curtains?\n1. Yes   2. No\n: ')
    while player_choice:
        if player_choice == '1':
            time.sleep(.5)
            print('     You closed the curtains')
            break

        elif player_choice == '2':
            os.system('cls')
            time.sleep(.5)
            print(
                '     Because the curtains were not closed, you felt the presence of someone watching you from outside')
            time.sleep(2)
            print('This action will have consequences...')
            time.sleep(1)
            print(f'sanity: {sanity}')
            sanity -= 2
            time.sleep(1)
            print(f'sanity: {sanity}')
            time.sleep(2)
            break

        else:
            player_choice = input('\n1. Yes   2. No\n: ')
    os.system('cls')

    time.sleep(1)
    print('     You check your phone')
    time.sleep(1)
    print('''            ╭───────────────────────────────────────╮
            |                                       |
            |                                       |
            |                 7:35pm                |
            |                                       |
            |                                       |
            |                                       |
            |                                       |
            |                                       |
            |                                       |
            |                                       |
            |                                       |    
            |        Mom                 2h ago     |
            |        Missed call                    |
            |                                       |
            |        Mom                 2h ago     |
            |        1 Text Message                 |
            |                                       |
            ╰───────────────────────────────────────╯
            
            
            ''')
    time.sleep(1)

    # force player choice 3: read text message from mom
    player_choice = input('1. Read new message  x.  Close\n: ').lower()
    while player_choice:
        os.system('cls')
        if player_choice == '1':
            break

        # loop until player reads message
        elif player_choice == 'x':
            print('Its already been 2 hours since she texted you, she will not be happy when she gets home')
            player_choice = input('1. Read new message  x.  Close\n: ').lower()
        else:
            player_choice = input('1. Read new message  x.  Close\n: ').lower()
    os.system('cls')

    print(f'''\n                     Mom





                        Today 7:35 pm

        Remember to get the groceries before I get home {name}.
        List is on the fridge.

            ''')
    time.sleep(2)
    input('[TAP] Enter to Get up')

    # Continue story line
    os.system('cls')
    time.sleep(.5)
    game_time = '7:40 pm'
    for i in game_time:
        print(i, end='')
        time.sleep(.2)
    print('\n')

    print(
        '     Mom gets home at 9 pm, so you decide to start heading to the grocery store right away', end=''), input()
    print('     before you leave your room, you pause and decide to take a few items with you')
    time.sleep(.5)
    input('\n[TAP] Enter to look around your bedroom')
    os.system('cls')
    print('     As your gaze sweeps across the room, a few items catch your attention', end=''), input()
    print(
        '     you spot your wallet and a slice of pizza that you were saving for later on your desk,', end=''), input()
    print('     and a weapon peaking from underneath your bed.\n', end='')
    time.sleep(1)
    player_choice = input('\n[Enter] Item to inspect\n\nWeapon\nPizza\nWallet\nx. Nothing\ni. inventory\n: ').lower()
    while player_choice:
        if player_choice in room:
            if player_choice not in inventory:
                time.sleep(1)
                inventory.append(player_choice)
                print(f'{player_choice} added to inventory!')
                player_choice = input(': ').lower()
            else:
                print(f'{player_choice} already in inventory.')
                player_choice = input(': ').lower()
        elif player_choice == 'x':
            break
        elif player_choice == 'i':
            inventory_ui(inventory, health, money)
            player_choice = input(
                '\n[Enter] Item to inspect\n\nWeapon\nPizza\nWallet\nx. leave\ni. inventory\n: ').lower()
        else:
            print(f'You dont see any {player_choice}')
            player_choice = input(': ').lower()
    time.sleep(1)

    objective = False
    os.system('cls')
    time.sleep(.5)
    print(
        '     Now that you have acquired your means for survival, you thrown a hoodie and make your way downstairs')
    time.sleep(1)
    player_choice = input('\n1. Enter Kitchen  2. Leave House\n: ')
    while player_choice:
        os.system('cls')
        if player_choice == '2':
            time.sleep(.5)
            print('This action will have consequences...')
            time.sleep(1)
            break
        elif player_choice == '1':
            print('''     Remembering your mother\'s assignment, You swiftly walk past the foyer in front of the stairs
     and make your way into the kitchen'''), input()
            print('     You pause at the fridge')
            time.sleep(.5)
            player_choice = input('1. Open Fridge  2. Inspect note  x. Leave House\n: ').lower()
            time.sleep(.5)
            while player_choice:
                os.system('cls')
                if player_choice == 'x':
                    if objective:
                        break
                    else:
                        time.sleep(.5)
                        print('This action will have consequences...')
                        time.sleep(1)
                        break
                elif player_choice == '1':
                    print('You open the fridge to see ')
                    print('\n[Enter] Item to inspect\n\nCheese\nPizza\nsomething\nx. Close fridge\n')
                    player_choice = input(': ').lower()
                    while player_choice:
                        if player_choice in fridge:
                            time.sleep(1)
                            inventory.append(player_choice)
                            print(f'{player_choice} added to inventory!')
                            player_choice = input(': ').lower()
                        elif player_choice == 'x':
                            break
                        else:
                            print(f'You dont see any {player_choice}')
                            player_choice = input(': ').lower()
                elif player_choice == '2':
                    print('You pick up the note your mother left you. .\n')
                    time.sleep(2)
                    print('''             ______________
                                 /              /
                                |  - Bread     |
                                |  - Milk      |
                                |  - Eggs      |
                                |  - Cheese    |
                                |  - Yogurt    |
                                |______________|'''), input()
                    objective = True
                    inventory.append(grocery_list)
                    print(f'Grocery list added to inventory!')
                    break
                else:
                    player_choice = input('1. Open Fridge  2. Inspect note\n: ')
        else:
            player_choice = input('1. Enter Kitchen  2. Leave House: ')
        scene2(health, sanity, inventory, name)


# Scene 2: NYC streets, user may enter map and grocery store, and encounter random battles
def scene2(health, sanity, inventory, name):
    objective = False  # objective: Read Mothers text message
    os.system('cls')
    game_time = '7:50 pm'
    for i in game_time:
        print(i, end='')
        time.sleep(.2)
    print('\n')
    print('You step off your front porch and start down new york city', end=''), input()
    print('Your phone chimes as you lift it to check the notification')
    time.sleep(1)
    print('''     ╭───────────────────────────────────────╮
    |                                       |
    |                 7:50 pm               |
    |                                       |
    |                                       |
    |                                       |
    |                                       |
    |                                       |
    |                                       |
    |                                       |
    |                                       |
    |                                       |    
    |                                       |
    |                                       |
    |                                       |
    |        Mom                 now        |
    |        3 Text Messages                |
    |                                       |
    ╰───────────────────────────────────────╯''')
    time.sleep(.5)
    player_choice = input('1. Read new message   x.  Close\n: ').lower()
    while player_choice:
        os.system('cls')
        if player_choice == 'x':
            if not objective:
                input()
                time.sleep(.5)
                print('This action will have consequences...')
                time.sleep(1)
                print(f'sanity: {sanity}')
                sanity -= 1
                time.sleep(.5)
                print(f'sanity: {sanity}')
                break
            else:
                objective = True
                break
        elif player_choice == '1':
            objective = True
            print(f'''\n                     Mom





                        Today 7:50 pm


        Did you have a friend over?
        Who was it that you left the house with?
        {name}?
        Message:'''), input()
            break
        else:
            player_choice = input('1. Read new message   x.  Close\n: ').lower()

    os.system('cls')
    if objective:
        time.sleep(.5)
        print('     You become more anxious at the fact that someone that was once in your house, is now following you')
        time.sleep(1)
        print(f'sanity: {sanity}')
        sanity -= 4
        time.sleep(.5)
        print(f'sanity: {sanity}')
        os.system('cls')
        print(f'sanity: BAD')
        os.system('cls')

    else:
        print(
            '     You put your phone away at the sight of your mother\'s name flashing across your screen', end='')
        input()

    print('     you leave your neighbourhood and start down the street to the grocery store'), input()
    time.sleep(1)
    # Import tyler's code
    # Continue storyline en route store
    proj.run_game()

    time.sleep(.5)
    game_time = '7:40 pm'
    for i in game_time:
        print(i, end='')
        time.sleep(.2)
    print('\n')


main()

# Scene 3: Grocery store, user may encounter battle with ninja tutle
# def scene3(health, sanity, inventory, grocery_list, money):
#     dairy, deli = ['chicken', 'turkey', 'filet mignon'], ['bread', 'milk', '2% milk', 'eggs', 'cheese', 'yogurt']
#     cart = []
#
#     objective = False
#     os.system('cls')
#     time.sleep(.5)
#     game_time = '7:40 pm'
#     for i in game_time:
#         print(i, end='')
#         time.sleep(.2)
#     print('\n')
#

#     if grocery_list in inventory:
#         print(
#            '     As you enter the grocery store, you pull out the list you grabbed before you left the house', end='')
#         input()
#         player_choice = input('1. inventory   x.  Close\n: ').lower()
#         while player_choice:
#             os.system('cls')
#
#             if player_choice == 'i':
#                 inventory_ui(inventory, health, money)
#                 break
#             elif player_choice == 'x':
#                 break
#             else:
#                 player_choice = input('1. Look at Shopping List   x.  Close\n: ').lower()
#         time.sleep(.5)
#
#     else:
#         print('     As you enter the grocery store you make your way across the aisle collecting food\n', end='')
#         time.sleep(.5)
#
#     print('[Enter] department name to shop')
#     player_choice = input('Deli\nDairy\n1.  Check out\ni. inventory\n: ').lower()
#     while player_choice.lower():
#         os.system('cls')
#         if player_choice == '1':
#             total = [cart * 5 for i in cart]
#             print('Receipt\n')
#             for i in cart:
#                 print(' ', i)
#         if player_choice == 'deli':
#             print(f'     Welcome to the deli department!')
#             for i in deli:
#                 print(i)
#             choice = input('\n[Enter] Item to add to cart\n: ').lower()
#             while choice:
#                 if choice in deli:
#                     cart.append(choice)
#                 else:
#                     input(f'You dont see any {choice} in the {player_choice}\n')
#                 choice = input(': ').lower()
#         if player_choice == 'dairy':
#             print(f'     Welcome to the deli department!')
#             for i in dairy:
#                 print(i)
#             choice = input('\n[Enter] Item to add to cart\n: ').lower()
#             while choice:
#                 if choice in dairy:
#                     cart.append(choice)
#                 else:
#                     input(f'You dont see any {choice} in the {player_choice}\n')
#                 choice = input(': ').lower()
#         elif player_choice == 'i':
#             inventory_ui(inventory, inventory, money)
#             player_choice = input('Deli\nProduce\nDairy\n   x.  Leave Store\n   i. inventory: ').lower()
#         else:
#             player_choice = input('Deli\nProduce\nDairy\n   x.  Leave Store\n   i. inventory: ').lower()
#
#
