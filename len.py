def my_len(s):
	if not s:
		return 0
	return 1 + my_len(s[:-1])

l = ['toto','maria','hello','lenght_of_a_string']
for st in l:
	print(st, my_len(st))
