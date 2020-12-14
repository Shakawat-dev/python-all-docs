# with open("poems.txt", "r") as f:
#     readFile = f.read()
f = open('poems.txt')
t = f.read()
if "twinkle" in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()
