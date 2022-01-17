with open("file1.txt") as file, open("file2.txt") as myfile:
    mylist = file.readlines()
    mysecondlist = myfile.readlines()
new_list = [int(x.strip()) for x in mylist if x in mysecondlist]
print(new_list)
