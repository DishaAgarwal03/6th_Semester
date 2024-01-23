#1. Write a python program to implement simple calculator which perform addition, 
#subtraction, multiplication, and division. 

print("Enter numbers: ")
a = int(input())
b = int(input())
op = input("Enter operator(+,-,*,/,//): ")
if op=='+': print(a+b)
elif op=='-': print(a-b)
elif op=='*': print(a*b)
elif op=='/' and b!=0: print(a/b)
elif op=='//' and b!=0: print(a//b)
else: print("Wrong operator or b is 0")