input_num=input()
if input_num==-1:
    print("you typed -1!")
else:
        print("you typed "+ str(input_num))


distance=0.0 
while True:
    distance = distance+10
    print(distance)
    if distance>72.5:
        break
# Always be careful indented block when using while loop and if statement
# You can see |   |   | with a same interval line while if break

friends =1
while friends<5:
    friends= friends+1
    print("your friend number "+ str(friends))
    digits=0
    while digits<4:
        digits= digits+1
        print(digits)
