import numpy as np
import pandas as pd  

# create an array consisting of linearly spaced elements between 0 to 9
arr = np.linspace(0,9, 10)
print(arr)

# replace all odd numbers without modifying the original
newarr = np.where(arr % 2 != 0, -1, arr)
print(newarr)

# reshaping to a 2-d array
tdarr = arr.reshape(2,5)
print(tdarr)

total = 0
# sum of all
for i in arr:
    total = total + i

print (total)