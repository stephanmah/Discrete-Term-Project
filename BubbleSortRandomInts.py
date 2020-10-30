#python instead
import sys
import numpy as np
print("Enter a positive nonzero integer")
user_number = int(input())
print(user_number)

my_generator = np.random.default_rng()
#randnums = np.random.randint(1, 26, user_number)
randnums1 = my_generator.integers(0, 100, size = user_number)
#listed_randnums = randnums.toList()
print (randnums1)
#print(type(randnums))


#rewrite
def bubbleSort(randnums):
    n = len(randnums)

    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if randnums[j] > randnums[j+1]:
                randnums[j], randnums[j+1] = randnums[j+1], randnums[j]


bubbleSort(randnums1)

print("Bubble Sorted array:")
for i in range(len(randnums1)):
    print("%d" % randnums1[i]),



