import functools
def timer(fn):
    import time
    @functools.wraps(fn)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, *kwargs)
        end_time = time.time()
        print(f"{fn.__name__}: the runtime is {end_time - start_time}")
        return result
    return wrapper_timer

@timer
def sum_of_powers(n, p):
    my_list = [items ** p for items in range(1, n+1)]
    # print(my_list)
    return sum(my_list)

print(sum_of_powers(1000000, 2))
print(sum_of_powers(1000000, 3))
print(sum_of_powers(1000000, 5))
