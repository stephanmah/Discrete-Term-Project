import sys
import random
import numpy as np
from timeit import default_timer as timer

print("Enter a positive nonzero integer")
user_number = int(input())
print("This is array has", user_number, "numbers")
my_generator = np.random.default_rng()


def create_many_arrays(user_input):
    many_arrays = []
    list_of_lists = []
    for x in range(user_input):
        many_arrays.append(random.randint(1, 100))

    
    return many_arrays


for i in range(3):
    create_many_arrays(user_number)



running_time = 0
test_list = []


