import os
import time
import random
# add speak function
# dialogue before leaving the house

def main():

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
    home(player_name)
    city()
    store()


main()


def home(player_name):
    player_sanity, player_money = 10, 20
    objective = False
    inventory, room, fridge = [], ['weapon', 'pizza', 'wallet'], ['cheese', 'pizza']
    grocery_list = ['bread', 'milk', 'eggs', 'cheese', 'yogurt']

    os.system('cls')
    time.sleep(.5)
    game_time = '7:30 pm'
    for i in game_time:
        print(i, end='')
        time.sleep(.2), print('\n')

    print('     It was the middle of summer and you are in a zero build Fortnite match with your friends,', end=''),
    input()
    print('     Your mother already left for work this afternoon which meant you are all by yourself for the night.')
    input()
    os.system('cls')
    print('     Theres 1 squad left and you\'re on your way to Reckless to meet back up with your squad,', end='')
    input()
    print('     you spot a Peter Griffin looting the nearby train currently heading in the same direction.')
    time.sleep(1)
    player_choice = input('\n1. push, they\'re a bot   2. Warn your squad\n: ')
    while player_choice:
        os.system('cls')
        if player_choice == '2':
            print('     You decide to continue with your original plan and head back to your team.', end=''), input()
            print('     You and your squad managed to kill Peter Griffin and the rest of his teammates\n')
            time.sleep(.5)
            print('     Victory Royale!')
            time.sleep(.5)
            inventory.append('Crown')
            print('\nCrown added to inventory.'),
            time.sleep(1)
            objective = True
            break
        elif player_choice == '1':
            outcome = random.randint(1, 5)
            if outcome % 2 == 1:
                print('     Deciding to instigate, you impulse yourself onto the train,', end='')
                input()
                print('     Suddenly, Peter Griffin places 3 turrets and one taps you with a frenzy.', end=''), input()
                print('     He begins dancing on you.'), input()
                os.system('cls')
                print('     While you were getting cooked, your team was jumped by his other squad members.', end='')
                input()
                print('     Since you did\'t warn your friends and died, they blamed you for selling the game,', end='')
                input()
                print('     and kicked you from the discord server')
                time.sleep(.5)
                print('\nThis action will have consequences...'), input()
                time.sleep(1)
                break
            elif outcome % 2 == 0:
                print('     You managed to successfully finish off Peter Griffin, and rejoin your team', end='')
                input()
                print('You and your squad managed to kill the rest of Peter Griffin\'s teammates\n')
                time.sleep(.5)
                print('     Victory Royale!')
                time.sleep(.5)
                inventory.append('Crown')
                print('\nCrown added to inventory.'), input()
                objective = True
                break
        else:
            player_choice = input('\n1. push, they\'re a bot   2. Warn your squad\n: ')

    os.system('cls')
    if not objective:
        print('     In a fit of rage, you get the sudden urge to fight your friend and slam your keyboard', end='')
        input()
        print('     You look in the direction your key caps few, You notice you have\'nt closed your curtains yet')
        time.sleep(.5)
    else:
        print('     After your victory, You decide to hop off for the night', end=''), input()
        print('     Taking in your room, you notice how dark it is outside since you got on')
        time.sleep(.5)

    player_choice = input('\nClose curtains?\n1. Yes   2. No\n: ')
    while player_choice:
        if player_choice == '1':
            time.sleep(.5)
            print('     You closed the curtains')
            time.sleep(1)
            break
        elif player_choice == '2':
            os.system('cls')
            time.sleep(.5)
            print('     Because the curtains were not closed, you felt the presence of someone else lucking over you')
            time.sleep(.5)
            print('This action will have consequences...')
            time.sleep(1)
            print(f'sanity: {player_sanity}'), input()
            player_sanity -= 1
            print(f'sanity: {player_sanity}')
            time.sleep(1)
            break
        else:
            player_choice = input('\n1. Yes   2. No\n: ')
    os.system('cls')

    print('     You check your phone')
    time.sleep(1)
    print('''╭───────────────────────────────────────╮
    |                                       |
    |                 7:43pm                |
    |                 7:43pm                |
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
    ╰───────────────────────────────────────╯''')
    time.sleep(1)
    while True:
        player_choice = input('1. Read new message  x.  Close\n: ')
        os.system('cls')
        if player_choice != '1':
            print('Are you seriously going to leave your mom on read?')
            while True:
                choice = input('1. Yes   2. No\n: ')
                if choice == '2':
                    print('Good, She raised you better than that')
                    break
                else:
                    print('Its already been 2 hours since she texted you, she will not be happy when she gets home')
                    break
        else:
            break

    os.system('cls')
    print(f'''\n                     Mom





                        Today 5:34 pm

        Remember to get the groceries before I get home {player_name}.
        List is on the fridge.

    Message:''')
    player_choice = input('1. Reply   x.  Close\n: ')
    while player_choice != 'x':
        os.system('cls')
        if player_choice == '1':
            print('''\n                     Mom





                    Today 5:34 pm

        Remember to get the groceries before I get home {player_name}.
        List is on the fridge.
                                ''')

            message = input('Message: ')
            os.system('cls')
            print(f'''\n                    Mom





                    Today 5:34 pm

        Remember to get the groceries before I get home {player_name}.
        List is on the fridge.

                                                {message}
                                ''', end='')
            time.sleep(1)
            print('                     delivered'), input()
            time.sleep(1)
            break
    os.system('cls')
    time.sleep(1)
    input('[TAP] Enter to Get up')

    # Continue story line
    os.system('cls')
    time.sleep(.5)
    game_time = '8:00 pm'
    for i in game_time:
        print(i, end='')
        time.sleep(.2)
    print('\n')
    print('     Mom gets home at 10 pm, so you decide to start heading to the grocery store right away', end='')
    input()
    print('     before you leave your room, you pause and decide to take a few items with you.')
    time.sleep(.5)
    input('\n[TAP] Enter to look around your bedroom')
    os.system('cls')
    print('     As your gaze sweeps across the room, a few items catch your attention.', end=''), input()
    print('     Resting on your desk, you spot your wallet with a slice of pizza you were saving for later', end='')
    input()
    print('     and a weapon peaking from underneath your bed.', end='')
    time.sleep(1)
    player_choice = input('\n[Enter] Item to inspect\n\nWeapon\nPizza\nWallet\nx. Nothing\n: ').lower()
    while player_choice:
        if player_choice == 'x':
            if 'Pizza' in inventory:
                break
            else:
                print('I should probably take the pizza with me')
                player_choice = input(': ')
        else:
            if player_choice in room:
                time.sleep(1)
                inventory.append(player_choice)
                print(f'{player_choice} added to inventory!')
                player_choice = input(': ')
            else:
                print(f'You dont see any {player_choice}')
                player_choice = input(': ')
    time.sleep(1)

    player_choice = input('Would you like to remove an item from your inventory?\n1. Yes   2. No\n: ')
    while player_choice:
        if player_choice == '1':
            player_choice = input(f'Enter item you would like to remove\nInventory:{inventory}\n: ')
            if player_choice in inventory:
                inventory = inventory.remove(player_choice)
            else:
                print(f'{player_choice} is not in inventory')
                player_choice = input(f'Enter item you would like to remove\nInventory:{inventory}\n: ')
        elif player_choice == 'x':
            break
        else:
            player_choice = input('Would you like to remove an item from your inventory')

    objective = False
    os.system('cls')
    time.sleep(.5)
    print('     Now that you have acquired your means for survival, you thrown a hoodie and make your way downstairs')
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
            print('You pause at the fridge')
            time.sleep(.5)
            player_choice = input('1. Open Fridge  2. Inspect note  x. Leave House\n: ')
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
                    print('\n[Enter] Item to inspect\n\nCheese\nPizza\nsomething\nx. Nothing\n')
                    player_choice = input(': ').lower()
                    # fix this
                    if player_choice in fridge:
                        time.sleep(1)
                        inventory.append(player_choice)
                        print(f'{player_choice} added to inventory!')
                        player_choice = input(': ')
                    else:
                        print(f'You dont see any {player_choice}')
                        player_choice = input(': ')
                elif player_choice == '2':
                    print('You pick up the note your mother left you. .\n')
                    time.sleep(2)
                    print('''   ______________
     /              /
    |  - Bread     |
    |  - Milk      |
    |  - Eggs      |
    |  - Cheese    |
    |  - Yogurt    |
    |______________|'''), input()
                    objective = True
                    print(f'Grocery list added to inventory!')
                    break
                else:
                    player_choice = input('1. Open Fridge  2. Inspect note\n: ')
        else:
            player_choice = input('1. Enter Kitchen  2. Leave House: ')

    return objective


def city():
    # New scene
    os.system('cls')
    game_time = '8:00 pm'
    for i in game_time:
        print(i, end='')
        time.sleep(.2)
    print('\n')
    print('You step off your front porch and start down new york city', end=''), input()
    print('Your phone chimes as you lift it to check the notification')
    time.sleep(1)
    print('''╭───────────────────────────────────────╮

    |                 8:10 pm               |
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
    |        1 Attachment                   |
    |                                       |
    |        Mom                 now        |
    |        3 Text Messages                |
    |                                       |
    ╰───────────────────────────────────────╯''')
    time.sleep(.5)
    player_choice = input('1. Read new message   x.  Close\n: ')
    bad_ending = True
    while player_choice:
        os.system('cls')
        if player_choice == 'x':
            if not bad_ending:
                input()
                time.sleep(.5)
                print('This action will have consequences...')
                time.sleep(1)
                print(f'sanity: {player_sanity}')
                player_sanity -= 1
                time.sleep(.5)
                print(f'sanity: {player_sanity}')
                break
            else:
                bad_ending = False
                break
        elif player_choice == '1':
            bad_ending = False
            print(f'''\n                     Mom





                        Today 8:20 pm
                        
        [ascii image of front door camera]
        
        Did you have a friend over?
        Who was it that you left the house with?
        {player_name}?
        Message:'''), input()
            break
        else:
            player_choice = input('1. Read new message   x.  Close\n: ')

    os.system('cls')
    if bad_ending:
        print('     bad ending here', end='')
        input()
        print('     more bad ending')
        time.sleep(.5)
    else:
        print('     good ending here', end=''), input()
        print('     more good ending')
        time.sleep(.5)
# Continue storyline en route store
# ascii map
    return objective

# New scene
    os.system('cls')
    time.sleep(.5)
    game_time = '8:40 pm'
    for i in game_time:
        print(i, end='')
        time.sleep(.2)
    print('\n')

    if grocery:
        print('     As you enter the grocery store, you pull out the list you grabbed before you left the house', end=''
              )
        input()
        print('     more good ending')
        time.sleep(.5)
    else:
        print('     As you enter the grocery store you make your way across the aisle collecting food ', end='')
        input()
        time.sleep(.5)

    print('     As you you enter the grocery store you pull out the list ', end='')
    print('[Enter] department name to shop')
    player_choice = input('Deli\nProduce\nDairy\n1. Look at Shopping List   x.  Leave Store\n: ')
    while player_choice:
        os.system('cls')
        if player_choice == 'x':
            if len(cart) > 0:
                break
            else:
                time.sleep(.5)
                print('This action will have consequences...')
                time.sleep(1)
                break
        elif player_choice == 'deli' or 'dairy':
            print(f'     Welcome to the {player_choice} department!')
            while True:
                if player_choice == 'Deli':
                    for i in grocery_store[0]:
                        print(i)
                    choice = input('\n[Enter] Item to add to cart\n: ').lower()
                    cart = [choice if choice in grocery_store[0] else input(
                        f'You dont see any {choice} in the {player_choice}\n')]
                    choice = input(': ').lower()
                elif player_choice == 'Produce':
                    for i in grocery_store[1]:
                        print(i)
                    choice = input('\n[Enter] Item to add to cart\n: ')
                    cart = [choice if choice in grocery_store[1] else input(
                        f'You dont see any {choice} in the {player_choice}\n')]
                    print(f'{choice} added to shopping cart')
                    choice = input(': ').lower()
                elif player_choice == 'Dairy':
                    for i in grocery_store[2]:
                        print(i)
                    choice = input('\n[Enter] Item to add to cart\n: ')
                    cart = [choice if choice in grocery_store[2] else input(
                        f'You dont see any {choice} in the {player_choice}\n')]
                    print(f'{choice} added to shopping cart')
                    choice = input(': ').lower()
                else:
                    print(f'You dont see a {player_choice} department')
                    player_choice = input(': ')
        elif player_choice == '1':
            print('\n')
            time.sleep(2)
            print('''   ______________
             /              /
            |  - Bread     |
            |  - Milk      |
            |  - Eggs      |
            |  - Cheese    |
            |  - Yogurt    |
            |______________|'''), input()
            player_choice = input('Deli\nDairy\n1. Look at Shopping List   x.  Leave Store\n: ').lower()
        else:
            player_choice = input('Deli\nDairy\n1. Look at Shopping List   x.  Leave Store\n: ').lower()


main_space()
