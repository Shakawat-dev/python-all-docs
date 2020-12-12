# Rock , Paper, Sessor ----- game #
import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False
    elif comp == "p":
        if you == "s":
            return True
        elif you == "r":
            return False
    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False
print("Comp Turn : Snake(s), Water(w), Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "r"
elif randNo == 2:
    comp = "p"
elif randNo == 3:
    comp = "s"
you = input("Your Turn : Snake(s), Water(w), Gun(g)? : ")
a = gameWin(comp, you)
print(f"Computer chose : {comp}")
print(f"You chose : {you}")
if a == None:
    print("The game is Tie!")
elif a:
    print("You Won!")
else:
    print("You Lose!")
