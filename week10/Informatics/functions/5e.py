
def prime(n):
	ok = True
	for i in range(2,n):
		if n % i == 0:
			ok = False

	if ok == True:
		return 'prime'
	else:
		return 'composite'


if __name__ == '__main__':
	n = int(input())
	print(prime(n))