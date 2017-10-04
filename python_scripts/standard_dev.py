# standard_deviation_function .

def standard_dev(x):
    import pandas as pd
    import numpy as np
    mean = x.mean()
    variance = 0 
    for n in x:
        difference = n - mean 
        square_diff = difference **2 
        variance+= square_diff 
    total_var = variance / len(x)
    stand_dev = total_var ** (1/2) 
    return stand_dev 
  
 
