myset={1}
print(myset)
myset.add(2)
print(myset)
myset.add(3)
print(myset)

my_list = [1, 2, 3, 3, 4, 5, 5]
my_set = set(my_list)
print(my_set)

my_list = [1, 2, 3, 3, 4, 5, 5]
my_set = {x for x in my_list}

print(my_set)

my_list = [1, 2, 3, 3, 4, 5, 5]
my_dict = dict.fromkeys(my_list)
my_set = set(my_dict)

print(my_set)

