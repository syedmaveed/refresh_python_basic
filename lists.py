# mylist=[1,2,3]

# mylist1=['abc',1]
# mylist1.append('xyz')
# mylist1.pop()

# #remove item inbetween
# newlist= mylist+mylist1
# print("NEW lIST : ",newlist)
# print(len(mylist1))
# print((mylist1[0]))
# print((mylist1))
# print(mylist + mylist1)
# newlist.pop(0)
# print(newlist)
# print(newlist[2:])
from functools import reduce
import operator
# import itertools
# list_new=['string',1,1.223,["A nested list"], "another item"]  

# flatList = list(itertools.chain.from_iterable(list_new))
# #list=[[1,2],[3,5],[4,6]]

# print(list_new)
# print(flatList)

from functools import reduce
xss = [[1,2,'a'], [4,5,6], ['string'], [8,9]]
out = reduce(lambda xs, ys: xs + ys, xss)
print(out)

new_list= [['string',1,1.223],["A nested list"], ["another item"]]
result=reduce(lambda a, b: a + b , new_list)
print(result)
# newlist=[]
# for x in list:
#     for y in x:
#         newlist.append(y)
# print("Newlist", newlist)