import random
import math
print("**************Guessing number choose zero(0) to ten (10)***********")
number = int(input("You, Enter the number :"))
computer = random.randrange(0, 10)
print("Computer, Enter the number  : " ,computer)
def random_game(number,computer):
    if number>computer:
        print("Winner is You! ")
    elif number<computer:
        print("Winner is computer !")
    elif number==computer:
        print("This match is tie !")
    else:
        print("Syntax Error !")