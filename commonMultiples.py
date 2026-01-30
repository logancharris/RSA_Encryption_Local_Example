from decimal import *
#greatest common devisor
def gcd(a,b):
    gcd_found = False

    while not gcd_found:
        r = a%b

        if(r == 0):
            return b
        else:
            a = b
            b = r

#leastCommonMultiple
def lcm(a,b):
    leastCommonMultiple = int(Decimal(a*b) / Decimal(gcd(a,b)))

    return leastCommonMultiple