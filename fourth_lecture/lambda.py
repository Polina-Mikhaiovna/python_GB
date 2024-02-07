'''
list1 = [1, 2, 3, 5, 8, 15, 23, 38]
new_list = []

for i in list1:
	if (i % 2) == 0:
		new_list.append((i, i*i))

print(new_list)
'''
def select(f, col): # это и есть функция map(), select() можно удалить и заменить на map()
	return [f(x) for x in col]

def where (f, col):
	return [x for x in col if f(x)]

list1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, list1)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)