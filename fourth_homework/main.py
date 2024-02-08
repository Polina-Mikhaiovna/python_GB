'''
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
'''

var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

n = int(var1[0])
m = int(var1[2])

first = set(map(int, var2.split()))
print(first)
second = set(map(int, var3.split()))

res = list(first.intersection(second))
res = map(str, res)
print(' '.join(res))



var1 = '4 4'
var2 = '5 6 7 8' 
var3 = '6 7 8 9'
Ожидаемый ответ:

6 7 8

Ваш ответ:

8 6 7


ar1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'