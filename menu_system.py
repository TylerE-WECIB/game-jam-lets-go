#import keyboard
import time
import os

player_health = 1000
player_money = 100
player_sanity = "good :)"
player_time = "7:00 PM"
# need to implement different menu types. travel, combat, and dialogue
player_name = "asdsadsadsdasdsaaddsd"
menu_name = f"""╔═{'═'*len(player_name)}═╗
║ {player_name.upper()} ║
╚═{'═'*len(player_name)}═╝"""
menu_dialogue = f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║                                        ..                                      ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║                                                                                ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║                                                                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║                                                                                ║ DRIP:     NONE     ║
║    |_____/     ║                                                                                ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝"""



def draw_menu_dialogue(line, text):
    print("hi")
print(menu_name)
print(menu_dialogue)

