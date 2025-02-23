# parallel_numpy.py - Parallelized Implementation Using NumPy & Multiprocessing

import numpy as np
import time
from multiprocessing.dummy import Pool 


# Generate a large NumPy array
N = 10**6
data = np.random.randint(1, 100, size=N)

def square_chunk(arr):
    return np.sum(arr ** 2)  # Vectorized computation on chunks

def sum_of_squares_parallel(arr, num_workers=4):
    chunk_size = len(arr) // num_workers
    chunks = [arr[i * chunk_size : (i + 1) * chunk_size] for i in range(num_workers)]
    
    with Pool(processes=num_workers) as pool:
        results = pool.map(square_chunk, chunks)

    return sum(results)

start = time.time()
result = sum_of_squares_parallel(data)
end = time.time()

print(f"Sum of squares: {result}")
print(f"Execution Time (Parallel NumPy Version): {end - start:.5f} seconds")
