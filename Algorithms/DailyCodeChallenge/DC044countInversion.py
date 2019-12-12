#Count the number of inversion required to make the array sorted

def merge(a_with_inv, b_with_inv):
    i,j=0,0
    a,a_inv = a_with_inv
    b,b_inv = b_with_inv
    inversion = a_inv+b_inv
    merged = list()

    while i<len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1

        elif a[i] > b[j]:
            merged.append(b[j])
            j += 1
            inversion += len(a[i:])

    while i<len(a):
        merged.append(a[i])
        i +=1
    while j<len(b):
        merged.append(b[j])
        j +=1

    return merged,inversion

def merge_sort(a):
    if not a or len(a) == 1:
        return a,0

    mid = len(a) //2
    merged_array , inversion = merge(merge_sort(a[:mid]),merge_sort(a[mid:]))
    return merged_array, inversion


def conversion(a):
    _ , inversion = merge_sort(a)
    return inversion

print (conversion([5,4,3,2,1]))
    
