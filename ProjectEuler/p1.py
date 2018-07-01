def multiples(n):
    multi = [x for x in range(n) if x % 3 == 0 or x % 5 == 0]
    return sum(multi)


print(multiples(1000))
