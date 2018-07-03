def fibbonacci():
    pos = 0
    fib = [1, 2]
    next_val = 0
    while next_val < 4000000:
        next_val = fib[pos] + fib[pos+1]
        pos += 1
        fib.append(next_val)

    evens = [x for x in fib if x % 2 == 0]
    return sum(evens)


print(fibbonacci())
