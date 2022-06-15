def binSearch(a,k):
    l = 0
    h = len(a)-1

    while l<=h:
        mid = (l+h)//2
        if a[mid] == k:
            print(a.count(k))
            return mid
        elif a[mid]>k:
            h = mid-1
        else:
            l = mid+1
    return False

a = [3,6,8,12,14,17,25,29,31,36,42,42,47,53,55]
k = 42
print(binSearch(a,k))
        