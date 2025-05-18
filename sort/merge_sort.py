import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Add the parent directory (project root) to the module search path
from utils.timer import timeit

@timeit
def merge_sort(arr):
    """
    Recursively sorts an array using the merge sort algorithm.
    This version returns a new sorted list.
    """

    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) > 1:
        return arr
    
    # Divide: split the array into two halves

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer: merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    """
    merged = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from both halves
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Test and benchmark the merge_sort function

if __name__ == "__main__":
    from utils.input_generators import generate_random_list

    sizes = [10, 100, 1000, 2000, 4000, 8000]
    for size in sizes:
        arr = generate_random_list(size)
        print(f"\nBenchmarking merge sort with input size: {size}")
        merge_sort(arr)

