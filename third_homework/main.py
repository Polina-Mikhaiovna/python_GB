'''
print("Поиск в списке list_1 = [1, 2, 3, 4, 5]")
print("переменной k и вывод количества совпадений")
list_1 = [1, 2, 3, 4, 5]
k = 1

count = 0
for i in list_1:
    if i == k:
        count +=1
print(count)
'''

list_1 = [1,8, 2, 3, 4, 5]
k = 5
min = abs(k - list_1[0])
i = 0
index = 0

for i in range(len(list_1)):
    if min > (abs(k - list_1[i])):
        min =  abs(k - list_1[i])
        index = i
print(list_1[index])