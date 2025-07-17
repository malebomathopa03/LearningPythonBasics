#Strings

message = """Hello.
World!"""

print(message)

#Advanced Concepts
#Indexing

message_1 = " Hello "
print(message_1[0])
print(message_1[1])
print(message_1[-1])

#Length of a string
print(len(message_1))

#Strip
message_2 = " Hello, World! "
print(message_2.strip())#Removes whitespaces from both ends
print(message_2.lower())#Converts to lowercase

#Spl
print(message_2.split(','))#Splits the string into a list based on the comma

#upper method
print(message_2.upper())#Converts to uppercase
#Replace method
print(message_2.replace("Hello", "Hi"))#Replaces "Hello" with "Hi"
