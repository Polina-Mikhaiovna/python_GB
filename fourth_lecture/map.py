# map() применяет переданную функцию ко всем элементам переданного объекта

list_1 = [x for x in range(1, 20)] # генерация списка
print(list_1)

list_2 = list(map(lambda x: x + 10, list_1)) # создаём список 
print(list_2)                 # из элементов list_1 к которым 
                                   # применена лямбда-функция
