def super_func(*args,
               **kwargs):  # Star allows multiple arguments to be passed and used as a single variable
    # within the function kwargs pass named variables as a dictionary (map)
    # Accepted style: pass regular params first, then *args, then default parameters, then **kwargs

    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))
