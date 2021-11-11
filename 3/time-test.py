import os
from timeit import timeit

# with open('C:/MinGW/bin/cpp/Python/lecture/readfile1.txt', 'a') as readfile:
#     i = 123761189
#     while os.path.getsize("C:/MinGW/bin/cpp/Python/lecture/readfile1.txt") <= 52428800:
#         readfile.write(str(i) + ' \n')
#         print(i)
#         i += 10

s = """
with open('C:/MinGW/bin/cpp/Python/lecture/readfile1.txt') as readfile:
    s = 0
    for line in readfile.readlines():
        if line.strip().isdigit():
            s += int(line)
"""
print(timeit(s, number = 10) / 10)

s = """
with open('C:/MinGW/bin/cpp/Python/lecture/readfile1.txt') as readfile:
    s = 0
    for line in readfile:
        if line.strip().isdigit():
            s += int(line)
"""
print(timeit(s, number = 10) / 10)

s = """
with open('C:/MinGW/bin/cpp/Python/lecture/readfile1.txt') as readfile:
    s = sum(int(line.strip()) for line in readfile if line.strip().isdigit())
"""
print(timeit(s, number = 10) / 10)