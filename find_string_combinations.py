def toString(a):
    return ''.join(a)


def permute(a, l, r):
    if l == r:
        print(toString(a))
    for i in range(l, r+1):
        a[l], a[i] = a[i], a[l]
        permute(a, l+1, r)
        a[l], a[i] = a[i], a[l]


string = 'abcde'
permute(list(string), 0, len(string)-1)
