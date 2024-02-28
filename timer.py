from time import time 
  
def my_timer(func): 
    # This function shows the execution time of the function object passed 
    def wrapper(*args, **kwargs): 
        ts = time() 
        res = func(*args, **kwargs) 
        te = time() 
        print(f"Function {func.__name__} executed in {(te-ts):.4f}s") 
        return res 
    return wrapper 
  
@my_timer
def long_calculation(): 
    print(f"Calculating...")
    for i in range(5000): 
        for j in range(i): 
            i+j*2
    print(f"Done!")
  
long_calculation() 