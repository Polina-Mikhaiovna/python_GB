def fibonacchi(n):

    if n == 1: return 0
    elif n == 2: return 1
    return fibonacchi(n - 2) + fibonacchi(n - 1)

for i in range(1, 11):
	print(fibonacchi(i), end=' ')


def fibonacchi_for(n):
    if n == 1: return 0
    elif n == 2: return 1
    n1, n2 = 1, 0
    for i in range(3, n+1):
        res = n1 + n2
        n2 = n1
        n1 = res
    print(res)

fibonacchi_for(10)
