#import keyboard
import time
import os

player_health = 1000
player_money = 100
player_sanity = 10
player_time = "7:00 PM"
player_position = 0
# need to implement different menu types. travel, combat, and dialogue
player_name = "Tyler"
menu_mode = "travel"

# menu for playername box
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

#menu when going around city
menu_travel = [
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

menu_screen = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# talk function for dialogue bits
def talk(words, speed=0.05, newline=False, delay_to_next=1):
    for letters in words:
        print(letters, end="")
        time.sleep(speed)

    if newline is True:
        print("\n", end="")
    time.sleep(delay_to_next)

# matches menu sprite index to player position variable. screen should also match
def draw_menu_travel(position = player_position):
    print(menu_travel[position])
def draw_menu_screen(position = player_position):
    print(menu_screen[position])

draw_menu_screen()
draw_menu_travel()