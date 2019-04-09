
def election(s):
	if (int(s[0]) + int(s[1]) + int(s[2])) > 1:
		return 1
	else:
		return 0

if __name__ == '__main__':
	s = input().split(' ')
	print(election(s))