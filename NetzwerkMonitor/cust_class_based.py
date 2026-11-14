import time
from functools import wraps

class ExecutionTracker:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        # 1. We need a state variable to track total calls
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        start_time = time.perf_counter()
        
        try:
            # Execute the actual function
            return self.func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            print(f"[{self.func.__name__}] Call #{self.call_count} executed in {end_time - start_time:.4f}s")

# Let's combine this with a Custom Context Manager for resources
class NetworkConnection:
    def __enter__(self):
        print("🔌 Opening secure network socket...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 2. This handles clean up even if errors happen
        print("🔒 Safely closing network socket. Zero memory leaked.")
        if exc_type:
            print(f"⚠️ Handled error of type: {exc_type.__name__}")
            return True # Suppresses the exception
