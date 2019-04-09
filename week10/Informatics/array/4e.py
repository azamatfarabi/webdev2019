
n = int(input())
cnt = 0
arr = [int(x) for x in input().split()]
ok = False
for i in range(1,n):
    if arr[i]*arr[i-1] > 0:
    	ok = True
    	break

if ok:
	print("YES")
else:
	print("NO")