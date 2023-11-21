import sys
m_n = {}
mem = {0:[1]}
def acker(m,n):
	k = (m,n)
	m_n[k] = m_n.get(k, 0) + 1
	if m not in mem:
		mem[m] = []
	if len(mem[m]) > n:
		return mem[m][n]

	if m == 0:
		res = n+1
	elif m > 0 and n == 0:
		res = acker(m-1,1)
	elif m > 0 and n > 0:
		for ni in range(len(mem[m]), n-1):
			acker(m, ni)
		v = acker(m, n - 1)
		res = acker(m-1,v)
	else:
		print("UNREACHABLE")
		exit(1)
	mem[m].append(res)
#	print(f'{m=}, {n=}, {len(mem[m])=}')
	assert(mem[m][n] == res)
	return res

a, b = map(int,sys.argv[1:])
r = acker(a, b)
print('calls', sum(m_n.values()))
for A in range(1+max(a for a,b in m_n)):
	print(A, max(b for a,b in m_n if a == A))

print(f'acker({a},{b})={r}')
