#write a python program that accepts a filename from the user and prints the extension of the file

fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])


