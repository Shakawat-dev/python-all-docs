# # Snake, gun, water ----game
# import random


# def gameWin(comp, you):
#     if comp == you:
#         return None
#     elif comp == "s":
#         if you == "w":
#             return False
#         elif you == "g":
#             return True
#     elif comp == "w":
#         if you == "g":
#             return False
#         elif you == "s":
#             return True
#     elif comp == "g":
#         if you == "s":
#             return False
#         elif you == "w":
#             return True
# print("Comp Turn: Snake(s), Water(w) or Gun(g)?")
# rantNo = random.randint(1, 3)
# if rantNo == 1:
#     comp = "s"
# elif rantNo == 2:
#     comp = "g"
# elif rantNo == 3:
#     comp = "w"
# you = input("Your Turn: Snake(s), Water(w) or Gun(g)? : ")
# a = gameWin(comp, you)
# print(f"Computer chose {comp}")
# print(f"You chose {you}")
# if a == None:
#     print("The game is Tie!")
# elif a:
#     print("You Won!")
# else:
#     print("You Lose!")




