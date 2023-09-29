def sum_digit_square_I(n):
    i = 10
    sum_number = 0
    while True:
        if n//i != 0:
            a = int(i/10)
            sum_number += int(((n%i-n%a)/a)**2)
            i *= 10
        elif n//i == 0:
            a = int(i/10)
            sum_number += int(((n%i-n%a)/a)**2)
            return int(sum_number)
        
def better_sum_digit_square_I(n):
    sum_number = 0
    while True:
        if n != 0:
            sum_number+=(n%10)**2
            n = n//10
        else:
            sum_number+=(n%10)**2
            return sum_number

def sum_digit_square_R(n):
    a = n%10
    if n//10 == 0:
        return a**2
    else:
        return a**2 + sum_digit_square_R(n//10)

def is_happy_number(n):
    while n>=10:
        n = sum_digit_square_R(n)
    if n < 10:
        if n == 1 or n == 7:
            return True
        else:
            return False

def all_happy_numbers(n,m):
    lista = []
    for i in range(n,m+1):
        if is_happy_number(i) == True:
            lista.append(i)
    return lista

n = int(input())
print(new_sum_digit_square_I(n))



