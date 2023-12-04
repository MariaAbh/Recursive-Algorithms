def inserer(l,start,end):
    if start == end+1:
        return l
    if start == 0:
        return inserer(l,start+1,end)
    current = l[start]
    prev = l[start-1]
    if current < prev:
        temp = prev
        l[start-1] = current
        l[start] = temp
        return inserer(l,start-1,end)
    else:
        return inserer(l,start+1,end)
    

l = [6,4,1,3,5,2]
start = 0
end = 5
print(inserer(l,start,end))
