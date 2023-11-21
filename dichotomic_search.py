def dicho(l,e,start,end):
	middle = (start+end)//2
	print(l,e,start,end)
	if l[start] == e:
		return start
	if start == end-1:
		return -1
	if e <= l[middle]:
		return dicho(l,e,start+1,middle+1)
	else:
		return dicho(l,e,middle,end)

l = [1,2,4,7,10,15]
e = 7
start = 1
end = 5
print(dicho(l,e,start,end))
