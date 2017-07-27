def pwdchk(pwd):
	lenchk = False
	numchk = False
	upperchk = False
	lowerchk = False
	pwdl = list(pwd)
	pwdll = len(pwdl)
	i = 0
	if len(pwd) >= 10:
		lenchk = True
		for i in range(pwdll):
			if pwdl[i].isdigit():
				numchk = True
			elif pwdl[i].isalpha():
				if pwdl[i].isupper():
					upperchk = True
				else:
					lowerchk = True
		if lenchk and numchk and upperchk and lowerchk:
			return True
		else:
			i = i + 1
			return False
	else:
		return False