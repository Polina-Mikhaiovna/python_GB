print("Выдать без повторений в порядке возрастания числа," +
      "которые встречаются в двух неупорядоченных наборах чисел.")


var1 = '5 6 7 8' 
var2 = '6 7 8 9'
print(var1)
print(var2)

first = set(map(int, var1.split())) # преобразование строки в множество(уберёт повторы) с приведение к типу int
second = set(map(int, var2.split())) # то же для второй строки

res = sorted(list(first.intersection(second))) # СОРТИРУЕМ ПРЕОБРАЗОВАННЫЕ В ЛИСТ ПЕРЕСЕЧЕНИЯ МНОЖЕСТВ first и second
print(' '.join(map(str, res))) # выводим преобразованный в строку список элементы которого приведены к типу str


'''
var1 = '4 4'
var2 = '5 6 7 8' 
var3 = '6 7 8 9'
Ожидаемый ответ:

6 7 8

Некоторые методы для работы с множествами:
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
'''
