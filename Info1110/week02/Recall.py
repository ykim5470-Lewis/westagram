import sys
print("Enter your height in metres: ")
input_variable = sys.argv[1]
input_variable2= sys.argv[2]
height = float(input_variable)
height2 = float(input_variable2)
print("You entered "+ str(height) + "m.")
print("If you were 10% bigger you'd be "+ str(height*1.1) +"m. ")
print("10 years later, I would be " +str(height2)+ "m. ")
