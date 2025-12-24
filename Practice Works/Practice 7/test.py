import meanmod
import time
import random

def python_mean(lst):
    start_time = time.time()
    s = 0
    for x in lst:
        s += x
    result = s / len(lst)
    end_time = time.time()
    print(f"Python Time: {end_time - start_time:.5f}")
    return result

sizes = [10000, 500000, 1000000]

for n in sizes:
    print(f"--- Test for {n} elements ---")
    data = [random.random() * 100 for _ in range(n)]
    
    print("Calling C++:")
    res_cpp = meanmod.calculate_mean(data)
    print(f"Result: {res_cpp:.2f}")

    print("Calling Python:")
    res_py = python_mean(data)
    print(f"Result: {res_py:.2f}")
    print()