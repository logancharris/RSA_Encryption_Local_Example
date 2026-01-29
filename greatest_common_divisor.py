
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
