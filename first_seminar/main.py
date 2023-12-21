# 2 Найдите сумму цифр трехзначного числа.
print("Введите трёхзначное число:")
n = int(input())
summa = 0

while n > 0:
	x = n % 10
	summa = summa + x
	n = n // 10

print("Сумма цифр этого числа =", summa) # 9

# 4 Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
print("Количество журавликов: ")
n = int(input())
oneBoy = n//6
print("S and P =", (oneBoy), "K =", (4 * oneBoy))

# 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
print("Номер билета: ")
ticket = int(input())
summa = 0

while ticket > 0:
	x = ticket % 10
	summa += x
	ticket = ticket // 10
	if ticket <= 999 and ticket > 99:
		firstPart = summa
		summa = 0

if firstPart == summa:
	print("yes")
else:
	print("no")



# 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
print("Сколько рядов у шоколадки: ")
n = int(input())
print("Сколько столбцов у шоколадки: ")
m = int(input())
print("Сколько кусочков отломить: ")
k = int(input())
if ((k % m) == 0) or ((k % n) == 0) or (k == n) or (k == m):
	print("yes")
else:
	print("no")