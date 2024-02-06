num = int(input("Enter number: "))
a = 0
b = 100
flag = False
while flag == False:
    x = b - ((b - a) // 2)
    print(x, ">, <, =")
    answer = input()
    if answer == "=":
        print(x)
        flag = True
    elif answer == ">":
        a = x
    else:
        b = x


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
    	pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([1, 5, 96456, 53, 56]))