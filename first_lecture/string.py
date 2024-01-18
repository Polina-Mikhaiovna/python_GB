text = 'съешь ещё этих мягких французских булочек'
print("text =", text)
print("len(text)", len(text))
print("text[1]", text[1])
print("text[len(text)-1]", text[len(text)-1])
print("text[-1]", text[-1]) #тоже что и предыдущее
print("text[:]", text[:])
print("text[:2]", text[:2])
print("text[len(text)-2:]", text[len(text)-2:])
print("text[2:5]", text[2:5])
print("text[2:-18]", text[2:-18])
print("text[0:len(text):6]", text[0:len(text):6]) # от нуля до конца с шагом 6
print("text[::6]", text[::6])

a = [0, 1, 2, 3, 4, 5]

print(a[0:4:2])
print(a[0])
