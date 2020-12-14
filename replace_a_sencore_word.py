with open("sencor_word.txt", "r") as f:
    content = f.read()
content = content.replace("donkey", "*******")
with open("sencor_word.txt", "w") as f:
    f.write(content)
