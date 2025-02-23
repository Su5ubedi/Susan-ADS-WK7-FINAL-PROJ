# baseline.py - Inefficient Implementation (Python Lists & Loops)

import random
import time

# Generate a large list of numbers
N = 10**6
data = [random.randint(1, 100) for _ in range(N)]

def sum_of_squares(lst):
    result = []
    for x in lst:
        result.append(x * x)  # Compute squares
    return sum(result)

start = time.time()
result = sum_of_squares(data)
end = time.time()

print(f"Sum of squares: {result}")
print(f"Execution Time (Baseline Version): {end - start:.5f} seconds")
