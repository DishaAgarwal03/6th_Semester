print("Enter 3 values: ")
a = int(input(""))
b = int(input(""))
c = int(input(""))
print("Largest number is: ")
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)