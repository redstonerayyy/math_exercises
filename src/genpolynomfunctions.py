import random
import time
import sys
from decimal import Decimal as D

# set pseudorandom generator with current time
now = time.time()
random.seed(now)

# random number between min, max with an additional floating point digit
# rounded to 1/10
def gen_number(min, max):
    # use decimal module to prevent floating point errors
    # so 0.1 is not displayed as 0.0.99999999999998
    num = random.randrange(min, max + 1) + round(D(random.random()), 1)
    return  num 

# generate exponential factor and exponential
def gen_exponential(exp, f1, f2):
    factor = 0
    while factor in [0]:
        factor = gen_number(f1, f2)

    exponential = exp if exp or exp == 0 else random.randint(1, 5)

    return [factor, exponential]

"""
f(x) = a(n)x^k + a(n-1)x^k-1 ... a(1)x + a(0)  
degrees - degrees of polynomal function
only rational numbers, rounded to first after floating point
exponent is natural number
fractions included
min,max are +/- 1 because of number generation
"""
def gen_function(degree, amin=-2, amax=3):
    if degree < 0:
        return False
    # generate which parts should be generated
    parts = []
    for _ in range(degree + 1):
        parts.append(random.randint(0, 1))

    # generate an exponential function for each part
    exponentfunctions = []
    for index in range(len(parts)):
        if parts[index]:
            exponentfunctions.append(gen_exponential(index, amin, amax))

    # convert to int if it is int
    for func in exponentfunctions:
        if float(func[0]).is_integer():
            func[0] = int(func[0])
        if float(func[1]).is_integer():
            func[1] = int(func[1])

    # generate an output string
    funcstring = ""
    # add the first element without x, because it is a(0)
    if parts[0]:
        # add and delete from array
        funcstring = f"{exponentfunctions[0][0]}"
        del exponentfunctions[0]
    # in reverse order add the functions so the smaller ones are added first
    for func in exponentfunctions[::1]:
        if funcstring:
            funcstring = " + " + funcstring
        if func[0] in [1]:
            funcstring = f"x^{func[1]}" + funcstring
        else:
            funcstring = f"{func[0]}x^{func[1]}" + funcstring

    return funcstring


def add_latex_formatting(func, num):
    return f"{num}) f(x) = ${func}$"

# argv for filename, function count and min,max degree
# e. g. python [this file] 1 100 -3 3
if __name__ == "__main__":
    with open(f"functions{int(sys.argv[1])}.txt", "w") as file:
        funcs = []
        for i in range(int(sys.argv[2])):
            while True: # prevent empty functions
                func = gen_function(4, int(sys.argv[3]), int(sys.argv[4]))
                if func != "" and (not func in funcs): # prevent empty and double
                    break
            funcs.append(func) # prevent doubles
            func = add_latex_formatting(func, i + 1)
            file.write(func + "\n\n") # double newline for LATEX