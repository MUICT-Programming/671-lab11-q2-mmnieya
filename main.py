n = int(input())
def summation(a,b,c) :
    for i in range(n) :
        sum = a[i] + b[i]
        c.append(sum)
    return sum
def find_min_max(a) :
    a.sort()
    print(f”({a[0]}, {a[n-1]})”)
    return a
lst1 = []
lst2 = []
update = []
for i in range(2*n) :
    num = int(input())
    if i <n :
        lst1.append(num)
    else :
        lst2.append(num)

summation(lst1,lst2,update)
print(update)
find_min_max(update)
