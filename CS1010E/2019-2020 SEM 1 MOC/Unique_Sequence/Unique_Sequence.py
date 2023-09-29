def is_unique(seq):
    for i in range(len(seq)):
        for k in range(i+1,len(seq)):
            if seq[i] == seq[k]:
                return False
    return True

def complex_is_unique(seq):
    a = 0
    for i in seq:
        a+=1
    k = 0
    while k < a:
        j = k+1
        while j<a:
            if seq[k] == seq[j]:
                return False
            j += 1
        k += 1
    return True


seq = input()
print(is_unique(seq))
print(complex_is_unique(seq))
        
