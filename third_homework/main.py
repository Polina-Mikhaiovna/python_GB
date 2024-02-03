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

# Поиск ближайшего по значению элемента в списке
list_1 = [1, 8, 2, 3, 4, 5]
k = 5
min = abs(k - list_1[0])
i = 0
index = 0

for i in range(len(list_1)):
    if min > (abs(k - list_1[i])):
        min =  abs(k - list_1[i])
        index = i
print(list_1[index])

#Игра Скрабл. Подсчёт стоимомти введённого пользователем слова.
'''
dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →
'''
k = 'hel'
k = k.upper()
cost = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
res = 0
for i in k:
    for j in cost: # j принимает значения ключей
        if i in cost[j]: # cost[j] это значение под j-ым ключом
            res = res + j
print(res)
