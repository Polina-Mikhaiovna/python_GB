a = 3
b = 5

# Возведение числа a в степень b
def f(a, b):
	if b == 1:
		return a
	return a * f(a, b - 1)

print(f(a,b))

# Сумма чисел a и b
def sum(a, b):
	if b == 0:
		return a
	return sum(a + 1, b - 1)

print(sum(a, b))

# Сложение цифр числа x
def rec(x):
	if x == 0: return x
	y = x % 10
	x = x // 10
	return y + rec(x)
print(rec(123))

