#Numeric data

num = 3

print(type(num))# Prints the type of num, which "int" for integer

num2 = 3.14
print(type(num2))# Prints the type of num2, which is "float" for floating-point number    

#Variables
#Valid variable names
my_variable = 10
total_count = 0
user = 'John'

#Invalid variable names
#2nd_variable = 10 # Variable names cannot start with a digit
#user-name = 'John'  # Hyphens are not allowed in variable names

#Operators
#Arithmetic Operators
x = 10
y = 2

print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus is the remainder after the division
print(5 % 2) # The answer is 1, because 5 divided by 2 is 2 with a remainder of 1
print(x ** y) # Exponentiation (x raised to the power of y)

x -= 2 # This is equivalent to x = x - 2
x += 2 # This is equivalent to x = x + 2
print(x) # Prints the updated value of x

#Operators on Strings

str1 = "Hello"
str2 = "World"

print(str1 + " " + str2)
print((str1 + " " ) * 3)  # Repeats the string 3 times
