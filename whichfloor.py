maximum_stories = 10
userinput = input("On what floor of the building is your office?")
floor = int(userinput)
while (floor > 10):
    print("This building only has 10 floors. Please, enter another number...")
    userinput = input("What floor is your office on?")
    floor = int(userinput)
print("Congratulations, " + (str(floor) + " is a valid floor number for this building"))
