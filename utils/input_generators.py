import random

def generate_random_list(size, min_val=0, max_value=10000):
    """
    Generates a list of random integers.
    - size: number of elements
    - min_val: minimum possible value
    - max_val: maximum possible value
    """
    return [random.randint(min_val, max_value) for _ in range(size)]