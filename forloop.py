foods=['pizza','icecream','pasta']

for food in foods:
    if food=="pizza":
        size=input("what size is the pizza?  ")
        print(f"you ordered a {size} pizza")
    
food1="pizza"
for letter in food1:
    print(letter)
    
dic={"name":"A","tweet":"a","insta":"aa"}
for key, value in dic.items():
    print(f"The key is {key} and value is {value}")
    

dic={"name":"A","tweet":"a","insta":"aa"}
for key in dic.keys():
    print(f"The key is {key} ")

dic={"name":"A","tweet":"a","insta":"aa"}
for  value in dic.values():
    print(f" value is {value}")