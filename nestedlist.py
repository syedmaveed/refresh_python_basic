from functools import reduce
# xss = [[1,2,'a'], [4,5,6], ['string'], [8,9]]
# out = reduce(lambda xs, ys: xs + ys, xss)
# print(out)

new_list= [['string',1,1.223,["A nested list"], ["another item"],'a']]
result=reduce(lambda a, b: a + b , new_list)
print(result)

## LAMBDA and Reduce fuctions are very imp