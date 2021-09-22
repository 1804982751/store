def ppp(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
print("排序前的数组", a)
ppp(a)

print("排序后的数组:")
for i in range(len(a)):
    print("%d" % a[i]),