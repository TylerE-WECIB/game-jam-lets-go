import os
import time
import random

# import keyboard
hp, sanity, player_position, money, inventory, items, map_open = 10, 10, 0, 0, [], ['Weapon', 'Pizza', 'Wallet'], False


# player_name = input('Who are ya?: ')
#
# time.sleep(0.5)
# os.system('cls')
# print(f'In a world...where groceries must be purchased, only {player_name} can buy them!', end="")
# input()
# os.system('cls')
# print("unfortunately, you live in new york. good luck bozo")
# time.sleep(2)
# input("[TAP] Enter to start! ")
# os.system('cls')

def home():
    story = '7:30 pm'
    for i in story:
        print(i, end='')
        time.sleep(.5)
    print('\n')

    print('     It was the middle of summer and you are playing Fortnite with your friends,', end=''), input(),
    print('     Your mother had already left for work that afternoon which meant you are all by yourself for the night.'), input()
    os.system('cls')

    print('     You check your phone')
    time.sleep(1)
    print('''\n                 7:43pm



        Mom                 2h ago
        Missed call
        
        Mom                 2h ago
        1 Text Message 

        ''')
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
    print('''\n                     Mom





                    Today 5:34 pm
            
    Remember to get the groceries before I get home.
    List is on the fridge.

Message:''')
    player_choice = input('1. Reply   x.  Close\n: ')
    while player_choice != 'x':
        os.system('cls')
        if player_choice == '1':
            print('''\n                     Mom





                Today 5:34 pm
            
    Remember to get the groceries before I get home.
    List is on the fridge.
                            ''')

            message = input('Message: ')
            os.system('cls')
            print(f'''\n                    Mom





                Today 5:34 pm
                
    Remember to get the groceries before I get home.
    List is on the fridge.

                                            {message}
                            ''', end='')
            time.sleep(1)
            print('                     delivered')
            break
    input('[TAP] Enter to put phone away')
    os.system('cls')
    time.sleep(1)
    input('[TAP] Enter to Get up')
    os.system('cls')

    story = '8:00 pm'
    for i in story:
        print(i, end='')
        time.sleep(.5)
    print('\n')
    print('     Mom gets home at 10 pm, so you decide to start heading to the grocery store right away', end='')
    input()
    print('     before you leave your room, you pause and decide to take a few items with you.')
    input('\n[TAP] Enter to look around your bedroom')
    os.system('cls')
    print('     As your gaze sweeps across the room, a few items catch your attention', end=''), input()
    print('     resting on your desk, you spot your wallet with a slice of pizza you were saving for later', end='')
    input()
    print('     and a weapon peaking from underneath your bed.', end=''), input()
    time.sleep(1)
    print('\n[Enter] Item to inspect\n\nWeapon\nPizza\nWallet\nx. Nothing\n')

    player_choice = input(': ')
    while player_choice:
        if player_choice == 'x':
            if 'Pizza' in inventory:
                break
            else:
                print('I should probably take the pizza with me')
                player_choice = input(': ')
        else:
            if player_choice in items:
                time.sleep(1)
                inventory.append(player_choice)
                print(f'{player_choice} added to inventory!')
                player_choice = input(': ')
    os.system('cls')
    time.sleep(1)
    print('     now that you have acquired your means for survival, you thrown a hoodie and make your way downstairs')
    input('\n')
    player_choice = input('1. Enter Kitchen  2. Leave House: ')
    while player_choice:
        if player_choice == '2':
            break
        if player_choice == '1':

            print('You enter the kitchen')
            
        else:
            player_choice = input('1. Enter Kitchen  2. Leave House: ')


home()


def city():
    pass


def store():
    pass
