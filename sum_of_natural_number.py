# Sum of user given number
num = int(input("Enter your number : "))
naturalNum = 0
for i in range(0, num+1):
    naturalNum += i
print(f"Sum of {num} is {naturalNum}")
