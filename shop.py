from distutils.command.config import LANG_EXT


print("Welcome to PyShop. \n I hope you enjoy")
username = input('Enter username: ')
print("Ok " + username + " let's go forth and write your shopping list.")
item1 = input('Enter item: ')
item2 = input('Enter item: ')
item3 = input('Enter item: ')
item4 = input('Enter item: ')
shoplist = (item1 + item2 + item3 + item4)
confirm = input("Are there any more items to add? ")
if confirm == "no":
    print('Here is your shopping list: \n' + shoplist)
    print('Happy Shopping ' + username)


print("Okay... now let's get some other things going")
greeting = input('Do you feel like $s is the best programming lanugage')
if confirm == 'yes':
    print('yes.... we love python too.')
else:
    lang = input("Wow! What is your favorite programming language?")
    print("Ok..." + lang + " eh. Well I hope you come to the Py side of things!")
    exit()



