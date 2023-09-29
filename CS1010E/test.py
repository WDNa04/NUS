def matchResistors(R,n):
    lista = []
    listb = list(R)
    dicta = {}
    i = 0
    for i in listb:
        dicta[i] = listb.count(i)
    for i in range(len(dicta.keys())):
        dicta_keys = list(dicta.keys())
        a = dicta_keys[i]
        if n-a in dicta_keys and dicta_keys.index(n-a)>=i:
            for i in range(min(dicta[a],dicta[n-a])):
                lista.append([(a,n-a)])
    return lista
    

listc = list(map(int,input().split()))
R = tuple(listc)
n = int(input())
print(matchResistors(R,n))

75 80 90 77 88 91 60 74 73 70 55 93 59
    