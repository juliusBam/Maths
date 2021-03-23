import math
n = 5
k = 4
if (n <= 0):
    print('n doesn\'t have a valid value, check your inputs')
elif (k < 0 or k > n):
    print('k doesn\'t have a valid value, check your inputs')
elif (n == k):
    print(f'Since n = k the binomial coefficient of {n} over {k} is: 1')
else:
    a = math.trunc(math.factorial(n)/(math.factorial(k) * math.factorial(n-k)))
    print(f'The binomial coefficient of {n} over {k} is: {a}')
