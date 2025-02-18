import math

def factor_pairs(num):
   
    factor_pairs_list = []

    for i in range(num + 1):
        for j in range(num + 1):
            if i * j == num and i <= j:
                factor_pairs.append((i, j))
    
    return factor_pairs_list
        
result = factor_pairs(23)

print(result) 

