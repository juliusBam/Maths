import math
import numpy as np
#Insert your population here:
Population = np.array([2, 4, 5, 7, 8])
Average = None
if (Population.dtype == 'float64' or Population.dtype == 'int64'):
#checks if every Element of the array is int or float
    Average = np.mean(Population)
    print(f'The average of the given population is {Average}')
    N = len(Population)
    print(f'The number of population elements is = {N}', end=". ")
    max = np.max(Population)
    print(f'The maximum value of the given population is {max}', end=". ")
    min = np.min(Population)
    print(f'The minimum value of the given population is {min}')
    Variance = np.var(Population)
    print(f'The variance of the given population is {Variance}', end=" and ")
    StandardDeviation = (Variance)**(1/2)
    print(f'the standard deviation of the given population is {StandardDeviation}')
else:
# if array doesn't have integers nor floats
    print('The array is not valid', end="")
