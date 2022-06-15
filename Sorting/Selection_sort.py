def selection_sort(a):
    i = 0
    while i<len(a)-1:
        j = i+1
        while j<len(nums):
            if a[i]>=a[j]:
                a[i],a[j] = a[j],a[i]
            j+=1
        i+=1
    return nums

nums = [11,25,12,22,64]
print(selection_sort(nums))

