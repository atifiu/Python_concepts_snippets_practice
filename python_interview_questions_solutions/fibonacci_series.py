### Interview question asked in Jan 2024 in Luxoft interview
# Create fibonacci series with series length provided as input parameter

def fibonacci_series(series_length):
    first_element = 0
    second_element = 1
    #series_length = 10
    #series = 1
    n = 3
    fib_series = [first_element, second_element]

    while n <= series_length:
        #print(n, fib_series)
        fib_series.append(fib_series[n-2] + fib_series[n-3])
        n += 1
        
    return fib_series

print(fibonacci_series(10))