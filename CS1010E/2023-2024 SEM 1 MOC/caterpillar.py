def caterpillar(n):
    caterpillar = ''
    for i in range(n-1):
        caterpillar += 'Q'
    caterpillar += '6'
    return caterpillar

def caterpillar_with_backside(n):
    a = caterpillar(n)
    new_caterpillar = 'c'
    for i in a[1:]:
        new_caterpillar += i
    return new_caterpillar

print(caterpillar(4))
print(caterpillar_with_backside(4))
