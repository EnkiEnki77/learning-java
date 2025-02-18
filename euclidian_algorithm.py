
def euclidian_aligorithm(big, small):
    while small:
        big, small = small, big % small
    
    return big

def lcm(a, b):
    # print(f"This is the sum of the denominators: {a*b} and this is the GCD of the denominators: {euclidian_aligorithm(a,b)}")
    # return a * b
    return (a*b)/euclidian_aligorithm(a,b)


print(f"The LCM is: {lcm(1042, 1376)}")