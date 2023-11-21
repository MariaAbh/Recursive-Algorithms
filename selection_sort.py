def minimum_list(l, start, end):
	if start == end-1:
		return l[start]
	mini = minimum_list(l, start+1, end)
	if l[start] < mini:
		return l[start]
	return mini

def tri_sel_2(l,start,end):
	if start == end-1:
		return [l[start]]
	mini = minimum_list(l,start+1,end)
	if l[start] > mini:
		index_m = l.index(mini)
		l[index_m],l[start] = l[start],mini
	return [l[start]] + tri_sel_2(l, start+1, end)

l = [6,4,5,3,1,2]
print(tri_sel_2(l,1,6))
