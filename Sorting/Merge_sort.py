"""
def merge(l,r,a):
    i = j = k = 0
    while(i<len(l) and j<len(r)):
        if(l[i] <= r[j] ):
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1

    while(i<len(l)):
        a[k] = l[i]
        i += 1
        k += 1

    while(j<len(r)):
        a[k] = l[j]
        j += 1
        k += 1   
    print(a)

def mergeSort(nums):
    n = len(nums)
    mid = n//2

    left = nums[:mid]
    right = nums[mid:]
    if n<2:
        return

    mergeSort(left)
    mergeSort(right)
    merge(left,right,nums)
    return nums


nums = [8,7,6,5,4,3]
print(mergeSort(nums))
"""

def merge_sort(arr):
    mid = len(arr)//2
    l1 = arr[:mid]
    r1 = arr[mid:]

    if mid<1:
        return

    merge_sort(l1)
    merge_sort(r1)
    merge(l1,r1,arr)
    return arr

def merge(l1,r1,nums):

    i=j=k = 0
    while i<len(l1) and j<len(r1):
        if l1[i]<r1[j]:
            nums[k] = l1[i]
            i+=1
        else:
            nums[k] = r1[j]
            j+=1
        k+=1

    while i<len(l1):
        nums[k] = l1[i]
        i+=1
        k+=1
    while j<len(r1):
        nums[k] = r1[j]
        j+=1
        k+=1
    

nums = [8,7,6,5,4,3]
print(merge_sort(nums))
