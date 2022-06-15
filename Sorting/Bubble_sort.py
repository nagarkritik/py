def bubbleSort(a):
    for i in range(7):
        i= 0
        j = i+1
        swap = False
        while j<len(a):
            
            if a[i]>a[j]:
                a[i],a[j] = a[j],a[i]
                swap = True
            i+=1
            j+=1
        if swap == False:
            break

    return a

a = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(a))