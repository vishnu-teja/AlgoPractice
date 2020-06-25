import urllib


def mergeArrays(a, f, m, l):
    global count
    fa = a[f: m]
    la = a[m: l]
    i = j = 0
    for k in range(f, l):

        if i < len(fa) and (j == len(la) or (fa[i]) < (la[j])):
            a[k] = fa[i]

            i += 1
        elif j < len(la) and (i == len(fa) or (fa[i]) > (la[j])):
            count += len(fa)-i
            a[k] = la[j]
            j += 1


def mergeSort(a, f, l):
    m = (l + f)//2
    if m > f:
        mergeSort(a, f, m)
        mergeSort(a, m, l)
        mergeArrays(a, f, m, l)


file = open('../data/unsorted.txt', 'r')
array = list(map(int, file.readlines()))
file.close()


count = 0
print(array)

mergeSort(array, 0, len(array))

print(count)
