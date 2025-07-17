#Control statements
# if, else, elseif

num = 10

if num > 0:
    print("This number is positive.")
else:
    print("This number is either zero or negative.")    

#elseif
num2 = -5
if num2 > 0:
    print("This number is positive.")
elif num2 == 0:
    print("This number is zero.")
else:
    print("This number is negative.")    

#Compare two numbers
numA = int(input("Enter the first number: "))    
numB = int(input("Enter the second number: "))

if numA > numB:
    print(numA, "is greater than", numB)
elif numA < numB:
    print(numB, "is greater than", numA)    
else:
    print("Both numbers are equal.")    
    