import random

print("Enter a positive nonzero integer")
user_number = int(input())
print("This is array has", user_number, "numbers")


def create_many_arrays(user_input):
    many_arrays = []
    list_of_lists = []
    for x in range(user_input):
        many_arrays.append(random.randint(1, 100))

    return many_arrays


def bubble_sort(randnums):
    n = len(randnums)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if randnums[j] > randnums[j+1]:
                randnums[j], randnums[j+1] = randnums[j+1], randnums[j]


bubble_sort(create_many_arrays(user_number))

print("Bubble sorted array:")
for i in range(len(randnums1)):
    print("%d" % randnums1[i]),
