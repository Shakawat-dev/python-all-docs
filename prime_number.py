num = int(input("Enter your number : "))
prime = True
for i in range (2, num):
    if (num%i == 0 and num != 2):
        prime = False
if prime:
    print("This number is a prime number :)")
else:
    print("This number is not a prime number :(")
print("Done")
