print("Please enter your NAME")
name = input()

print("Please create your USERNAME:")
username = input()

print("Please create your PASSWORD")
password = input()

login = username + password

#going through the username and password entering process
print("Please enter your USERNAME")
while input() != username:
    print("Incorrect try again!")
print("Correct!")

print("Please enter your PASSWORD")
while input() != password:
    print("Incorrect try again!")
print("Correct!")