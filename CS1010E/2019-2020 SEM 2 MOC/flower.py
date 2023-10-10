def rotate(bouquet, step):
    if step == len(bouquet) or step == 0:
        return bouquet
    else:
        if step > len(bouquet):
            new_bouquet = bouquet[step%len(bouquet):] + bouquet[:step%len(bouquet)]
            return new_bouquet
        elif step < len(bouquet):
            new_bouquet = bouquet[step:] + bouquet[:step]
            return new_bouquet

def flower_I(bouquet, k):
    line = ''
    while len(bouquet) != 0:
        bouquet = rotate(bouquet,k-1)
        line += bouquet[0]
        if len(bouquet) == 1:
            break
        else:
            bouquet = bouquet[1:]
    return line

def flower_R(bouquet,k):
    if len(bouquet) == 1:
        return bouquet[0]
    else:
        return rotate(bouquet,k-1)[0] + flower_R(rotate(bouquet,k-1)[1:],k)

def pink_rose(bouquet):
    k = 0
    while True:
        if flower_R(bouquet,k)[-1] == 'P':
            return k
        else:
            k += 1

bouquet = ("R", "P", "W", "W", "P", "R", "R", "R")
print(pink_rose(bouquet))
        
