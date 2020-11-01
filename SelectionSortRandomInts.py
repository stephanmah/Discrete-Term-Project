import sys
import numpy as np

#Takes an integer as input
print("Enter a positive nonzero integer")
user_number = int(input())
print("This is array has",user_number,"numbers")

my_generator = np.random.default_rng()
randnums1 = my_generator.integers(0, 100, size=user_number)
print(randnums1)


def selection_sort(randnums):
    for i in range(len(randnums)-1):
        min_index = i
        for j in range(i+1, len(randnums)-1):
            if randnums[j] < randnums[min_index]:
                min_index = j
        randnums[i], randnums[min_index] = randnums[min_index], randnums[i]

selection_sort(randnums1)

print("Selection sorted array")
for i in range(len(randnums1)):
    print("%d" % randnums1[i]),