# 11. Write a program to demonstrate while loop with else.
n = 0
while n<10:
    n = int(input("Enter: "))
    if n==5:
        break
else:
    print("Not 5")
print("Success")