def every_factor(num):
    # We want each item to be unique, no duplicates, so we use a set
    factors = set()

    # We want to check if num is divisible by every number up to its sqrt. Sqrt can be calculated by raising the num to
    # the power of .5.
    for d in range(1, int(num ** 0.5) + 1):
        # checking if num is divisible by a number
        if num % d == 0:
            # if divisible, add the number and add the quotient of num and the number to the set
            factors.add(d)
            factors.add(num // d)
    
    # return the set sorted from least to greatest.
    return sorted(factors)

result = every_factor(12)

print(result)