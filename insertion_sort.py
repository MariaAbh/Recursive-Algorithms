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
    
def tri_insertion(l,start,end):
    if start == end+1:
        return 
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

start = 0
end = 5

l = [6,4,1,3,5,2]
print('inserer:',inserer(l,start,end))

l1 = [6,4,1,3,5,2]
l1.sort()
print('l.sort():',l1)

l2 = [6,4,1,3,5,2]
tri_insertion(l2,start,end)
print('tri_insertion:',l2)
