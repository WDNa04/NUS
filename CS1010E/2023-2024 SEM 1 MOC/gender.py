def how_many_female(faculty):
    count = 0
    for i in faculty:
        if i == 'F':
            count+= 1
    return count

def how_many_male(faculty):
    count = 0
    for i in faculty:
        if i == 'M':
            count += 1
    return count

def gender_balance(faculty):
    if how_many_female(faculty) == how_many_male(faculty):
        return 'balanced'
    elif how_many_female(faculty) > how_many_male(faculty):
        return 'female'
    else:
        return 'male'
        

engineering = 'MMFMFFMMF'
history = 'FFMMFFFFMFF'
business = 'FFFMMMFFMMFMFMFM'

print(gender_balance(engineering))
