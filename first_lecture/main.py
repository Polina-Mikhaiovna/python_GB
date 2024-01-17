print("Задача: Сколько нужно двухместных парт для учеников классов a, b, c")
a = 20
b = 21
c = 22
print(((a + 1) // 2) + ((b + 1) // 2) + ((c + 1) // 2))


print(f"{b} / 2 =", b / 2) # 10.5
print(f"round({b} / 2) =", round(b / 2)) # 10
print(f"round(({b} + 0.1 ) / 2) =", round((b + 0.1 ) / 2)) # 11
print(f"{b} // 2 =", b // 2) # 10
print(f"{b} % 2 =", b % 2) # 1
k = 21.4
print(f"{k} % 2 =", k % 2) # 1.3999999999999986


print("for i in range(1, 10, 2):")
for i in range(1, 10, 2):
	print(i)


for i in range(5):
	line = "" # опустошаем строку
	for j in range(5):
		line += "+" #заполняем плюсиками
	print(line)


text = 'СЪешЬ ещё'
print(f"len({text}) ->", len(text))
print(f"'ещё' in {text}) ->", 'ещё' in text)
print(f"{text}.lower() ->", text.lower())
print(f"{text}.upper() ->", text.upper())
print(f"{text}.replace('ещё', 'ЕЩЁ') ->", text.replace('ещё', 'ЕЩЁ'))
