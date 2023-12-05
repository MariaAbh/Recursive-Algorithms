def tri_fusion(l,start,m,end):
    if start == end-1:
        return l[start:end]
    part1 = tri_fusion(l,start,(start+m)//2,m)
    part2 = tri_fusion(l,m,(m+end)//2,end)

    return fusion(part1,part2)

def fusion(l1,l2):
    merged = []
    i = 0
    j = 0
    while i<len(l1) and j<len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    for x in range(i,len(l1)):
        merged.append(l1[x])
    for y in range(j,len(l2)):
        merged.append(l2[y])

    return merged

l = [6,4,1,3,5,2]
print(tri_fusion(l,0,3,7))
