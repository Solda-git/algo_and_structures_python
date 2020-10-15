"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
from  hashlib import sha1

INPUT_STRING = input("Input string in low case: ")
SUBSTRINGS = []
UNIQUE = set()
UNIQUE_HASH = set()
i = 0
while i < len(INPUT_STRING):
    for j in range(i, len(INPUT_STRING)):
        if len(INPUT_STRING[i:j+1]) == len(INPUT_STRING):
            break
        SUBSTRINGS.append(INPUT_STRING[i:j+1])
        UNIQUE.add(INPUT_STRING[i:j+1])
        UNIQUE_HASH.add(sha1(INPUT_STRING[i:j+1].encode('utf-8')).hexdigest())
    i += 1

print(SUBSTRINGS)
print(UNIQUE)
print(f"Number of different substrings are {len(UNIQUE_HASH)}:\n{UNIQUE_HASH}.")

