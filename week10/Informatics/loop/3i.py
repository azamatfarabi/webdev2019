
import math
x = int(input())
count = 0

for i in range(1,int(math.sqrt(x+1))):
	if x % i == 0:
		count += 1


if int(math.sqrt(x)*math.sqrt(x)) == x:
	count = count*2 - 1
else:
	count *= 2

print(count, end = " ")