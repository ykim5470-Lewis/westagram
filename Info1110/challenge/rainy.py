# YOUR CODE HERE
answer= input("Is it currently ranining? ")
if answer == "Yes":
    print("You should take the bus")
elif answer == "No":
    distance= input("How far km do you need to travel? ")
    if int(distance)>=2 and int(distance)<=10:
        print("You should take the bus.")
    elif int(distance)<2:
        print("You should ride your bike.")
        


