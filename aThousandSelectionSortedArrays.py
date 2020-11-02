import sys
import numpy as np
import time

#Takes an integer as input
print("Enter a positive nonzero integer")
user_number = int(input())
print("This is array has", user_number, "numbers")


def selection_sort(randnums):
    for i in range(len(randnums)-1):
        min_index = i
        for j in range(i+1, len(randnums)-1):
            if randnums[j] < randnums[min_index]:
                min_index = j
        randnums[i], randnums[min_index] = randnums[min_index], randnums[i]


def print_array(randnums1):
    print("Selection sorted array:")
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
    selection_sort(randnums1)
    #print_array(randnums1)
    n = n + 1


end_time = time.time()
running_time = end_time - start_time
average_time = running_time / 1000

print("\nRunning Time: ", running_time)
print("\nAverage Selection Sort Time: ", average_time)
