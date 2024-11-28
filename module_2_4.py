numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
is_prime = 0
for is_prime in numbers:
    primes.append(is_prime)
    for i in range(2,is_prime):
        if is_prime % i == 0:
            not_primes.append(is_prime)
            primes.remove(is_prime)
            break
primes.remove(1)
print(primes)
print(not_primes)
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for i in numbers:
    if i==1:
        continue
    if i % 2 == 0 or i % 3 == 0:
        if i<4:
            primes.append(i)
        else:
            not_primes.append(i)
    else:
        primes.append(i)
print(primes)
print(not_primes)
'''
#смог решить двумя способами один из которых с помощью вложенного цикла,а второй с помощью одного цикла, хотелось бы посмотреть на ваш код как быстрее и правильнее решить это задачу


