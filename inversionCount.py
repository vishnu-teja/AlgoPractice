import urllib


def mergeArrays(a, f, m, l):
    global count
    fa = a[f: m ]
    la = a[m: l]
    i = j = 0
    for k in range(f, l):
        if i< len(fa) and (j == len(la) or (fa[i]) < (la[j])):
            a[k] = fa[i]
            i+=1
        elif j< len(la) and (i == len(fa) or (fa[i]) > (la[j])):
            count +=1
            a[k] = la[j]
            j+=1
        


def mergeSort(a, f, l):
    m = (l + f)//2
    if m > f:
        mergeSort(a, f, m)
        mergeSort(a, m, l)
        mergeArrays(a, f, m, l)
        


link = "https://d3c33hcgiwev3.cloudfront.net/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt?Expires=1591056000&Signature=LPJUeI3nyYAsdE0oNC1xi-7~zTXI78VPIpgPzHCHVp7Dmo4doFUSRXgyqkzya2CB9FPbJEDIA767uA0B~vDW1lYxZ4ql83qe26c8-a3qSWNL7WAPidXAYURyQxxTQTZgs06XbkM31MQfyhG1Ea~t~ji2SXkhZ-n9SQk6qkI83ro_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
f = urllib.urlopen(link)
myfile = str(f.read())

values = myfile.split('\r\n')
values = values[:-1]
values = [int(i) for i in values]

count = 0


mergeSort(values, 0, len(values))

print(count)
