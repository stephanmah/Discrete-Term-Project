#python instead
import sys
import numpy as np
print("Enter a positive nonzero integer")
user_number = int(input())
print(user_number)

my_generator = np.random.default_rng()
#randnums = np.random.randint(1, 26, user_number)
randnums1 = my_generator.integers(0, 100, size=user_number)
#listed_randnums = randnums.toList()
print(randnums1)
#print(type(randnums))

# Traverse through all array elements


def selection_sort(randnums):
    # i indicates how many items were sorted
    for i in range(len(randnums)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        #
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(randnums)-1):
            # Update the min_index if the element at j is lower than it
            if randnums[j] < randnums[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        randnums[i], randnums[min_index] = randnums[min_index], randnums[i]
# Driver code to test above
selection_sort(randnums1)
print("Selection sorted array")
for i in range(len(randnums1)):
    print("%d" % randnums1[i]),
