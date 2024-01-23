#2. Write a python program to reverse a content a file and store it in another file. 

f1 = open("outfile.txt", "w")
with open("infile.txt", "r") as myfile:
    data = myfile.read()

data_1 = data[::-1]
f1.write(data_1)
print("File successfully written!")
f1.close()
