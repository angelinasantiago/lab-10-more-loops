userstring = input("Gimme a number that is greater than 100... ")
usernum = int(userstring)

while (usernum < 100): #test condition for when the condition is not TRUE
  print(str(usernum) + " is less than 100, try again...")
  userstring = input("Give me a number that is greater than 100...")
  usernum = int(userstring)

print(str(usernum) + " is greater than 100! Great job!")
