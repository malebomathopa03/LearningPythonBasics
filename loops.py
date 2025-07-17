#Loops
#for loop

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits: # Iterating through the list
    print(fruit)
    
numbers = [1, 2, 3, 4, 5]    

for number in numbers:
    print(numbers)# Prints the entire list in each iteration
    print(number) # Prints the current number in each iteration
    
#Using a while loop to count from 1 to 5
count = 1

while count <= 5: # Loop until count is greater than 5
    print(count)
    count += 1 # Increments the count by 1 in each iteration    

#Loop Control Statements
#if statements in loops
for fruit in fruits:
    if fruit == "cherry":
        break  # Skip the rest of the loop for this iteration/ exit the loop if cherry is found
    print(fruit) # Prints all fruits until cherry is found and not including cherry

for fruit in fruits:
    if fruit == "cherry":
        continue # Skip the rest of the loop for this iteration if cherry is found
    print(fruit) # Prints all fruits except cherry   
    
for fruit in fruits:
    if fruit == "cherry":
        pass  # Do nothing, just a placeholder. No action is needed for cherry
    print(fruit) # Prints all fruits including cherry
    
#While loop with break

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  # Exits the loop when count reaches 3> it won't print 3