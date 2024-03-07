import random
import os
import time

current_battle = 1

def fight(player_health, enemy_health, battle):
    #rat fight
    if battle == 1:
        os.system('cls')
        print(f"YOU: {player_health} ENEMY: {enemy_health}")
        print("THE FAT RAT ATTACKS!")
        while True:
            #player turn
            choice = input()
            if choice.lower() == "punch":
                print("punched da rat ")
                damage = random.randint(0, 20)
                time.sleep(1)
                print(f"DEALT {damage} DAMAGE!")
                time.sleep(1)
                enemy_health -= damage
                os.system('cls')
                if enemy_health <= 0:
                    enemy_health = 0
                    print(f"YOU: {player_health} ENEMY: {enemy_health}")
                    print("YOU WIN!")
                    return "win"

            #handling invalid input
            else:
                print("invalid")
                time.sleep(1)
                os.system('cls')
                print(f"YOU: {player_health} ENEMY: {enemy_health}")
                continue

             #rat turn
            print(f"YOU: {player_health} ENEMY: {enemy_health}")
            print("THE RAT BITES YOU!")
            damage = random.randint(0, 5)
            time.sleep(1)
            print(f"DEALT {damage} DAMAGE!")
            player_health -= damage
            time.sleep(1)
            os.system('cls')
            print(f"YOU: {player_health} ENEMY: {enemy_health}")

            if player_health <= 0:
                player_health = 0
                os.system('cls')
                print(f"YOU: {player_health} ENEMY: {enemy_health}")
                print("YOU LOSE!")
                return "lose"

    if battle == 2:
        os.system('cls')
        print(f"YOU: {player_health} ENEMY: {enemy_health}")
        print("\"EY IM WALKIN' HERE!\"")
        while True:
            #player turn
            choice = input()
            if choice.lower() == "punch":
                print("punched da new yorker ")
                damage = random.randint(0, 20)
                time.sleep(1)
                print(f"DEALT {damage} DAMAGE!")
                time.sleep(1)
                enemy_health -= damage
                os.system('cls')
                if enemy_health <= 0:
                    enemy_health = 0
                    print(f"YOU: {player_health} ENEMY: {enemy_health}")
                    print("YOU WIN!")
                    time.sleep(2)
                    print("YOU GOT $50!")
                    return "win"

            #handling invalid input
            else:
                print("invalid")
                time.sleep(1)
                os.system('cls')
                print(f"YOU: {player_health} ENEMY: {enemy_health}")
                continue

             #rat turn
            print(f"YOU: {player_health} ENEMY: {enemy_health}")
            print("NEW YORKER STABS YOU")
            damage = random.randint(0, 10)
            time.sleep(1)
            print(f"DEALT {damage} DAMAGE!")
            player_health -= damage
            time.sleep(1)
            os.system('cls')
            print(f"YOU: {player_health} ENEMY: {enemy_health}")

            if player_health <= 0:
                player_health = 0
                os.system('cls')
                print(f"YOU: {player_health} ENEMY: {enemy_health}")
                print("YOU LOSE!")
                return "lose"

if fight(15, 10, 1) == "lose":
    quit()
time.sleep(3)
if fight(15, 15, 2) == "lose":
    quit()
time.sleep(3)
if fight(15, 2, 1) == "lose":
    quit()
time.sleep(3)