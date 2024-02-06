list1 = [1, 2, 3, 4, 5, 6] 
k = 2
#k = len(list1) - k # смещение влево
arr = []
for i in range(len(list1)-k, len(list1)): # [4, 5, 6]
    arr.append(list1[i])

for i in range(len(list1)-k):
	arr.append(list1[i])

print(arr)