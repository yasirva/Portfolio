from math import sqrt

def factors(N):
    a = N
    factors = []
    i = 2
    while i<=sqrt(N):

        if a%i==0:
            a /= i
            factors.append(i)
            if a==1:
                break
        else:
            i += 1
    return factors
