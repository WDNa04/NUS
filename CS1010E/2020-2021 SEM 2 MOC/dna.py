def dna_transcription_I(dna):
    line = ''
    for i in dna:
        if i == 'A':
            line += 'U'
        elif i == 'G':
            line += 'C'
        elif i == 'C':
            line += 'G'
        else:
            line += 'A'
    return line

def dna_transcription_R(dna):
    if len(dna) == 1:
        if dna == 'A':
            return 'U'
        elif dna == 'G':
            return 'C'
        elif dna == 'C':
            return 'G'
        elif dna == 'T':
            return 'A'
    else: 
        if dna[0] == 'A':
            return 'U' + dna_transcription_R(dna[1:])
        elif dna[0] == 'G':
            return 'C' + dna_transcription_R(dna[1:])
        elif dna[0] == 'C':
            return 'G' + dna_transcription_R(dna[1:])
        elif dna[0] == 'T':
            return 'A' + dna_transcription_R(dna[1:])

def rna_segment(rna):
    cut_rna = ''
    for i in range(len(rna)):
        if rna[i]+rna[i+1] == 'UU' or rna[i]+rna[i+1] == 'UG':
            new_rna = rna[i:]
            break
    for i in range(len(new_rna)):
        if new_rna[i] + new_rna[i+1] == 'AC' or new_rna[i] + new_rna[i+1] == 'AA':
            if len(new_rna[:i+2])%2 == 0:
                cut_rna = new_rna[:i+2]
                break
    return cut_rna

def poly_property(poly):
    dict_amino = {'F': 'acidic', 'S': 'polar', 'Y': 'polar', 'Q': 'acidic', 'L': 'non-polar', 'P': 'acidic', 'O': 'non-polar', 'C': 'basic', 'M': 'basic', 'T': 'polar', 'A': 'basic', 'R': 'basic'}
    count_acid = 0
    count_polar = 0
    count_basic = 0
    count_non = 0
    for i in poly:
        if i not in dict_amino.keys():
            return 'Neutral'
        else:
            if dict_amino[i] == 'acidic':
                count_acid += 1
            elif dict_amino[i] == 'polar':
                count_polar += 1
            elif dict_amino[i] == 'basic':
                count_basic += 1
            elif dict_amino[i] == 'non-polar':
                count_non += 1
    if count_acid > count_basic:
        return 'Acidic'
    elif count_acid < count_basic:
        return 'Basic'
    elif count_acid == count_basic and count_polar > count_non:
        return 'Polar'
    else:
        return 'Neutral'
        

def auspicious_number(n,bad):
    count = 0
    if n == 1:
        for i in range(1,10):
            for k in str(i):
                if int(k) in bad:
                    count += 1
    else:
        for i in range(10**(n-1), 10**n):
            for k in str(i):
                if int(k) in bad:
                    count += 1
                    break
    return 10**n-10**(n-1) - count


def efficient_auspicious_number(n,bad):
    list_number = []
    for i in range(10**(n-1), 10**n):
        list_number.append(i)
    return list_number


n = int(input())
bad = []
while True:
    a = int(input())
    if a != -1:
        bad.append(a)
    else:
        break
print(efficient_auspicious_number(n,bad))







