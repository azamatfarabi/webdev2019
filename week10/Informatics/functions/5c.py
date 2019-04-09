
def xor(s):
	if s[0]!= s[1]:
		return 1
	else:
		return 0


if __name__ == '__main__':
	s = input().split(' ')
	print(xor(s))