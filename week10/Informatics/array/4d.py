
n = int(input())
cnt = 0

arr = [int(x) for x in input().split()]

for i in range(1,n):
    if arr[i] > arr[i-1]:
    	cnt += 1


print(cnt,end = " ")