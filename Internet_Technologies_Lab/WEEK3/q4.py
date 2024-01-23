# 4. Write a python program to sort words in alphabetical order.
s = input("Enter words: ")
l = s.split(" ")
n = len(l)
for i in range(n-1):
	for j in range(n-i-1):
		if l[j]>l[j+1]:
			l[j],l[j+1] = l[j+1],l[j]
for word in l:
	print(word,end=' ')
print()