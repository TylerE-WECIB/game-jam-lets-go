import os
x = [
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "10",
    "11", "12", "13", "14", "15",
    "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25"
]

g=0
print(x[g])
y=0
while y==0:
    try:
        o=input("Pick right:")
        if o.lower() =="right":
            os.system('cls')

            if g>=0:
                g += 1
                print(x[g])

            else:
                print("ty again")


        elif o.lower()=="left":
            os.system('cls')

            if g>=0:
                g -= 1
                print(x[g])

            else:
                print("ty again")

        elif o.lower()=="down":
            os.system('cls')

            if g>=0:
                g += 5
                print(x[g])

            else:
                print("ty again")

        elif o.lower()=="up":
            os.system('cls')

            if g>=0:
                g -= 5
                print(x[g])

            else:
                print("ty again")
        else:
            print("try again:")
    except:
        print("can't go there")

