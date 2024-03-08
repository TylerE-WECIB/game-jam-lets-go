import os
import time
import random

os.system('cls')
# player variables
player_health = 10 # Health of Player
player_position = 0 # Position of Player in menu list
player_money = 100 # money to buy stuff
player_sanity = 10 # sanity level from Mary's code
player_time = "7:00 PM" # Time of day if we can implement that, if not it's unimportant
battle_type = 1
player_name = input("Who are ya? ")
time.sleep(1)
os.system('cls')

fight_rat = [9, 15]
fight_new_yorker = [11, 20]
fight_wise_guy = [2]

# menu for playername box
menu_name = f"""╔═{'═'*len(player_name)}═╗
║ {player_name.upper()} ║
╚═{'═'*len(player_name)}═╝"""

#menu when going  around city
menu_travel = []

def update_menu_travel():
    return [
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [YOU][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][YOU][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][YOU][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][YOU][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][YOU]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [YOU][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][YOU][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][YOU][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][YOU][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][YOU]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [YOU][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][YOU][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][YOU][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][YOU][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][YOU]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [YOU][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][YOU][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][YOU][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][YOU][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][YOU]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [YOU][   ][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][YOU][   ][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][YOU][   ][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][YOU][   ]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝""",
f"""╔════════════════╦════════════════════════════════════════════════════════════════════════════════╦════════════════════╗
║   .-------.    ║   [   ][   ][ * ][   ][   ]                 up                                 ║ HEALTH:   {str(player_health) + " "*(9-len(str(player_health)))}║
║   | 0   0 |    ║   [   ][   ][   ][   ][   ]            left    right                           ║ MONEY:    {str(player_money) + " "*(9-len(str(player_money)))}║
║  (|    >  |    ║   [   ][   ][   ][   ][   ]                down                                ║ SANITY:   {str(player_sanity) + " "*(9-len(str(player_sanity)))}║
║   |  ___  /    ║   [   ][   ][   ][   ][   ]                                                    ║ DRIP:     NONE     ║
║    |_____/     ║   [   ][   ][   ][   ][YOU]                                                    ║ TIME:     {str(player_time) + " "*(9-len(str(player_time)))}║
╚════════════════╩════════════════════════════════════════════════════════════════════════════════╩════════════════════╝"""]

menu_travel = update_menu_travel()

def draw_menu_travel(pos, clear = True):
    if clear:
        os.system('cls')
    print(menu_name)
    print(menu_travel[pos])

def fight(player_health, enemy_health, battle):
    global player_money
    screens = [f"""╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  RAT DIMENSION: FAT RAT                                                                                              ║
║                                                                  <-__--------______                                  ║
║                                                                  _____‾‾‾‾‾-->     ‾‾‾‾--_                           ║
║                                                         __-- ‾ ‾       ____________       |                          ║
║                                                       /‾  ___---‾‾‾‾‾‾‾            ‾‾‾‾‾‾‾                           ║
║                                                      |  \\‾__------‾‾‾‾‾‾‾‾‾---_                                      ║
║                                                       \\  /                      \\        _                           ║
║                                                       /                   ___     \\    /  |                          ║
║                                                      |                   |    \\ _-------__|                          ║
║                                                      |                   \\  _ ‾           |                          ║
║                                                      \\            __‾‾\\   \\/    ‾-__    / |                          ║
║                                                       \\      ___/‾     \\   -_     O ‾    O |   /                     ║
║                                                     /  |_\\_ <____‾‾-_ /      ‾‾--__        _\\/                       ║
║                                                     |/\\_\\\\  ‾-__ \\/\\/         ___  ‾‾--___ |_|---‾                   ║
║                                                                 ‾‾‾‾---------\\    |  ‾‾   /                          ║
║                                                                              /|/\\/\\|    /                            ║
║                                                                                                                      ║
║ PUNCH IT!                                                                                                            ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝""",
               f"""╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  THE STREETS: NEW YORKER                                                _-‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾--__                     ║
║                                                                       |                         |                    ║
║                                                                      | ----   /‾\\/‾\\  |\\  | \\ /  |                   ║
║                                                                     |    |    \\    /  | \\ |  |    |                  ║
║                                                                    |   ----     \\/    |  \\|  |    |                  ║
║                                                                  __┴------------------------------┴__                ║
║                                                                 |      |      |      |       |       |               ║
║                                                                 |      |      |      |       |       |               ║
║                                                                |-------------------------------------|  EY I'M       ║
║                                                                 ---|   --_                 _--    |     WALKIN       ║
║                                                                |   |      ‾‾--_        _-‾‾      |‾‾|   HERE!        ║
║                                                                 \\   |       0  ‾‾    ‾‾ 0       /   /                ║
║                                                                   \\ |               |          /   /                 ║
║                                                                      \\              _>         /‾‾                   ║
║                                                                       \\                      /                       ║
║                                                                        --_     /‾‾‾‾\\      _-                        ║
║                                                                         /  --__________ --|                          ║
║ PUNCH HIM!                                                              |                 |                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝""",
               f"""╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  GROCERY STORE: WISE GUY                                         ---------------__                                   ║
║                                                               /‾‾  _____-----_    ‾‾-_                               ║
║                                                               \\ --‾            \\      \\                              ║
║                                                               /                 |       \\                            ║
║                         EY CHUMP! RIDDLE ME THIS             /  ---‾‾‾‾          \\      |_                           ║
║                                                              | ----‾‾  _______    \\  /‾| \\|                          ║
║                   WHAT WALKS ON 4 LEGS IN DA MORNIN'         |____  -/ --0---/     \\/  > >|                          ║
║                 2 LEGS IN DA AFTANOON, AND 3 AT NIGHT?        | 0 |     ‾‾‾‾     /    | / |                          ║
║                                                                |  |     -       /     |--|                           ║
║                    YOU'LL BE SWIMMIN' WITH DA FISHIES          |  |  /--  \\           | /                            ║
║                        IF YA CAN'T ANSA DIS ONE!                |  ‾‾ =====           |‾‾-.  /‾‾\\                    ║
║                                                                  |  /-‾‾‾‾--\\       /‾‾\\   \\  \\   \\                  ║
║                                                                   |                 \\   \\   \\  \\   \\                 ║
║                                                                     ‾-_       __-‾‾‾ \\   \\   \\  \\   \\      ___       ║
║                                                      _------------/‾‾‾ ‾‾‾‾‾‾        _\\   \\   \\  \\   \\   /‾  /       ║
║                                                     /                               |  \\‾‾ \\   v/     \\ |   |        ║
║                                                    /                 .‾‾‾‾‾‾‾‾‾‾‾‾‾‾\\  \\‾‾‾            \\/   |        ║
║                                                   |                 /              /                       |         ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝""",]

    if battle == 1:
        os.system('cls')
        print(f"YOU: {player_health} ENEMY: {enemy_health}")
        print(screens[0])
        while True:
            #player turn
            choice = input(": ")
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
                    print(screens[0])
                    print("YOU WIN!")
                    time.sleep(2)
                    return "win"

            #handling invalid input
            else:
                print("invalid")
                time.sleep(1)
                os.system('cls')
                print(f"YOU: {player_health} ENEMY: {enemy_health}")
                print(screens[0])
                continue

             #rat turn
            print(f"YOU: {player_health} ENEMY: {enemy_health}")
            print(screens[0])
            print("THE RAT BITES YOU!")
            damage = random.randint(0, 5)
            time.sleep(1)
            print(f"DEALT {damage} DAMAGE!")
            player_health -= damage
            time.sleep(1)
            os.system('cls')
            print(f"YOU: {player_health} ENEMY: {enemy_health}")
            print(screens[0])

            if player_health <= 0:
                player_health = 0
                os.system('cls')
                print(f"YOU: {player_health} ENEMY: {enemy_health}")
                print(screens[0])
                print("YOU LOSE!")
                time.sleep(2)
                return "lose"

    if battle == 2:
        os.system('cls')
        print(f"YOU: {player_health} ENEMY: {enemy_health}")
        print(screens[1])
        while True:
            #player turn
            choice = input(": ")
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
                    print(screens[1])
                    print("YOU WIN!")
                    time.sleep(2)
                    print("YOU GOT $50!")
                    time.sleep(2)
                    return "win"

            #handling invalid input
            else:
                print("invalid")
                time.sleep(1)
                os.system('cls')
                print(f"YOU: {player_health} ENEMY: {enemy_health}")
                print(screens[1])
                continue

             #new yorker turn
            print(f"YOU: {player_health} ENEMY: {enemy_health}")
            print(screens[1])
            print("NEW YORKER STABS YOU")
            damage = random.randint(0, 10)
            time.sleep(1)
            print(f"DEALT {damage} DAMAGE!")
            player_health -= damage
            time.sleep(1)
            os.system('cls')
            print(f"YOU: {player_health} ENEMY: {enemy_health}")
            print(screens[1])

            if player_health <= 0:
                player_health = 0
                os.system('cls')
                print(f"YOU: {player_health} ENEMY: {enemy_health}")
                print(screens[1])
                print("YOU LOSE!")
                time.sleep(2)
                return "lose"
    if battle == 3:
        while True:
            #wise guy fight
            os.system('cls')
            print(f"YOU: {player_health} ENEMY: {enemy_health}")
            print(screens[2])
            choice = input("ANSWER THE RIDDLE!: ")
            if "man" not in choice:
                damage = random.randint(1,4)
                print("WRONG BOZO!")
                time.sleep(1)
                print(f"TOOK {damage} DAMAGE!")
                player_health -= damage
                time.sleep(1)

                if player_health <= 0:
                    player_health = 0
                    os.system('cls')
                    print(f"YOU: {player_health} ENEMY: {enemy_health}")
                    print(screens[2])
                    print("YOU LOSE!")
                    time.sleep(2)
                    return "lose"
            else:
                print("NO WAY!")
                time.sleep(1)
                print("YOU WIN!")
                time.sleep(2)
                return "win"



# olivia's movement code and game loop
draw_menu_travel(player_position)

travelling = True

while travelling:
    # checking for fights
    if player_position in fight_rat:
        if fight(player_health, 10, 1) == "win":
            fight_rat.remove(player_position)
        else:
            os.system('cls')
            player_position = 0
    elif player_position in fight_new_yorker:
        if fight(player_health, 15, 2) == "win":
            player_money += 50
            menu_travel = update_menu_travel()
            fight_new_yorker.remove(player_position)
        else:
            player_position = 0
    elif player_position in fight_wise_guy:
        if fight(player_health, 1000, 3) == "win":
            fight_wise_guy.remove(player_position)
        else:
            player_position = 0
    os.system('cls')
    draw_menu_travel(player_position)
    if player_position == 2 and player_position not in fight_wise_guy:
        if player_money < 200:
            print("I need $200...")
        else:
            break
    try:

        o=input(": ")
        if o.lower() =="right" and player_position not in [4, 9, 14, 19 ,24]:
            os.system('cls')
            player_position += 1
            draw_menu_travel(player_position)

        elif o.lower()=="left" and player_position not in [0,5,10,20]:
            os.system('cls')

            player_position -= 1
            draw_menu_travel(player_position)

        elif o.lower()=="down" and player_position not in [20,21,22,23,24]:
            os.system('cls')

            player_position += 5
            draw_menu_travel(player_position)

        elif o.lower()=="up" and player_position not in [0,1,2,3,4]:
            os.system('cls')

            player_position -= 5
            draw_menu_travel(player_position)


        else:
            print("try again:")
    except:
        print("can't go there")

os.system('cls')

# mary 2nd part begins here
print("end")