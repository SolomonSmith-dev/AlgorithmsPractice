import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from utils.input_generators import generate_random_list
from sort.merge_sort import merge_sort
from sort.insertion_sort import insertion_sort
from sort.merge_sort import merge_sort
import time

input_sizes = [10, 100, 500, 1000, 2000,]
insertion_times = []
merge_times = []

for size in input_sizes:
    print(f"Benchmarking with input size: {size}")
    test_data = generate_random_list(size)

    # Time insertion sort
    data1 = test_data.copy()
    start = time.time()
    insertion_sort(data1)
    end = time.time()
    insertion_times.append(end - start)

    # Time merge sort
    data2 = test_data.copy()
    start = time.time()
    merge_sort(data2)
    end = time.time()
    merge_times.append(end - start)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, insertion_times, label='Insertion Sort', marker='o')
plt.plot(input_sizes, merge_times, label='Merge Sort', marker='o')

plt.title('Insertion Sort vs Merge Sort Performance')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)

# Save the plot and show it
plt.savefig('sort/benchmark_plot.png')
plt.show()