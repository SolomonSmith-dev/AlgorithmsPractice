import sys
import os

# Add the parent directory (project root) to the module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils.timer import timeit
from utils.input_generators import generate_random_list

@timeit
def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.
    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1


        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    print("Before:", arr)
    insertion_sort(arr)
    print("After:", arr)

# === BONUS: Benchmark on larger input sizes ===
sizes = [10, 100, 1000, 2000]  # We'll stop short of 10,000 for now since it's slow

for size in sizes:
    test_arr = generate_random_list(size)
    print(f"\nBenchmarking insertion sort with input size: {size}")
    insertion_sort(test_arr)
