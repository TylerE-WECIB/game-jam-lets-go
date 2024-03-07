import os
x = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9",
    "10", "11", "12", "13", "14",
    "15", "16", "17", "18", "19",
    "20", "21", "22", "23", "24"
]

g=0
print(x[g])
y=0
while y==0:
    try:

        o=input("Pick right:")
        if o.lower() =="right" and g not in [4, 9, 14, 19 ,24]:
            os.system('cls')

            g += 1
            print(x[g])

        elif o.lower()=="left" and g not in [0,5,10,20]:
            os.system('cls')

            g -= 1
            print(x[g])

        elif o.lower()=="down" and g not in [20,21,22,23,24]:
            os.system('cls')

            g += 5
            print(x[g])

        elif o.lower()=="up" and g not in [0,1,2,3,4]:
            os.system('cls')

            g -= 5
            print(x[g])

        else:
            print("try again:")
    except:
        print("can't go there")

