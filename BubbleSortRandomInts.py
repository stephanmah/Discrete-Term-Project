import sys
import numpy as np

#Takes an integer as input
print("Enter a positive nonzero integer")
user_number = int(input())
print("This is array has", user_number, "numbers")

my_generator = np.random.default_rng()
randnums1 = my_generator.integers(0, 100, size = user_number)
print (randnums1)


def bubbleSort(randnums):
    n = len(randnums)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if randnums[j] > randnums[j+1]:
                randnums[j], randnums[j+1] = randnums[j+1], randnums[j]

bubbleSort(randnums1)

print("Bubble sorted array:")
for i in range(len(randnums1)):
    print("%d" % randnums1[i]),
