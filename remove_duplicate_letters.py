def remove_duplicate_letters(a):
    s = []
    for i in range(0, len(a)):
        if len(s) > 0 and s[-1] == a[i]:
            s.pop(-1)
        else:
            s.append(a[i])
    return ''.join(s)


string = 'f54321ff12345  '
print(remove_duplicate_letters(list(string)))
