
def format_number(n, m):
    sn = '0' * (abs(m - len(str(n)))) + str(n)
    return sn


def multiply_numbers(num1, num2):
    if len(num1) == 1:
        return int(num1) * int(num2)
    else:
        n = len(num1)
        mid = n // 2
        max_len = max(mid, n-mid)
        max_len += max_len//2
        a = format_number(num1[0: mid], max_len)
        b = format_number(num1[mid: n], max_len)
        c = format_number(num2[0: mid], max_len)
        d = format_number(num2[mid: n], max_len)
        print(a, b, c, d)

        ac = multiply_numbers(a, c)
        bd = multiply_numbers(b, d)

        max_len2 = max(len(str(int(a) + int(b))), len(str(int(c) + int(d))))
        max_len2 += max_len2//2
        ab = format_number(int(a) + int(b), max_len2)
        cd = format_number(int(c) + int(d), max_len2)
        adbc = multiply_numbers(ab, cd) - ac - bd
        print(ac, adbc, bd)
        return ac * (10**n) + adbc * (10**mid) + bd


a = 999
b = 432
ml = max(len(str(a)), len(str(b)))
ml += ml//2
sa = format_number(a, ml)
sb = format_number(b, ml)
print(sa, sb)
m = multiply_numbers(sa, sb)

print('karat', m)

print('coret', a*b)
