"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import cProfile
import sys

def find_prime(nmbr):
    """
    function returns i-prime item
    :param nmbr: integer - number of prime item
    :return: integer

    complexity of function is: O(n^2)
    """

    if nmbr == 1:
        return 2
    if nmbr == 2:
        return 3
    prime_n = [2, 3]
    i = 4
    while len(prime_n) < nmbr:
        for j, item in enumerate(prime_n):
            if j == nmbr - 1:
                return item
            if i < item * 2:
                prime_n.append(i)
                i += 1
                break
            if i % item == 0:
                i += 1
                break
    return prime_n[-1]


def sieve_eratosthenes(max_value, nmbr):
    """
        function returns i-prime item
        :param maxValue: integer - max number to build up array of primes
        :param nmbr: integer - number of prime item
        :return: integer

        complexity of function is: O(n^2)
        """

    sieve = [0]*max_value
    i = 2
    while i*i < max_value:
        k = i*i
        if sieve[i] == 0:
            while k < max_value:
                sieve[k] = 1
                k += i
        i += 1
    result = []
    for j, item in enumerate(sieve):
        if j < 2:
            continue
        if item == 0:
            result.append(j)
    #print(result)
    return result[nmbr-1]

NUMB = int(input("Input number of simple item: "))

RESULT1 = find_prime(NUMB)

if RESULT1 < 10:
    MAX_VAL = 10
elif RESULT1 < 100:
    MAX_VAL = 100
elif RESULT1 < 500:
    MAX_VAL = 500
elif RESULT1 < 1000:
    MAX_VAL = 1000
else:
    print("Too big number entered. Try again.")
    sys.exit()
RESULT2 = sieve_eratosthenes(MAX_VAL, NUMB)

print(f"Result of function (find_prime) is {RESULT1}.")
print(f"Result of function (sieve_eratosthenes) is {RESULT2}.")
input("Start measuring. Press any key to measure find_prime().")
STR = f"find_prime({NUMB})"
cProfile.run(STR)
input("Press any key to measure sieveEratosthenes().")
STR = f"find_prime(sieve_eratosthenes({MAX_VAL}, {NUMB}))"
cProfile.run(STR)
