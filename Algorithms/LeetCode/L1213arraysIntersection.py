
#Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

def arraysIntersection(arr1,arr2,arr3):
    i,j,k = 0,0,0

    result = []
    while i<len(arr1) and j<len(arr2) and k< len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
            continue
        
        m = max(arr1[i],arr2[j],arr3[k])

        if arr1[i] < m:
            i +=1
        if arr2[j] < m:
            j +=1
        if arr3[k] < m:
            k +=1
    
    return result

print(arraysIntersection([1,2,3,4,5],[1,2,5,7,9],[1,3,4,5,8]))