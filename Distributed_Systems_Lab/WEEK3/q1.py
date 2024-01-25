# 1. Write a program to find the factors of a given number (get input from user) using for loop.
n = int(input("Enter a number: "))
print("Factors are:")
for i in range(1,n+1):
    if n%i==0: print(i, end=' ')