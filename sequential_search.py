def seq_search(my_list,elem,start,end):
	if start == end:
		return -1
	if my_list[start] == elem:
		return start
	else:
		return seq_search(my_list,elem,start+1,end)

l = [1,2,5,10,7]
e = 2
start = 0
end = 1
result = seq_search(l,e,start,end)
print(result)
