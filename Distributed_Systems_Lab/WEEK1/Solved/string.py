str = 'Hello World!'
print (str) # Prints complete string
print (str[0]) # Prints first character of the string
print (str[2:5]) # Prints characters starting from 3rd to 5th
print (str[2:]) # Prints string starting from 3rd character
print (str * 2) # Prints string two times
print (str + "TEST") # Prints concatenated string

# Updating a string
var1 = 'Hello World!'
print ("Updated String :", var1[:6] + 'Python')

# String formatting operator
print( "String formatting: My name is %s and weight is %d kg!" % ('Abay', 55))

# Built−in String methods
str = "this is STRING example wow!!!"
print ("Capitalize: ", str.capitalize())
print("Count: ", str.count('s'))
print("Find: ", str.find('example'))
print ("Lower: ", str.lower())
print ("Replace: ", str.replace("is", "was"))
print ("Swapcase: ", str.swapcase())
print ("Title: ", str.title())
