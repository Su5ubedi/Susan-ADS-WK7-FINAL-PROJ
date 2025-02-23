# optimized_numpy.py - Optimized Implementation Using NumPy

import numpy as np
import time

# Generate a large NumPy array of random numbers
N = 10**6
data = np.random.randint(1, 100, size=N)

def sum_of_squares_np(arr):
    return np.sum(arr ** 2)  # Vectorized computation

start = time.time()
result = sum_of_squares_np(data)
end = time.time()

print(f"Sum of squares: {result}")
print(f"Execution Time (Optimized NumPy Version): {end - start:.5f} seconds")
