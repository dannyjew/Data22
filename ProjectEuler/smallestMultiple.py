import math

def finding_prime_factor(n):
    i = 2
    while i < math.sqrt(n):
        while n % i == 0:
            n = n / i
        i = i + 1
    print(n)
finding_prime_factor(600851475143)

non_int = input("here")
int(non_int)