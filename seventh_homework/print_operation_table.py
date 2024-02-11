def print_operation_table(operation, rows=9, cols=9):
	"""
    Функция вывода таблицы
	:param operation: функция бинарной операции rows: количество строк cols: количество столбцов
	:return: 
	"""
	if rows <= 1 or cols <= 1:
		print("ОШИБКА! Размерности таблицы должны быть больше 2!")
		return
	for i in range(1, rows+1):
		for j in range(1, cols+1):
			if j == cols:
				print(operation(i, j))
			else:
					print(operation(i, j), end=' ')

print_operation_table(lambda x, y: x * y, 3, 3)


# Чуть отличающееся решение с платформы GB
'''
def print_operation_table(operation, num_rows=9, num_columns=9):
    result = []
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                if j != num_columns :
                    result.append(f'{operation(i, j)} ')
                else:
                    result.append(operation(i, j))
            result.append('\n')
        print(''.join([str(i) for i in result[:len(result) - 1]]))
'''