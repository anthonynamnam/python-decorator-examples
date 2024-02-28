from time import time 
from functools import cache  

@cache
def factorial(n): 
    if n == 1:
        return 1
    return n * factorial(n-1)

ts = time()
factorial(100)
te = time()
print(f"Calculation 1 completed in {(te-ts)*1000:.10f}ms\n") 
ts = time()
factorial(200)
te = time()
print(f"Calculation 2 completed in {(te-ts)*1000:.10f}ms\n")        
ts = time()
factorial(120)
te = time()
print(f"Calculation 3 completed in {(te-ts)*1000:.10f}ms\n") 