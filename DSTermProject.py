#python instead
import numpy as np
print("Enter a positive nonzero integer")
user_number = int(input())
print(user_number)

randnums = np.random.randint(1,26,user_number)
print(randnums)
print(type(user_number))
