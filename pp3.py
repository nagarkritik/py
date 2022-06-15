
n = 1634
t = n
l = 0
while t:
    t = t//10
    l+=1

s = 0

t1 = n

while t1:
    r = t1%10
    t1 = t1//10

    s += r**l

if s==n:
    print("True")
else:
    print("False")












