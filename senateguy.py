# It's senating time >:]

import time, keyboard, os

os.system("")
lives = 4  # lives in the game

# Line1 = 234, Line2 = 386, Line3 = 538


class Person:  # The people in congress talking and stuff.
    def __init__(self, speech_box):
        self.ui = speech_box
        self.base_ui = speech_box

    def reset_ui(self):  # clears the ui so someone can talk again.
        self.ui = self.base_ui[:]

    def speak(self, words, line=1, speed=0.05, pause_speed=0.5, start_delay=0.5,
              end_delay=0.5):  # printing text in the box like the character is speaking
        if line == 1:
            line_start = 234
        elif line == 2:
            line_start = 386
        elif line == 3:
            line_start = 538
        else:
            return "Error. Line out of range. you have like half a tweet to make it work bozo do better."
        print(self.ui)
        time.sleep(start_delay)
        for letters in range(len(words)):
            print('\033[12A\033[2K',
                  end='')  # ANSI escape sequence. idk how this works but it clears the screen better than os
            self.ui = self.ui[:line_start + letters] + words[letters] + self.ui[line_start + letters + 1:]
            print(self.ui)
            time.sleep(speed)
            if words[letters] in "!.?,":
                time.sleep(pause_speed)
        time.sleep(end_delay)
        print('\033[12A\033[2K', end='')


# Dialogue Templates ‾

# ╔════════════════════════════╗
# ║ GARY CONGRESSGUY           ║
# ╠═════════════════╦══════════╩════════════════════════════════════════════╗
# ║  ____________^  ║                                                       ║
# ║ /             | ║ this is some placeholder dialogue                     ║
# ║ |---__________/ ║                                                       ║
# ║ |  ==    ==  |  ║ i can talk on 3 lines and at different speeds         ║
# ║ |     oo     |  ║                                                       ║
# ║ |   /----\   |  ║ this is a yuge development                            ║
# ║  \__________/   ║                                                       ║
# ║                 ║                                                       ║
# ╚═════════════════╩═══════════════════════════════════════════════════════╝


title = """\n                                         $$\\
                                         $$ |
 $$$$$$$\\  $$$$$$\\  $$$$$$$\\   $$$$$$\\ $$$$$$\\    $$$$$$\\         $$$$$$\\  $$\\   $$\\ $$\\   $$\\
$$  _____|$$  __$$\\ $$  __$$\\  \\____$$\\\\_$$  _|  $$  __$$\\       $$  __$$\\ $$ |  $$ |$$ |  $$ |
\\$$$$$$\\  $$$$$$$$ |$$ |  $$ | $$$$$$$ | $$ |    $$$$$$$$ |      $$ /  $$ |$$ |  $$ |$$ |  $$ |
 \\____$$\\ $$   ____|$$ |  $$ |$$  __$$ | $$ |$$\\ $$   ____|      $$ |  $$ |$$ |  $$ |$$ |  $$ |
$$$$$$$  |\\$$$$$$$\\ $$ |  $$ |\\$$$$$$$ | \\$$$$  |\\$$$$$$$\\       \\$$$$$$$ |\\$$$$$$  |\\$$$$$$$ |
\\_______/  \\_______|\\__|  \\__| \\_______|  \\____/  \\_______|       \\____$$ | \\______/  \\____$$ |
                                                                 $$\\   $$ |          $$\\   $$ |
       By Tyler Ellis   May 12th 2023                            \\$$$$$$  |          \\$$$$$$  |      /‾‾‾‾‾‾‾‾\\
                                                                  \\______/            \\______/      | o        |
       Hit Enter!      (Play in Fullscreen)                                                         |        o |
                                                                                                    |   ---    |
                                                                                                     \\________/"""

senate_room = f"""
                        ┌─o─┐ ││┌o─┐  ( )     ( )  ┌─o┐││┌─o─┐
                        └───┘ ││└──┘  ││       ││  └──┘││└───┘
                              ││┌o─┐  ││       ││  ┌o─┐││
 [o]   [o]     [o]    [o]     ││└──┘  \\\\┌──o──┐//  └──┘││      [o]   [o]    [o]    [o]
 [o]   [o]            [o]     ││        └─────┘        ││      [o]   [o]    [o]    [o]
              [o]             \\\\_┌──o─┬─o──┬──o─┬──o─┐ //     [o]    [o]    [o]    [o]
 [o]    [o]           [o]      ‾‾└────┴────┴────┴────┘‾‾     [o]     [o]    [o]    [o]
         [o]   [o]     [o]      ┌─────────┐  ┌────────┐             [o]    [o]
  [o]            [o]            └─────────┘  └────────┘     [o]            [o]     [o]
                          [o]                                    [o]             [o]
            [o]     [o]       [o]                      [o]     [o]
     [o]     [o]      [o]        [o]   [o]  [o]    [o]      [o]        [o]
       [o]      [o]      [o]                              [o]      [o][o]    [o]
         [o]      [o]        [o]  [o]            [o] [o]         [o]       [o]
           [o]       [o]               [o]   [o]              [o]        [o]
               [o]          [o]                          [o]        [o] [o]
                 [o]          [o] [o]       [o] [o][o][o]         [o]
                                      [o]
                        [o][o]                        [o][o][o]
                               [o] [o] [o]    [o] [o][o]"""

print(title)
debug = input()
time.sleep(0.1)
for i in range(2):
    os.system('cls')
    time.sleep(0.08)
    print(title)
    time.sleep(0.08)
time.sleep(0.6)
print('\033[1000A\033[2K', end='')
for i in range(15):
    print(" " * 130)
    time.sleep(0.05)
print('\033[1000A\033[2K', end='')
time.sleep(1)
if debug != "debug":
    name = input("Who are ya?: ")
    time.sleep(1)
else:
    name = "debug"
os.system('cls')
time.sleep(1)
print(senate_room)

you = Person(f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║                                                       ║
║ |         O  |  ║                                                       ║
║ | O          |  ║                                                       ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")

jerry_m = Person("""╔════════════════════════════╗
║ JERRY M.            MAJ.L  ║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║  ____________^  ║                                                       ║
║ /             | ║                                                       ║
║ |---__________/ ║                                                       ║
║ |  ==    ==  |  ║                                                       ║
║ |     oo     |  ║                                                       ║
║ |   /----\   |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")
jim = Person("""╔════════════════════════════╗
║ JIM GARRISON             R ║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║                                                       ║
║ | ____  --__ |  ║                                                       ║
║ | ┌──┐__┌──┐ |  ║                                                       ║
║ | └──┘/\└──┘ |  ║                                                       ║
║ | ~~      ~~ |  ║                                                       ║
║  \  /____\  /   ║                                                       ║
║   \________/    ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")
ron = Person("""╔════════════════════════════╗
║ RON JEFFREY              R ║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║   __________    ║                                                       ║
║  /          \   ║                                                       ║
║ |/‾‾-____-‾‾\|  ║                                                       ║
║ | \__    __/ |  ║                                                       ║
║ |   O |  O   |  ║                                                       ║
║ |      >     |  ║                                                       ║
║  \   ----   /   ║                                                       ║
║   \________/    ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")
abigail = Person("""╔════════════════════════════╗
║ ABIGAIL MCDAVIDSON       D ║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║        _____    ║                                                       ║
║  ____/‾     \   ║                                                       ║
║ /            \  ║                                                       ║
║|__/‾‾‾‾\_     | ║                                                       ║
║ |- ==    \    | ║                                                       ║
║ \ --  >  -\__/  ║                                                       ║
║  \-/>----<\-/   ║                                                       ║
║   ‾‾‾‾‾‾‾‾‾‾    ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")
marquez = Person("""╔════════════════════════════╗
║ MARQUEZ DE LA CRUZ       D ║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║   __________    ║                                                       ║
║  /          \   ║                                                       ║
║ | ---      / |  ║                                                       ║
║ |  O  \  ███ |  ║                                                       ║
║ |     _> /   |  ║                                                       ║
║  |  --- /   |   ║                                                       ║
║   \    /   /    ║                                                       ║
║    ‾‾‾‾‾‾‾‾     ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")
old_man_mgee = Person("""╔════════════════════════════╗
║ OLD MAN MGEE             D ║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾ \   ║                                                       ║
║ /\  ======  /\  ║                                                       ║
║ || __    __ ||  ║                                                       ║
║ |/    <     \|  ║                                                       ║
║  |   ----   |   ║                                                       ║
║   \        /    ║                                                       ║
║    ‾‾‾‾‾‾‾‾     ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")
goku = Person("""╔════════════════════════════╗
║ SON G.                   I ║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║        ‾‾‾‾‾‾\  ║                                                       ║
║               \_║                                                       ║
║    /‾‾/   /‾-.  ║                                                       ║
║\|\|-__| /_-- |  ║                                                       ║
║‾| | o|  |o | |‾|║                                                       ║
║\|      >     |/_║                                                       ║
║ ‾\    ‾‾    /‾‾ ║                                                       ║
║    \______/     ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")
if debug != "debug":
    jerry_m.speak("Alright fellas, new bill! This one is yuge.", 1)
    jerry_m.speak("The greatest bill in American history. SB-7001.", 2, end_delay=0.5, start_delay=0)
    jerry_m.reset_ui()
    jerry_m.speak("We're banning the internet.", 1, 0.1, 0.5, 1, 1)
    you.speak("Huh???",pause_speed=0, start_delay=1.5)

game_ui = [f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ LISTEN ]                  [ CALL PRESIDENT ]      ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ COUNTERARGUMENT ]         [ ARG. ESSAY ]          ║
║ |            |  ║                                                       ║
║ |   ----     |  ║   [ FILIBUSTER ]              [ GIVE UP ]             ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
""",
           f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║  >[ LISTEN ]<                 [ CALL PRESIDENT ]      ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ COUNTERARGUMENT ]         [ ARG. ESSAY ]          ║
║ |            |  ║                                                       ║
║ |   ----     |  ║   [ FILIBUSTER ]              [ GIVE UP ]             ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Listen up!                                                                 """,
           f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ LISTEN ]                 >[ CALL PRESIDENT ]<     ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ COUNTERARGUMENT ]         [ ARG. ESSAY ]          ║
║ |            |  ║                                                       ║
║ |   ----     |  ║   [ FILIBUSTER ]              [ GIVE UP ]             ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
It's vetoin' time.                                                         """,
           f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ LISTEN ]                  [ CALL PRESIDENT ]      ║
║ |         O  |  ║                                                       ║
║ | O          |  ║  >[ COUNTERARGUMENT ]<        [ ARG. ESSAY ]          ║
║ |            |  ║                                                       ║
║ |   ----     |  ║   [ FILIBUSTER ]              [ GIVE UP ]             ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
OBJECTION!                                                                 """,
           f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ LISTEN ]                  [ CALL PRESIDENT ]      ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ COUNTERARGUMENT ]        >[ ARG. ESSAY ]<         ║
║ |            |  ║                                                       ║
║ |   ----     |  ║   [ FILIBUSTER ]              [ GIVE UP ]             ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Write good. Great for convincing people.                                   """,
           f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ LISTEN ]                  [ CALL PRESIDENT ]      ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ COUNTERARGUMENT ]         [ ARG. ESSAY ]          ║
║ |            |  ║                                                       ║
║ |   ----     |  ║  >[ FILIBUSTER ]<             [ GIVE UP ]             ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Talk but like a lot. That'll stop em for sure.                             """,
           f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ LISTEN ]                  [ CALL PRESIDENT ]      ║
║ | ___    ___ |  ║                                                       ║
║ |  O      O  |  ║   [ COUNTERARGUMENT ]         [ ARG. ESSAY ]          ║
║ |            |  ║                                                       ║
║ |   ------   |  ║   [ FILIBUSTER ]             >[ GIVE UP ]<            ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Don't!                                                                     """,
           f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ LISTEN ]                  [ CALL PRESIDENT ]      ║
║ | ___    ___ |  ║                                                       ║
║ |  O      O  |  ║   [ COUNTERARGUMENT ]         [ ARG. ESSAY ]          ║
║ |            |  ║                                                       ║
║ |   ------   |  ║   [ FILIBUSTER ]              [ GIVE UP ]             ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Don't!                                                                     """,
]

correct_counter = 0 # correct counterargument
correct_case = 0 # correct case for question
should_argue = False # message for if you should counterargue
listen_over = False # when the listen process stops
game_end = False  # game over and stuff
def listen():
    global correct_counter
    global should_argue
    global listen_over
    # 1
    jim.reset_ui()
    jim.speak("Well the contents of the bill say that we're banning", end_delay=0)
    jim.speak("the internet until we replace it. What we need is", 2, start_delay=0, end_delay=0)
    jim.speak("something more heavily [regulated].", 3, start_delay=0, end_delay=1)

    ron.reset_ui()
    ron.speak("True! So much [commerce] happens online. That hurts", end_delay=0)
    ron.speak("local businesses. How can they compete with Amazon?", 2,start_delay=0, end_delay=0)
    ron.speak("We gotta pass this bill now!",3,start_delay=0)

    correct_counter = 1
    should_argue = True
    print_game_ui(False)
    yield
    abigail.reset_ui()
    abigail.speak("We should go forward with this one. [Social media] is",end_delay=0)
    abigail.speak("a problem. These youngins are being infuenced by ",2,start_delay=0, end_delay=0)
    abigail.speak("other countries!",3,start_delay=0,end_delay=1)
    abigail.reset_ui()
    abigail.speak("I'd say it's a [clear and present danger] to the",end_delay=0)
    abigail.speak("security of our nation!",2,start_delay=0,end_delay=1)

    marquez.reset_ui()
    marquez.speak("Disagree.")

    old_man_mgee.reset_ui()
    old_man_mgee.speak("Nah she's right.")
    correct_counter = 3
    should_argue = True
    print_game_ui(False)
    yield

    old_man_mgee.reset_ui()
    old_man_mgee.speak("I still think getting rid of social media",end_delay=0)
    old_man_mgee.speak("would be great! It's not even useful!",2,start_delay=0)
    old_man_mgee.speak("It just poisons the youth!",3)

    ron.reset_ui()
    ron.speak("Nah I can't agree with that one.")

    marquez.reset_ui()
    abigail.reset_ui()
    abigail.speak("I can! He's absolutely correct.")
    abigail.speak("How does it help me or my voters at all?",2)
    abigail.speak("Get rid of it.",3)
    correct_counter = 2

    should_argue = True
    print_game_ui(False)
    listen_over = True
    yield

hearing = listen()

counter_arguments = [f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ COMMERCE CLAUSE ]      [ LINKAGE INSTITUTION ]    ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ FREE SPEECH ]          [ BACK ]                   ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Pick the relevant one!                                                     """,
                     f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║  >[ COMMERCE CLAUSE ]<     [ LINKAGE INSTITUTION ]    ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ FREE SPEECH ]          [ BACK ]                   ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Pick the relevant one!                                                     """,
                     f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ COMMERCE CLAUSE ]     >[ LINKAGE INSTITUTION ]<   ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ FREE SPEECH ]          [ BACK ]                   ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Pick the relevant one!                                                     """,
                     f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ COMMERCE CLAUSE ]      [ LINKAGE INSTITUTION ]    ║
║ |         O  |  ║                                                       ║
║ | O          |  ║  >[ FREE SPEECH ]<         [ BACK ]                   ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Pick the relevant one!                                                     """,
                     f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ COMMERCE CLAUSE ]      [ LINKAGE INSTITUTION ]    ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ FREE SPEECH ]         >[ BACK ]<                  ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Pick the relevant one!                                                     """
]
cases = [f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ MARBURY V. MADISON ]   [ US V. LOPEZ ]            ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ SHENCK V. US ]         [ PLESSY V. FERGUSON ]     ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Defend your case with a case!                                              """,
         f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║  >[ MARBURY V. MADISON ]<  [ US V. LOPEZ ]            ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ SHENCK V. US ]         [ PLESSY V. FERGUSON ]     ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Defend your case with a case!                                              """,
         f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ MARBURY V. MADISON ]  >[ US V. LOPEZ ]<           ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ SHENCK V. US ]         [ PLESSY V. FERGUSON ]     ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Defend your case with a case!                                              """,
         f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ MARBURY V. MADISON ]   [ US V. LOPEZ ]            ║
║ |         O  |  ║                                                       ║
║ | O          |  ║  >[ SHENCK V. US ]<        [ PLESSY V. FERGUSON ]     ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Defend your case with a case!                                              """,
         f"""╔════════════════════════════╗
║ {name.upper()}{" " * (27 - len(name))}║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║   [ MARBURY V. MADISON ]   [ US V. LOPEZ ]            ║
║ |         O  |  ║                                                       ║
║ | O          |  ║   [ SHENCK V. US ]        >[ PLESSY V. FERGUSON ]<    ║
║ |            |  ║                                                       ║
║ |   ----     |  ║                                                       ║
║  \__________/   ║                                                       ║
║                 ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝
Defend your case with a case!                                              """
]
phone = Person("""╔════════════════════════════╗
║ PHONE                      ║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║  /‾‾‾‾‾‾‾‾‾‾\   ║                                                       ║
║ | ┌────────┐ |  ║                                                       ║
║ | │(P)~~~~ │ |  ║                                                       ║
║ | │1 2 3 # │ |  ║                                                       ║
║ | │4 5 6 - │ |  ║                                                       ║
║ | │7 8 9 0 │ |  ║                                                       ║
║ | └───━━───┘ |  ║                                                       ║
║  \__________/   ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")
preston = Person("""╔════════════════════════════╗
║ PRESTON E. DENT            ║
╠═════════════════╦══════════╩════════════════════════════════════════════╗
║                 ║                                                       ║
║  /‾‾‾‾‾‾‾‾‾‾\   ║                                                       ║
║ |/‾‾‾‾‾‾‾‾‾‾\|  ║                                                       ║
║ | ___    ___ |  ║                                                       ║
║ |  ==    ==  |  ║                                                       ║
║ |   / || \   |  ║                                                       ║
║  \   _--_   /   ║                                                       ║
║   \________/    ║                                                       ║
╚═════════════════╩═══════════════════════════════════════════════════════╝""")
# Ok it's time for the actual game!
lose = False

keypress = lambda button: keyboard.is_pressed(button)
will_veto = False # if the president is going to veto
selection = 1  # menu movement
counter_selection = 1  # counter argument menu movement
case_selection = 1  # case menu movement


print(game_ui[1])


def print_game_ui(go_back=True):
    if go_back is True:
        print('\033[13A\033[2K', end='')
    print('\033[1A\033[2K', end='')
    print(f"Lives: {'▌'*lives}")
    print(game_ui[selection])


def print_counter_ui(go_back=True):
    if go_back is True:
        print('\033[13A\033[2K', end='')
    print('\033[1A\033[2K', end='')
    print(f"Lives: {'▌' * lives}")
    print(counter_arguments[counter_selection])


def print_case_ui(go_back=True):
    if go_back is True:
        print('\033[13A\033[2K', end='')
    print('\033[1A\033[2K', end='')
    print(f"Lives: {'▌' * lives}")
    print(cases[case_selection])

def change_life(number):
    global lives
    lives += number
    if lives < 0:
        lives = 0
    if lives > 4:
        lives = 4


print_game_ui()
while True:
    if game_end is True:
        break
    if lives == 0:
        lose = True
        break
    if keypress("left arrow") and selection - 1 > 0:
        selection -= 1
        print_game_ui()
        while keypress("left arrow"):
            pass
    if keypress("right arrow") and selection + 1 < 7:
        selection += 1
        print_game_ui()
        while keypress("right arrow"):
            pass
    if keypress("up arrow") and selection - 2 > 0:
        selection -= 2
        print_game_ui()
        while keypress("up arrow"):
            pass
    if keypress("down arrow") and selection + 2 < 7:
        selection += 2
        print_game_ui()
        while keypress("down arrow"):
            pass
    if keypress("enter"):
        input()
        print('\033[1A\033[2K', end='')
        choice = selection
        if choice == 6:
            selection = 7
        else:
            selection = 0
        print_game_ui()
        time.sleep(0.1)
        selection = choice
        print_game_ui()
        time.sleep(0.3)
        if selection == 1:
            print('\033[13A\033[2K', end='')
            if should_argue is True:
                you.reset_ui()
                you.speak("(I should say something.)",pause_speed=0)
                print_game_ui(False)
            elif listen_over is False:
                next(hearing)
            else:
                break

        elif selection == 2:
            print('\033[13A\033[2K', end='')
            phone.reset_ui()
            phone.speak('Calling "Mr. President"',pause_speed=0)
            #print('\033[12A\033[2K', end='')
            for i in range(5):
                phone.reset_ui()
                print(phone.ui)
                print('\033[12A\033[2K', end='')
                phone.speak("....................",1,pause_speed=0,end_delay=0,start_delay=0)
            phone.reset_ui()
            phone.speak("beep")
            preston.reset_ui()
            preston.speak("Hello? How did you get my number",end_delay=0)
            you.reset_ui()
            you.speak("Hey sir things are looking bad! ",start_delay=0)
            you.speak("I need you to veto this bill.",2,start_delay=0)
            preston.reset_ui()
            preston.speak("?? Who are you",end_delay=0)
            you.reset_ui()
            you.speak("No time! We gotta veto it!",speed=0.02)
            preston.reset_ui()
            preston.speak("Alright, but im gonna need something from you.")
            preston.speak("Look at this opinion poll! My ratings are tanking!",2)
            os.system('cls')
            print("""How would you rate President Dent?

                Other
                0.7%

                   ░██████████████
                ▓▓▓░██████████████████
He's ok     ▓▓▓▓▓▓▓░██████████████████████
18%       ▓▓▓▓▓▓▓▓▓░████████████████████████
        ▓▓▓▓▓▓▓▓▓▓▓▓░█████████████████████████
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░██████████████████████████
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░█████████████████████████
    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░██████████████████████████
    ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░█████████████████████████
  ██████████▓▓▓▓▓▓▓▓▓▓▓▓▓░██████████████████████████
  ███████████████▓▓▓▓▓▓▓▓░██████████████████████████
  █████████████████████▓▓░██████████████████████████
  ██████████████████████████████████████████████████  Hate him
  ██████████████████████████████████████████████████  81.3%
  ██████████████████████████████████████████████████
  ██████████████████████████████████████████████████
    ██████████████████████████████████████████████
    ██████████████████████████████████████████████
      ██████████████████████████████████████████
      ██████████████████████████████████████████
        ██████████████████████████████████████
          ██████████████████████████████████
            ██████████████████████████████
                ██████████████████████
                    ██████████████""")
            time.sleep(5)
            os.system('cls')
            print(senate_room)
            preston.speak("How can I advertise this veto to secure my reelection?",3,end_delay=2)
            #print('\033[12A\033[2K', end='')
            print_counter_ui(False)
            while True:
                if keypress("left arrow") and counter_selection - 1 > 0:
                    counter_selection -= 1
                    print_counter_ui()
                    while keypress("left arrow"):
                        pass
                if keypress("right arrow") and counter_selection + 1 < 5:
                    counter_selection += 1
                    print_counter_ui()
                    while keypress("right arrow"):
                        pass
                if keypress("up arrow") and counter_selection - 2 > 0:
                    counter_selection -= 2
                    print_counter_ui()
                    while keypress("up arrow"):
                        pass
                if keypress("down arrow") and counter_selection + 2 < 5:
                    counter_selection += 2
                    print_counter_ui()
                    while keypress("down arrow"):
                        pass
                if keypress("enter"):
                    input()
                    print('\033[1A\033[2K', end='')
                    counter_choice = counter_selection
                    counter_selection = 0
                    print_counter_ui()
                    time.sleep(0.1)
                    counter_selection = counter_choice
                    print_counter_ui()
                    time.sleep(0.3)
                    if counter_selection == 1:
                        you.reset_ui()
                        print('\033[13A\033[2K', end='')
                        you.speak("Talk about the commerce clause? That's important!")
                        preston.reset_ui()
                        preston.speak("I don't think voters would care about that.")
                        print_counter_ui(False)
                    elif counter_selection == 2:
                        you.reset_ui()
                        print('\033[13A\033[2K', end='')
                        you.speak("Mention linkage institutions.")
                        preston.reset_ui()
                        preston.speak("Hey you're right. Voters know they need the internet",end_delay=0)
                        preston.speak("to stay involved. This will boost [public opinion]",2,start_delay=0,end_delay=0)
                        preston.speak("for sure! I'll veto the bill if you lose.",3,start_delay=0)
                        will_veto=True
                    elif counter_selection == 3:
                        you.reset_ui()
                        print('\033[13A\033[2K', end='')
                        you.speak("Just talk about free speech.")
                        preston.reset_ui()
                        preston.speak("You're right! That'll get em on my side.")
                        preston.speak("Ok. I'll veto the bill if you lose.", 2, start_delay=0)
                        will_veto = True
                    if will_veto is True:
                        selection = 0
                        print_game_ui(False)
                        print('\033[1A\033[2K', end='')
                        print("                                         ")
                        print('\033[1A\033[2K', end='')
                        time.sleep(0.3)
                        for letters in "Nice!":
                            print(letters, end="",flush=True)
                            time.sleep(0.05)
                        time.sleep(0.5)
                        for letters in " You got presidential support!":
                            print(letters, end="",flush=True)
                            time.sleep(0.05)
                        time.sleep(0.5)
                        for letters in " Vetos are a check that keep unwanted bills from being passed.":
                            print(letters, end="",flush=True)
                            time.sleep(0.05)
                        time.sleep(1.2)
                        os.system('cls')
                        print(senate_room)
                        selection = 1
                        print_game_ui(False)
                        break
                    if counter_selection == 4:
                        you.reset_ui()
                        print('\033[13A\033[2K', end='')
                        you.speak("uhh...i'll get back to you.")
                        print_game_ui(False)
                        break

        elif selection == 3:
            if correct_counter == 0:
                you.reset_ui()
                print('\033[13A\033[2K', end='')
                you.speak("(I should [ LISTEN ] first.)",pause_speed=0)
                print_game_ui(False)
            else:
                print_counter_ui()
                while True:
                    if keypress("left arrow") and counter_selection - 1 > 0:
                        counter_selection -= 1
                        print_counter_ui()
                        while keypress("left arrow"):
                            pass
                    if keypress("right arrow") and counter_selection + 1 < 5:
                        counter_selection += 1
                        print_counter_ui()
                        while keypress("right arrow"):
                            pass
                    if keypress("up arrow") and counter_selection - 2 > 0:
                        counter_selection -= 2
                        print_counter_ui()
                        while keypress("up arrow"):
                            pass
                    if keypress("down arrow") and counter_selection + 2 < 5:
                        counter_selection += 2
                        print_counter_ui()
                        while keypress("down arrow"):
                            pass
                    if keypress("enter"):
                        input()
                        print('\033[1A\033[2K', end='')
                        counter_choice = counter_selection
                        counter_selection = 0
                        print_counter_ui()
                        time.sleep(0.1)
                        counter_selection = counter_choice
                        print_counter_ui()
                        time.sleep(0.3)
                        if counter_selection != 4:
                            you.reset_ui()
                            os.system('cls')
                            print("""                                 xxx
                                x   x
                               x     x
                               x      x                      xx
      xxx                     x       xx               xxxxx x
       x x xxxx              x         x             xx      x
        x      xxxx         x           x        xxxx
        xx          xxx    x             x   xxxx           x          xxxxxxxxxxxx
         x            xxxxx               xxx               x       xxx          x
          x                                xx               x   xxx             x
           x          ■    ■        ■■■                     xxxx               x
             x       ■    ■       ■    ■        ■     ■■■■■■                   x
           xx       ■■■■■■        ■    ■       ■      ■     ■■               xx
       xxxxx       ■    ■        ■     ■      ■       ■      ■             xx
 xxxxxxx           ■    ■        ■     ■     ■        ■      ■            x
x                 ■    ■         ■     ■     ■        ■      ■              x
xxxxxxx xx        ■    ■          ■■■■■      ■        ■    ■■               x
         xxxxx                               ■■■■■    ■■■■■                 x
             xxxxx         ■■■■■■                                             x
                x            ■        ■■■■■■■                xx               xx
                x           ■■          ■■                    xx                x
              xx         ■■■■■■         ■                     x xx              x
             xx                         ■                     x   xxx            x
            x                           ■      x               x      xxxxxx      x
            x               xxxx               xx              x            xxxx   xx
           x             xxxx  xx             x  xx            x                xxxxx
         xx           xxx       x          xxx     x            x
         x         x x           x       xx          x          x
         x      xxxx              x    xx              x         x
         x    x x                  x  xx                 x       x
        xxxxx                      xxx                    xx     x
                                    x                       xxx  x
                                                               xxx""")
                            time.sleep(2)
                            os.system('cls')
                            print(senate_room)
                            you.reset_ui()
                        if counter_selection == 1:
                            if correct_counter == 1:
                                you.speak("Hey this is unconstitutional!")
                                you.speak("That violates the Commerce Clause!",2)
                                ron.reset_ui()
                                ron.speak("No it doesn't! The Commerce Clause lets congress",end_delay=0)
                                ron.speak("regulate any and all interstate commerce. You fool!",2)
                                you.reset_ui()
                                you.speak("(I should cite a court case.)",end_delay=1,pause_speed=0)
                                print_case_ui(False)
                                while True:
                                    if keypress("left arrow") and case_selection - 1 > 0:
                                        case_selection -= 1
                                        print_case_ui()
                                        while keypress("left arrow"):
                                            pass
                                    if keypress("right arrow") and case_selection + 1 < 5:
                                        case_selection += 1
                                        print_case_ui()
                                        while keypress("right arrow"):
                                            pass
                                    if keypress("up arrow") and case_selection - 2 > 0:
                                        case_selection -= 2
                                        print_case_ui()
                                        while keypress("up arrow"):
                                            pass
                                    if keypress("down arrow") and case_selection + 2 < 5:
                                        case_selection += 2
                                        print_case_ui()
                                        while keypress("down arrow"):
                                            pass
                                    if keypress("enter"):
                                        input()
                                        print('\033[1A\033[2K', end='')
                                        case_choice = case_selection
                                        case_selection = 0
                                        print_case_ui()
                                        time.sleep(0.1)
                                        case_selection = case_choice
                                        print_case_ui()
                                        time.sleep(0.3)
                                        you.reset_ui()
                                        os.system('cls')
                                        print("""                                 xxx
                                x
                               x    xx
                               x      x                      xx
      xxx                     x       xx               xxxxx x
       x x xxxx              x         x             xx      x
        x      xxxx         x           x        xxxx
        xx          xxx    x             x  xxxxx           x          xxxxxxxxxxxx
         x            xxxxx               xxx               x       xxx          x
          x                                xx               x   xxx             x
           x               ■       ■                        xxxx               x
             x            ■■     ■■     ■■    ■■    ■■     ■■                x
           xx            ■■■■    ■■    ■■     ■■    ■■    ■■              xx
       xxxxx            ■■  ■■  ■■    ■■     ■■    ■■    ■■                xx
 xxxxxxx               ■■    ■■■■     ■■    ■■    ■■■■■■■                   x
x                      ■      ■■      ■■   ■■    ■■    ■■                    x
xxxxxxx xx                     ■       ■■■■     ■■    ■■                     x
         xxxxx                                 ■■    ■■                      x
             xxxxx      ■■    ■■     ■■    ■■                                  x
                x      ■■     ■■    ■■   ■■                  xx               xx
                x      ■■    ■■    ■■■■■■■                    xx                x
              xx       ■■   ■■    ■■   ■■                     x xx              x
             xx         ■■■■     ■■   ■■                      x   xxx            x
            x                   ■■   ■■        x               x      xxxxxx      x
            x               xxxx               xx              x            xxxx   xx
           x             xxxx  xx             x  xx            x                xxxxx
         xx           xxx       x          xxx     x            x
         x         x x           x       xx          x          x
         x      xxxx              x    xx              x         x
         x    x x                  x  xx                 x       x
        xxxxx                      xxx                    x      x
                                   xx                       xx  x
                                                               xxx""")
                                        time.sleep(1)
                                        os.system('cls')
                                        print(senate_room)
                                        if case_selection == 2:
                                            you.speak("Commerce Clause doesn't go that far! It's limited.")
                                            you.speak("US v Lopez proved this. You definitely can't",2,end_delay=0)
                                            you.speak("regulate an entire internet.",3,start_delay=0)
                                            jim.reset_ui()
                                            jim.speak("Hmm...you might be right. Intriguing.")
                                            ron.reset_ui()
                                            ron.speak(">:|",end_delay=1)

                                            selection = 0
                                            change_life(1)

                                            print_game_ui(False)
                                            print('\033[1A\033[2K', end='')
                                            print("                                         ")
                                            print('\033[1A\033[2K', end='')
                                            time.sleep(0.3)
                                            for letters in "Good Job!":
                                                print(letters, end="",flush=True)
                                                time.sleep(0.05)
                                            time.sleep(0.5)
                                            for letters in " The US v. Lopez case limits the expression of the Commerce Clause,":
                                                print(letters, end="",flush=True)
                                                time.sleep(0.05)
                                            time.sleep(0.3)
                                            for letters in " and can serve as legal precedent.":
                                                print(letters, end="",flush=True)
                                                time.sleep(0.05)
                                            time.sleep(1.2)
                                            os.system('cls')
                                            print(senate_room)
                                            selection = 1
                                            correct_counter = 0
                                            should_argue = False
                                        elif case_selection == 1:
                                            you.speak("Commerce Clause doesn't go that far! It's limited.")
                                            you.speak("Marbury v Madison proved this. wait no",2,end_delay=0)
                                            you.speak("that doesn't sound right",3,start_delay=0)
                                            ron.reset_ui()
                                            ron.speak("Imagine trying to argue with ME and not even knowing",end_delay=0)
                                            ron.speak("your court cases. Why are you even here?",2,start_delay=0)
                                            change_life(-1)
                                        elif case_selection == 3:
                                            you.speak("Commerce Clause doesn't go that far! It's limited.")
                                            you.speak("Shenck v US proved this. wait no",2,end_delay=0)
                                            you.speak("that doesn't sound right",3,start_delay=0)
                                            ron.reset_ui()
                                            ron.speak("Imagine trying to argue with ME and not even knowing",end_delay=0)
                                            ron.speak("your court cases. Why are you even here?",2,start_delay=0)
                                            change_life(-1)
                                        elif case_selection == 4:
                                            you.speak("Commerce Clause doesn't go that far! It's limited.")
                                            you.speak("Plessy v Ferguson proved this. wait no",2,end_delay=0)
                                            you.speak("that doesn't sound right",3,start_delay=0)
                                            ron.reset_ui()
                                            ron.speak("Imagine trying to argue with ME and not even knowing",end_delay=0)
                                            ron.speak("your court cases. Why are you even here?",2,start_delay=0)
                                            change_life(-1)
                                        break

                                os.system('cls')
                                print(senate_room)
                                print_game_ui(False)
                                break
                            else:
                                you.reset_ui()
                                you.speak("Hey this is unconstitutional!")
                                you.speak("That violates the Commerce Clause!", 2)
                                jerry_m.reset_ui()
                                jerry_m.speak("The Commerce Clause wasn't even in discussion.")
                                jerry_m.speak("Do better.",2)
                                change_life(-1)
                                print_game_ui(False)
                                break

                        elif counter_selection == 2:
                            if correct_counter == 2:
                                you.reset_ui()
                                you.speak("Hey we can't do that. Social media is a linkage ",end_delay=0)
                                you.speak("institution!",2,start_delay=0)
                                old_man_mgee.reset_ui()
                                old_man_mgee.speak("Rats. I forgot. I guess we can't ban it.")
                                marquez.reset_ui()
                                marquez.speak("Agree.")
                                change_life(1)
                                selection = 0
                                print_game_ui(False)
                                print('\033[1A\033[2K', end='')
                                print("                                         ")
                                print('\033[1A\033[2K', end='')
                                time.sleep(0.3)
                                for letters in "Perfect!":
                                    print(letters, end="", flush=True)
                                    time.sleep(0.05)
                                time.sleep(0.5)
                                for letters in " Social Media is a Linkage Institution.":
                                    print(letters, end="", flush=True)
                                    time.sleep(0.05)
                                time.sleep(0.5)
                                for letters in " It's very important for connecting people with the political environment.":
                                    print(letters, end="", flush=True)
                                    time.sleep(0.05)
                                time.sleep(1.2)
                                os.system('cls')
                                print(senate_room)
                                selection = 1
                                correct_counter = 0
                                should_argue = False
                                game_end = True
                                if listen_over is True:
                                    break

                            else:
                                you.reset_ui()
                                you.speak("Hey we can't do that. Social media is a linkage ", end_delay=0)
                                you.speak(" institution!", 2, start_delay=0)
                                jerry_m.reset_ui()
                                jerry_m.speak("You think we care about linkage institutions",end_delay=0)
                                jerry_m.speak("right now? Stay on topic.",2,start_delay=0)
                                change_life(-1)
                                print_game_ui(False)
                                break
                        elif counter_selection == 3:
                            if correct_counter == 3:
                                you.reset_ui()
                                you.speak("Hey! This violates the First Amendment!")
                                you.speak("You can't ignore free speech like that!",2)
                                abigail.reset_ui()
                                abigail.speak("Didn't you hear what I said? This is ",end_delay=0)
                                abigail.speak("a national security threat. Social media is a",2,end_delay=0,start_delay=0)
                                abigail.speak("[clear and present danger].",3,start_delay=0)
                                you.reset_ui()
                                you.speak("(What case was that again?", end_delay=1, pause_speed=0)
                                print_case_ui(False)
                                while True:
                                    if keypress("left arrow") and case_selection - 1 > 0:
                                        case_selection -= 1
                                        print_case_ui()
                                        while keypress("left arrow"):
                                            pass
                                    if keypress("right arrow") and case_selection + 1 < 5:
                                        case_selection += 1
                                        print_case_ui()
                                        while keypress("right arrow"):
                                            pass
                                    if keypress("up arrow") and case_selection - 2 > 0:
                                        case_selection -= 2
                                        print_case_ui()
                                        while keypress("up arrow"):
                                            pass
                                    if keypress("down arrow") and case_selection + 2 < 5:
                                        case_selection += 2
                                        print_case_ui()
                                        while keypress("down arrow"):
                                            pass
                                    if keypress("enter"):
                                        input()
                                        print('\033[1A\033[2K', end='')
                                        case_choice = case_selection
                                        case_selection = 0
                                        print_case_ui()
                                        time.sleep(0.1)
                                        case_selection = case_choice
                                        print_case_ui()
                                        time.sleep(0.3)
                                        you.reset_ui()
                                        os.system('cls')
                                        print("""                                 xxx
                                x
                               x    xx
                               x      x                      xx
      xxx                     x       xx               xxxxx x
       x x xxxx              x         x             xx      x
        x      xxxx         x           x        xxxx
        xx          xxx    x             x  xxxxx           x          xxxxxxxxxxxx
         x            xxxxx               xxx               x       xxx          x
          x                                xx               x   xxx             x
           x               ■       ■                        xxxx               x
             x            ■■     ■■     ■■    ■■    ■■     ■■                x
           xx            ■■■■    ■■    ■■     ■■    ■■    ■■              xx
       xxxxx            ■■  ■■  ■■    ■■     ■■    ■■    ■■                xx
 xxxxxxx               ■■    ■■■■     ■■    ■■    ■■■■■■■                   x
x                      ■      ■■      ■■   ■■    ■■    ■■                    x
xxxxxxx xx                     ■       ■■■■     ■■    ■■                     x
         xxxxx                                 ■■    ■■                      x
             xxxxx      ■■    ■■     ■■    ■■                                  x
                x      ■■     ■■    ■■   ■■                  xx               xx
                x      ■■    ■■    ■■■■■■■                    xx                x
              xx       ■■   ■■    ■■   ■■                     x xx              x
             xx         ■■■■     ■■   ■■                      x   xxx            x
            x                   ■■   ■■        x               x      xxxxxx      x
            x               xxxx               xx              x            xxxx   xx
           x             xxxx  xx             x  xx            x                xxxxx
         xx           xxx       x          xxx     x            x
         x         x x           x       xx          x          x
         x      xxxx              x    xx              x         x
         x    x x                  x  xx                 x       x
        xxxxx                      xxx                    x      x
                                   xx                       xx  x
                                                               xxx""")
                                        time.sleep(1)
                                        os.system('cls')
                                        print(senate_room)
                                        if case_selection == 3:
                                            you.reset_ui()
                                            you.speak("That's not how clear and present danger works.")
                                            you.speak("The ruling of Shenck v US only applies to specific", 2, end_delay=0)
                                            you.speak("threats like propaganda. You can't just apply it to", 3, start_delay=0,end_delay=0)
                                            you.reset_ui()
                                            you.speak("entire social platforms.",start_delay=0)
                                            marquez.reset_ui()
                                            marquez.speak("Agree")
                                            abigail.reset_ui()
                                            abigail.speak("Dagnabit...")

                                            change_life(1)
                                            selection = 0
                                            print_game_ui(False)
                                            print('\033[1A\033[2K', end='')
                                            print("                                         ")
                                            print('\033[1A\033[2K', end='')
                                            time.sleep(0.3)
                                            for letters in "Awesome!":
                                                print(letters, end="", flush=True)
                                                time.sleep(0.05)
                                            time.sleep(0.5)
                                            for letters in " Shenck v. US is an important 1st Amendment case.":
                                                print(letters, end="", flush=True)
                                                time.sleep(0.05)
                                            time.sleep(0.5)
                                            for letters in " It limits free speech by introducing the idea of a \"clear and present danger\".":
                                                print(letters, end="", flush=True)
                                                time.sleep(0.05)
                                            time.sleep(1.2)
                                            os.system('cls')
                                            print(senate_room)
                                            selection = 1
                                            correct_counter = 0
                                            should_argue = False
                                        elif case_selection == 1:
                                            you.reset_ui()
                                            you.speak("That's not how clear and present danger works.")
                                            you.speak("The ruling of Marbury v Madison only...", 2, end_delay=0)
                                            you.speak("Wait, something feels wrong", 3, start_delay=0, end_delay=0)
                                            abigail.reset_ui()
                                            abigail.speak("That aint even the right case!")
                                            abigail.speak("And you call yourself a senator? Shameful.",2)
                                            change_life(-1)
                                        elif case_selection == 2:
                                            you.reset_ui()
                                            you.speak("That's not how clear and present danger works.")
                                            you.speak("The ruling of US v Lopez only...", 2, end_delay=0)
                                            you.speak("Wait, something feels wrong", 3, start_delay=0, end_delay=0)
                                            abigail.reset_ui()
                                            abigail.speak("That aint even the right case!")
                                            abigail.speak("And you call yourself a senator? Shameful.", 2)
                                            change_life(-1)
                                        elif case_selection == 4:
                                            you.reset_ui()
                                            you.speak("That's not how clear and present danger works.")
                                            you.speak("The ruling of Plessy v Ferguson only...", 2, end_delay=0)
                                            you.speak("Wait, something feels wrong", 3, start_delay=0, end_delay=0)
                                            abigail.reset_ui()
                                            abigail.speak("That aint even the right case!")
                                            abigail.speak("And you call yourself a senator? Shameful.", 2)
                                            change_life(-1)
                                        break

                                print_game_ui(False)
                                break
                            else:
                                you.reset_ui()
                                you.speak("Hey! This violates the First Amendment!")
                                you.speak("You can't ignore free speech like that!", 2)
                                jerry_m.reset_ui()
                                jerry_m.speak("We aren't talking about freedom of speech.")
                                jerry_m.speak("Pay attention.", 2)
                                change_life(-1)
                                print_game_ui(False)
                                break

                        elif counter_selection == 4:
                            break
                print_game_ui()
        elif selection == 4:
            print('\033[13A\033[2K', end='')
            you.reset_ui()
            you.speak("I'll write an arguementative essay.",end_delay=0)
            you.speak("I gotta do this well.",2)
            you.reset_ui()
            os.system('cls')
            time.sleep(0.2)
            for letters in "You got this!":
                print(letters,end="",flush=True)
                time.sleep(0.05)
            time.sleep(0.5)
            for letters in " Don't think too hard or spend a bunch of time.":
                print(letters,end="",flush=True)
                time.sleep(0.05)
            time.sleep(0.5)
            for letters in " Now why is this bill bad?":
                print(letters,end="",flush=True)
                time.sleep(0.05)
            time.sleep(0.3)
            print("\n")
            essay = input("( o_o) Thesis: ")
            input("Claim 1: ")
            input("Claim 2: ")
            input("Opposing View: ")
            time.sleep(0.5)
            print("OK!")
            time.sleep(0.5)
            os.system('cls')
            print("""                                 xxx
                                x
                               x    xx
                               x      x                      xx
      xxx                     x       xx               xxxxx x
       x x xxxx              x         x             xx      x
        x      xxxx         x           x        xxxx       x
        xx          xxx    x             x  xxxxx           x          xxxxxxxxxxxx
         x            xxxxx               xxx               x       xxx          x
          x                                xx               x   xxx             x
           x       ■■■■■■■                                  xxxx               x
             x    ■■             ■■■■■                                         x
           xx     ■■■■■■        ■          ■■■■■     ■■      ■■    ■■        xx
       xxxxx      ■■            ■■■       ■         ■  ■      ■■ ■■        xx
 xxxxxxx          ■■              ■■       ■■     ■■■■■■■      ■■         x
x                 ■■■■■■■■    ■■■■■         ■    ■■    ■■     ■■            x
xxxxxxxxxx                              ■■■■    ■■      ■    ■■             x
         xxxxx                                          ■    ■              x
             xxxxx                                                            x
                x                                            xx               xx
                x                                             xx                x
              xx                                              x xx              x
             xx                                               x   xxx            x
            x                                  x               x      xxxxxx      x
            x               xxxx               xx              x            xxxx   xx
           x             xxxx  xx             x  xx            x                xxxxx
         xx           xxx       x          xxx     x            x
         x         x x           x       xx          x          x
         x      xxxx              x    xx              x         x
         x    x x                  x  xx                 x       x
        xxxxx                      xx                     x      x
                                  xx                         xx  x
                                                               xxx""")
            time.sleep(2)
            os.system('cls')
            print(senate_room)
            you.reset_ui()
            you.speak("*essay*")
            jerry_m.reset_ui()
            if "because" in essay.lower():
                jerry_m.speak("This is a fantastic argument. Truly immaculate.")
                goku.reset_ui()
                goku.speak("Your argument is really strong!")
                abigail.reset_ui()
                abigail.speak("Yeah that was a valid point there.")
                change_life(1)
                selection = 0
                print_game_ui(False)
                for letters in "Great job!":
                    print(letters, end="", flush=True)
                    time.sleep(0.05)
                time.sleep(0.5)
                for letters in " To get points for an argumentative essay on the AP exam,":
                    print(letters, end="", flush=True)
                    time.sleep(0.05)
                time.sleep(0.3)
                for letters in " you need to put \"because\" in your thesis statement.":
                    print(letters, end="", flush=True)
                    time.sleep(0.05)
                time.sleep(1.2)
                os.system('cls')
                print(senate_room)
                selection = 1
                print_game_ui(False)
            else:
                jerry_m.speak("While I acknowledge your attempt at an argument,")
                jerry_m.speak("I can't let this slide.",2)
                jerry_m.speak("""You didn't put "because" in your thesis statement.""",3)
                you.reset_ui()
                change_life(-1)
                you.speak("NOOOOOOOOOOOOOOOOOOOOO")
                print_game_ui(False)

        elif selection == 5:
            print('\033[13A\033[2K', end='')
            you.reset_ui()
            you.speak("(Aight imma stall!)", pause_speed=0)
            you.reset_ui()
            you.ui += "Cloture: 0/100"
            you.speak("YO! According to all known laws of aviation there's ", 1, end_delay=0, speed=0.03)
            you.ui = you.ui.replace("Cloture: 0/100", "Cloture: 1/100")
            you.speak("no way a bee should be able to fly. Its wings are ", 2, start_delay=0, end_delay=0,
                      pause_speed=0, speed=0.02)
            you.ui = you.ui.replace("Cloture: 1/100", "Cloture: 5/100")
            you.speak("too small to get its fat little body off the ground.", 3, start_delay=0, end_delay=0,
                      pause_speed=0, speed=0.02)
            you.reset_ui()
            you.ui += "Cloture: 8/100"
            you.speak("The bee of course flies anyway because bees don't ", 1, start_delay=0, end_delay=0,
                      pause_speed=0, speed=0.02)
            you.ui = you.ui.replace("Cloture: 8/100", "Cloture: 19/100")
            you.speak("care what humans think is impossible. Yellow, black", 2, start_delay=0, end_delay=0,
                      pause_speed=0, speed=0.02)
            you.ui = you.ui.replace("Cloture: 19/100", "Cloture: 31/100")
            you.speak(", yellow, black, yellow, black, yellow, black, ooh", 3, start_delay=0, end_delay=0,
                      pause_speed=0, speed=0.02)
            you.ui = you.ui.replace("Cloture: 31/100", "Cloture: 45/100")
            you.reset_ui()
            you.ui += "Cloture: 51/100"
            you.speak("black and yellow! Let's shake it up a little! Barry!", 1, start_delay=0, end_delay=0,
                      pause_speed=0, speed=0.02)
            you.ui = you.ui.replace("Cloture: 51/100", "Cloture: 52/100")
            you.speak("breakfast is ready! Coming! Hang on a second! Hello?", 2, start_delay=0, end_delay=0,
                      pause_speed=0, speed=0.02)
            you.ui = you.ui.replace("Cloture: 52/100", "Cloture: 67/100")
            you.speak("-Barry? Adam? Can you believe this is happening?", 3, start_delay=0, end_delay=0, pause_speed=0,
                      speed=0.02)
            you.ui = you.ui.replace("Cloture: 67/100", "Cloture: 99/100")
            print(you.ui)
            time.sleep(0.1)
            os.system('cls')
            print("""                                 xxx
                                    x
                               x    xx
                               x      x                      xx
      xxx                     x       xx               xxxxx x
       x x xxxx              x         x             xx      x
        x      xxxx         x           x        xxxx                              
        xx          xxx    x             x   xxxx           x          xxxxxxxxxxxx
         x            xxxxx               xxx               x       xxx          x
          x                                xx               x   xxx             x
           x                                                xxxx               x
             x      ■■■■■■    ■    ■                                            x
           xx      ■■         ■    ■   ■      ■   ■■■■■■■■■■■                xx
       xxxxx        ■■■■■     ■■■■■    ■      ■      ■                     xx
 xxxxxxx                ■■   ■    ■    ■      ■      ■                    x
x                        ■   ■    ■    ■      ■      ■                      x
xxxxxxx xx          ■■■■■    ■    ■    ■    ■■      ■                       x
         xxxxx                          ■■■■        ■                       x
             xxxxx       ■       ■                                            x
                x        ■       ■     ■■■■■                 xx               xx
                x        ■      ■      ■    ■                 xx                x
              xx         ■     ■       ■■■■■                  x xx              x
             xx           ■■■■■        ■                      x   xxx            x
            x                         ■        x               x      xxxxxx      x
            x               xxxx      ■        xx              x            xxxx   xx
           x             xxxx  xx             x  xx            x                xxxxx
         xx           xxx       x          xxx     x            x
         x         x x           x       xx          x          x
         x      xxxx              x    xx              x         x
         x    x x                  x  xx                 x       x
        xxxxx                     xxx                     x      x
                                    xx                       xx  x
                                                                xxx"""
                  )
            time.sleep(2)
            os.system('cls')
            print(senate_room)
            you.reset_ui()
            you.speak("...")
            print(game_ui[0])
            time.sleep(0.3)
            for letters in "Clotures stop filibusters.":
                print(letters,end="",flush=True)
                time.sleep(0.05)
            time.sleep(0.5)
            for letters in " They need a 2/3 majority,":
                print(letters,end="",flush=True)
                time.sleep(0.05)
            time.sleep(0.1)
            for letters in " and over 40 have been invoked in 2023!":
                print(letters,end="",flush=True)
                time.sleep(0.05)
            time.sleep(1.2)
            os.system('cls')
            print(senate_room)
            print_game_ui(False)

        elif selection == 6:
            you.reset_ui()
            print('\033[13A\033[2K', end='')
            you.speak("Failure is not an option.", start_delay=0.5)
            print_game_ui(False)
        while keypress("enter"):
            pass
        if lose is True:
            break
os.system('cls')
print(senate_room)
jerry_m.reset_ui()
jerry_m.speak("Alright people. very important.")
jerry_m.speak("It's time for the final vote.",2,end_delay=1)
win_or_lose = [
"""
$$\     $$\ $$$$$$$$\  $$$$$$\            $$$$$$$\    $$\   
\$$\   $$  |$$  _____|$$  __$$\           $$  ____| $$$$ |  
 \$$\ $$  / $$ |      $$ /  $$ |$$\       $$ |      \_$$ |  
  \$$$$  /  $$$$$\    $$$$$$$$ |\__|      $$$$$$$\    $$ |  
   \$$  /   $$  __|   $$  __$$ |          \_____$$\   $$ |  
    $$ |    $$ |      $$ |  $$ |$$\       $$\   $$ |  $$ |  
    $$ |    $$$$$$$$\ $$ |  $$ |\__|      \$$$$$$  |$$$$$$\ 
    \__|    \________|\__|  \__|           \______/ \______|
""",
"""
$$\     $$\ $$$$$$$$\  $$$$$$\            $$\   $$\  $$$$$$\  
\$$\   $$  |$$  _____|$$  __$$\           $$ |  $$ |$$  __$$\ 
 \$$\ $$  / $$ |      $$ /  $$ |$$\       $$ |  $$ |$$ /  $$ |
  \$$$$  /  $$$$$\    $$$$$$$$ |\__|      $$$$$$$$ |\$$$$$$$ |
   \$$  /   $$  __|   $$  __$$ |          \_____$$ | \____$$ |
    $$ |    $$ |      $$ |  $$ |$$\             $$ |$$\   $$ |
    $$ |    $$$$$$$$\ $$ |  $$ |\__|            $$ |\$$$$$$  |
    \__|    \________|\__|  \__|                \__| \______/
""",
"""
$$\   $$\ $$$$$$$$\  $$$$$$\            $$$$$$$\    $$\   
$$$\  $$ |$$  _____|$$  __$$\           $$  ____| $$$$ |  
$$$$\ $$ |$$ |      $$ /  $$ |$$\       $$ |      \_$$ |  
$$ $$\$$ |$$$$$\    $$$$$$$$ |\__|      $$$$$$$\    $$ |  
$$ \$$$$ |$$  __|   $$  __$$ |          \_____$$\   $$ |  
$$ |\$$$ |$$ |      $$ |  $$ |$$\       $$\   $$ |  $$ |  
$$ | \$$ |$$$$$$$$\ $$ |  $$ |\__|      \$$$$$$  |$$$$$$\ 
\__|  \__|\________|\__|  \__|           \______/ \______|
""",
"""
$$\   $$\ $$$$$$$$\  $$$$$$\            $$\   $$\  $$$$$$\  
$$$\  $$ |$$  _____|$$  __$$\           $$ |  $$ |$$  __$$\ 
$$$$\ $$ |$$ |      $$ /  $$ |$$\       $$ |  $$ |$$ /  $$ |
$$ $$\$$ |$$$$$\    $$$$$$$$ |\__|      $$$$$$$$ |\$$$$$$$ |
$$ \$$$$ |$$  __|   $$  __$$ |          \_____$$ | \____$$ |
$$ |\$$$ |$$ |      $$ |  $$ |$$\             $$ |$$\   $$ |
$$ | \$$ |$$$$$$$$\ $$ |  $$ |\__|            $$ |\$$$$$$  |
\__|  \__|\________|\__|  \__|                \__| \______/
""",
"""
══════════════════════════════════════════════════
    $$\    $$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\  
    $$ |   $$ |$$  _____|\__$$  __|$$  __$$\ 
    $$ |   $$ |$$ |         $$ |   $$ /  $$ |
    \$$\  $$  |$$$$$\       $$ |   $$ |  $$ |
     \$$\$$  / $$  __|      $$ |   $$ |  $$ |
      \$$$  /  $$ |         $$ |   $$ |  $$ |
       \$  /   $$$$$$$$\    $$ |    $$$$$$  |
        \_/    \________|   \__|    \______/
══════════════════════════════════════════════════
""",
"""
$$\     $$\  $$$$$$\  $$\   $$\       $$\      $$\ $$$$$$\ $$\   $$\ $$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ | $\  $$ |\_$$  _|$$$\  $$ |$$ |
 \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |$$$\ $$ |  $$ |  $$$$\ $$ |$$ |
  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |  $$ |  $$ $$\$$ |$$ |
   \$$  /   $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |  $$ |  $$ \$$$$ |\__|
    $$ |    $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |  $$ |  $$ |\$$$ |    
    $$ |     $$$$$$  |\$$$$$$  |      $$  /   \$$ |$$$$$$\ $$ | \$$ |$$\ 
    \__|     \______/  \______/       \__/     \__|\______|\__|  \__|\__|
""",
"""
$$\     $$\  $$$$$$\  $$\   $$\       $$\       $$$$$$\   $$$$$$\  $$$$$$$$\ $$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ |     $$  __$$\ $$  __$$\ $$  _____|$$ |
 \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |     $$ /  $$ |$$ /  \__|$$ |      $$ |
  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |\$$$$$$\  $$$$$\    $$ |
   \$$  /   $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ | \____$$\ $$  __|   \__|
    $$ |    $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |$$\   $$ |$$ |          
    $$ |     $$$$$$  |\$$$$$$  |      $$$$$$$$\ $$$$$$  |\$$$$$$  |$$$$$$$$\ $$\ 
    \__|     \______/  \______/       \________|\______/  \______/ \________|\__|
"""]
os.system('cls')
time.sleep(1)
if lose is True:
    print(win_or_lose[0])
else:
    print(win_or_lose[1])
time.sleep(1)
if lose is True:
    print(win_or_lose[3])
else:
    print(win_or_lose[2])
if lose is True and will_veto is True:
    time.sleep(1)
    print(win_or_lose[4])
time.sleep(1)
if lose is True and will_veto is True:
    print(win_or_lose[5])
elif lose is True and will_veto is False:
    print(win_or_lose[6])
else:
    print(win_or_lose[5])

time.sleep(3)
print("""
Source for Cloture Info:
- https://www.senate.gov/legislative/cloture/clotureCounts.htm
""")
input()
