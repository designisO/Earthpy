# Welcome to EarthPy!!!


print("Welcome to EarthPy")
username = input("What is your username please? ")
if username == '':
    exit()
location = input("What country did you want to visit? ")
travelers = input("How many travelers would you have with you? ")
beds = input("How many beds needed? ")
rental = input("Would you need a rental car? ")
nights = input("How many nights will you be visiting " + location + "? ")
print("Please confirm the details listed below:::::  ")
print("You will be visitng the country of: " + location)
print("Travelers: " + travelers)
print("Beds: " + beds)
print("rental: " + rental)
print("nights: " + nights)
confirmation = input("Is this information correct? ")
if confirmation == ("yes"):
    print("You are all SET. 5 Star Hotel Room Reserved under the guest named: " + username)
    print("Software developed by Orion")
else:
    print("Well I guess we must restart. Thanks for visiting EarthPy.")
    print("Software developed by Orion Ford.")
    exit()





