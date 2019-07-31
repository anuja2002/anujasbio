#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
d = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
test_password = test_password.strip()

found = False


#Write logic to see if the password is in the dictionary file below here:
for line in d:
    if test_password.strip() == line.strip():
        found = True
        print("You have been caught" )
        break

if  not found:
    print("Congrats, you made it through")
