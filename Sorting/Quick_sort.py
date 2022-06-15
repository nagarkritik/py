import random
def randPartition(x, st, en):
    a = random.randint(st, en)
    x[a], x[en] = x[en], x[a]
    pindex = partition(x, st, en)
    return pindex

def partition(x, st, en):
    piv = x[en]

    pindex = st

    for i in range(st,en):
        if(x[i] <= piv):
            x[pindex], x[i] = x[i], x[pindex]
            pindex += 1

    x[pindex], x[en] = x[en], x[pindex]
    return pindex

def quick(x, st, en):

    if st<en:
        pi = randPartition(x,st,en)
        quick(x,st,pi-1)
        quick(x,pi+1,en)

    return x


nums = [7,2,1,6,8,5,3,4]
print(quick(nums, 0, 7))