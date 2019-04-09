
n = int(input())
cnt = 0
arr = [int(x) for x in input().split()]

for i in reversed(range(n)):
	print(arr[i],end = " ")