def prime_generator(count):
    primes = []
    num = 2
    while len(primes) < count:
        for i in primes:
            if num % i == 0:
                break
        else:
            primes.append(num)
            yield num
        num += 1


for prime in prime_generator(5):
    print(prime)
