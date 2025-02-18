from fractions import Fraction

def euclidian_aligorithm(big, small):
    while small:
        big, small = small, big % small
    
    return big

def lcm(a, b):
    # print(f"This is the sum of the denominators: {a*b} and this is the GCD of the denominators: {euclidian_aligorithm(a,b)}")
    # return a * b
    return (a*b)/euclidian_aligorithm(a,b)

def add_fractions():
    frac_1_numerator = int(input("What's the numerator of the first fraction?: "))
    frac_1_denominator = int(input("...and the denominator?: "))
    frac_1 = Fraction(frac_1_numerator, frac_1_denominator, _normalize = False)
    frac_2_numerator = int(input("What's the numerator of the second fraction?: "))
    frac_2_denominator = int(input("...and the denominator?: "))
    frac_2 = Fraction(frac_2_numerator, frac_2_denominator, _normalize = False)

    lcd = None
    if frac_1_denominator > frac_2_denominator:
        lcd = lcm((frac_1_denominator), frac_2_denominator)
    else:
        lcd = lcm(frac_1_denominator, frac_2_denominator)

    

add_fractions()