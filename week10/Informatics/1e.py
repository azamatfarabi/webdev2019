import math

v = int(input())
t = int(input())

s = math.fabs(v*t) % 109

if v >= 0:
 	res = s % 109
else:
 	res = (109 - s) % 109

print(int(res))