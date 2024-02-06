# Вывод оригинальных значений списка

many = set()
list_1 = [1, 1, 2, 0, -1, 3, 4, 4]

for i in range(len(list_1)):
	many.add(list_1[i]) # Используя особенность кортежа хранить только уникальные элементы
	                    # применяем к списку метод добавления элементов в кортеж
print(len(many))


# Циклический сдвиг


'''
    reverse(0, i-1)   /* cba|defgh */
    reverse(i, n-1)   /* cba|hgfed */
    reverse(0, n-1)   /* defgh|abc */
'''

list1 = [1, 2, 3, 4, 5, 6] 
k = 3
def reverse(array, i, l):
    temp = 0
    for i in range(len(array)//2):
    	temp = array[i]
    	array[i] = array[l-i]
    	array[l-i] = temp

    return array

print(reverse(list1, 0, len(list1) - 1))

print(reverse(list1, 0, k-1))

# !!!!!!!!!!! на жанном этапе не работает, дописать











