arr = [5, 8, 6, 4, 9, 2, 7, 3]

max = arr[-2] + arr[-1] + arr[0]
sum = 0
for i in range(len(arr)-1):
	sum = arr[i-1] + arr[i] + arr[i+1]
	if max < sum:
		max = sum

print(max)
