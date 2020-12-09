# check user number and comparison with 4 condition 
userData = int(input('Enter your value:'))
if (userData > 1 and userData < 10):
    print("You found your number between 1 and 10 ")
elif (userData > 10 and userData < 20):
    print("You found your number between 10 and 20")
elif (userData > 20 and userData < 30):
    print("You found your number between 20 and 30")
elif (userData > 30):
    print("You number is greater than 30")
print("done")
