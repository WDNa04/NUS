def binom_coeff(n,k):
    multi_n_k = 1
    for i in range(n-k+1, n+1):
        multi_n_k *= i
    multi_k = 1
    for i in range(1,k+1):
        multi_k *= i
    return int(multi_n_k / multi_k)

print("hello")