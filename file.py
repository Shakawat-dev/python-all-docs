# Modes of opening the file 
# 1.r >> open for reading
# 2.w >> write for writing
# 3.a >> open for appending
# 4.+ >> open for updating

# Read a file with open statement
f = open("file.txt") 
with open('file.txt', 'r') as f:
    a = f.read()
print(a)

# write a file with open statement
with open('file.txt', 'w') as f:
    a = f.write('mr.khan')
print(a)

data = f.read()
# read the first line of the file 
data = f.readline()
print(data)
# Read the second line of the file
# show output with spacing for /n  (readline())
data = f.readline()
print(data)
# Read the third line of the file
data = f.readline()
print(data)
# Read the fourth and so on line of the file
data = f.readline()
print(data)
f.close()
