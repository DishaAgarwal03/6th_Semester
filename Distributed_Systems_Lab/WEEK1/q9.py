l = [1,2,-4,-2,4]
p, n = 0, 0
for i in l:
    if i<0: n+=1
    elif i>0: p+=1
print("# positive numbers:", p, "\n# negative numbers:", n)