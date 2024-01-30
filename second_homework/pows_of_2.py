n = int(input("До какого числа вывести все степени двойки?" + "До:"))
'''
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1
'''

i=0
res = 0
num = 2
for i in range(0, n):
    res = num ** i
    if res == n:
        print(res)
        break
    elif res > n:
        break
    else:
        print(res)
