def calculate_areas(w_list, h_list):
    dicta = {}
    for i in range(1,len(w_list)+1):
        for k in range(1,len(h_list)+1):
            a = (i+k-2) % 3
            dicta[(i,k)] = a
    zero_total = 0
    one_total = 0
    two_total = 0
    for i in dicta:
        if dicta[i] == 0:
            zero_total += w_list[i[0]-1] * h_list[i[1]-1]
        elif dicta[i] == 1:
            one_total += w_list[i[0]-1] * h_list[i[1]-1]
        else:
            two_total += w_list[i[0]-1] * h_list[i[1]-1]
    return (zero_total, one_total, two_total)

l4 = [i for i in range(100000)]
print(calculate_areas(l4,l4[::-1]))


            
