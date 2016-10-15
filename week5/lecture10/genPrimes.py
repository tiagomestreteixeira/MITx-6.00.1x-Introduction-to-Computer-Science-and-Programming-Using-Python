def genPrimes():
    primes_list = []
    prime_candidate = 2
    while True:
        is_prime = True
        for elem in primes_list:
            if (prime_candidate % elem) == 0:
                is_prime = False
        if is_prime:
            primes_list.append(prime_candidate)
            yield prime_candidate
        prime_candidate += 1

a = genPrimes()
print(genPrimes())

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())