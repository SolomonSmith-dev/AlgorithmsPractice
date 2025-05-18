import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"⏱ Running {func.__name__}...")
        start_time = time.time()              # Start the timer
        result = func(*args, **kwargs)        # Run the function
        end_time = time.time()                # Stop the timer
        print(f"✅ {func.__name__} finished in {(end_time - start_time):.6f} seconds\n")
        return result                         # Return the result of the function
    return wrapper