# 12. Write a program to print negative Numbers in a List using while loop.
l = [-1, 4, 5, -324, 23, -34]
i = 0
while i<len(l):
    if l[i]<0:
        print(l[i])
    i+=1