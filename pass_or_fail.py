# calculate students exam marks
sub1 = int(input("Enter your subject marks \n:"))
sub2 = int(input("Enter your subject marks \n:"))
sub3 = int(input("Enter your subject marks \n:"))

if(sub1<33 or sub2<33 or sub3<33):
    print("Sorry, You are fail !")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to less percantage")
else:
    print("Congratulation! You are passed")
