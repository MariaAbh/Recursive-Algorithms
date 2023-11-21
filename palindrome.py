def comp(a, b):
	global comp_counter
	comp_counter += 1
	return a == b

def pal(s):
	if not s:
		return True
	res_comp = comp(s[0], s[-1])
	if not res_comp:
		return False
	result = pal(s[1:-1])
	return result

tests = [
	"lamalamaghiamalamal",
	"laval",
	"titouan",
	"maria",
	"a",
	"aba",
	"abba",
]

for s in tests:
	comp_counter = 0
	r = pal(s)
	print(s,r,comp_counter)
	assert(r == (s == s[::-1]))
