def make_bouquet(shop, number):
    target = number - 3
    if target == 0:
        return True
    i = 0
    for k in shop:
        if k[1] <= target:
            target -= k[1]
            i += 1
            if k[1] == target and i == 0:
                return True
            elif i > 2:
                return False
            elif target == 0:
                return True
    return False

def minimum_cost(shop, number):
    if make_bouquet(shop, number) == True:
        target = number - 3
        if target == 0:
            return 1
        lista = []
        for k in range(3):
            if shop[k][1] + shop[k+1][1] == target:
                lista.append((shop[k],shop[k+1]))
            elif shop[k][1] == target or shop[k][1] * 2 == target:
                lista.append(shop[k])
        if shop[3][1] == target:
            lista.append((shop[3],1))
        elif shop[3][1] * 2 == target:
            lista.append((shop[3],2))
        listb = []
        for i in lista:
            if i[1] == 1:
                listb.append(2)
            elif i[1] == 2:
                listb.append(4)
            else:
                listb.append(i[0][2] + i[1][2])
        return min(listb) + 4
    else:
        return -1
        

flowers_r_us = [("R", 5, 3), ("R", 3, 2), ("W", 4, 3), ("W", 2, 2), ("P", 3, 4)]

print(minimum_cost(flowers_r_us, 2))
