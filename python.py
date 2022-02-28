# 28-02-2022
# 1
def multiples_of_3_or_5():
    sum = 0
    for i in range(1000): 
        if i % 3 == 0 or i % 5 == 0: sum += i
    return sum

# 2
def even_fibonacci_numbers():
    total = 0
    p0 = 0
    p1 = 1
    fib = 0

    while fib <= 4000000: 
        p0 = p1
        p1 = fib
        fib = p0 + p1
        print(fib)
        if fib % 2 == 0: total += fib


    # total = 0
    # p0 = 0
    # p1 = 1
    # fib = 0
    # for i in range(24): 
    
    #     p0 = p1
    #     p1 = fib
    #     fib = p0 + p1
    #     if fib % 2 == 0: total += fib


    
    #     # # check 4 million
    #     # fib = p0 + p1
    #     # # check even
    #     # if fib <= 4000000:
    #     #     if fib % 2 == 0: total += fib
    #     #     print(fib)
    #     #     p0 = p1
    #     #     p1 = fib
    #     # else:
    #     #     break
            
    return total



