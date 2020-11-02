import sys
import numpy as np
import time

#Takes an integer as input
print("Enter a positive nonzero integer")
user_number = int(input())
print("This is array has", user_number, "numbers")


def bubble_sort(randnums):
    n = len(randnums)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if randnums[j] > randnums[j+1]:
                randnums[j], randnums[j+1] = randnums[j+1], randnums[j]


def print_array(randnums1):
    print("Bubble sorted array:")
    print(randnums1)


n = 0
running_time = 0
while (n < 1000):
    my_generator = np.random.default_rng()
    randnums1 = my_generator.integers(0, 100, size=user_number)
    start_time = time.time()
    #If you want to see the arrays before and after
    #print("Unsorted Array:")
    #print(randnums1)
    bubble_sort(randnums1)
    #print_array(randnums1)
    n = n + 1


end_time = time.time()
running_time = end_time - start_time
average_time = running_time / 1000

print("\nRunning Time: ", running_time)
print("\nAverage Bubble Sort Time: ", average_time)
