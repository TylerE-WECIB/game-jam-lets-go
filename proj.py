import os
import time
import random
# import keyboard
player_health = 10
player_position = 0
map_open = False
def draw_screen():
    pass

def draw_menu():
    pass

def draw_map():
    pass
player_name = input("Who are ya? ")

time.sleep(0.5)
os.system('cls')
print(f'In a world...where groceries must be purchased, only {player_name} can buy them!',end="")
input()
os.system('cls')
print("unfortunately, you live in new york. good luck bozo")
time.sleep(2)
input("Hit enter to start! ")
os.system('cls')