# multiply by the user nunber
num  = int(input("Enter your number : "))
for i in range(1, 10):
# print(str(i) + ' x ' + str(num) + ' = ' + str(num*i)) 
    print(f"{num} X {i} = {num  * i}")
# Find string using first character
nameList = ['Rahul', 'Sochin', 'Sohan', 'Shakib', 'patal']
for name in nameList:
    if name.startswith('S'):
        print(name)

