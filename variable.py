# name=input("Enter your name")
# print("my name is :",end="")
# print(name)

#********************************************#
#FORMATTED STring

# name=input("Enter the name: ")
# print(f"Hello {name}")

#******************************************#
#USe escape char to add quote to ur char

# print('hello,  "friend"')

# # OR

# print("hello, \"friend\"")

#***************************************#

#STRING USages

#remove whitespace

# name=input("Enter Name : ")
# name=name.strip()
# print(f"HEllo {name}")

# #Capitalise first letter
# name=input("Enter Name : ")
# name=name.strip()
# name=name.capitalize()
# print(f"HEllo {name}")


#Capitalise first letter for each word
# name=input("Enter Name : ")
# name=name.strip()
# name=name.title()
# print(f"HEllo {name}")

# Fix all in one line using these

name=input("Enter Name : ")
name=name.strip().title()

print(f"HEllo {name}")

# One more way to write this code

name=input("Enter Name : ").strip().title()

name=name.split(" ",1) #Changes string into a list
print(f"HEllo {name}")
