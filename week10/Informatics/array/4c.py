
n = int(input())

arr = [int(x) for x in input().split()]
cnt = 0
for i in range(n):
    if arr[i] > 0:
    	cnt += 1


print(cnt,end = " ")