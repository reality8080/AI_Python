import numpy as np
import timeit

def MEAN(a:np.array):
    SUM=0
    for i in a:
        SUM+=i
    return SUM/len(a)
    


matrix1=np.array(
    [189, 170, 189, 163, 183, 171, 185, 186, 173, 183, 173, 175, 178, 175, 183, 173,
174, 183, 163, 178, 170, 178, 182, 178, 173, 178, 183, 173,
177, 185, 188, 183, 185, 182, 191,182]
)

h=np.mean(matrix1)
execution_time_h1 = timeit.timeit('MEAN(matrix1)', globals=globals(), number=10)
execution_time_h2 = timeit.timeit('h', globals=globals(), number=10)
print(execution_time_h1,execution_time_h2)
sd=np.std(matrix1)
MIN=np.min(matrix1)
MAX=np.max(matrix1)


# print(f"Mean: {h}")
# print(f"standard deviation: {sd}")
# print(f"Minimum: {MIN}")
# print(f"Maximum: {MAX}")
