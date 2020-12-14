# update a score of a file with a function
def game():
    return 543
score = game()
with open("update_score.txt") as f:
    highscoreStr = f.read()
if highscoreStr == "":
    with open("update_score.txt", "w") as f:
        f.write(str(score))
elif int(highscoreStr) < score :
    with open("update_score.txt", "w") as f:
        f.write(str(score))
