import math

# When testing if a number is prime you only need to test possible divisors up to the square root of the number your testing.
# Once you start testing numbers above the square root you start getting to repeat divisors.
# You cut down on run time of the algorithm by cutting down number of possible divisors to test.
def testPrime(num):
    sqrtn = math.sqrt(num)
    sqrtnint = int(sqrtn)

    numIsComposite = False
    numIsPrime = False 
    
    for x in range(2,(sqrtnint+1)):
        if(num%x ==0):
            numIsComposite = True
            break 
    
    if not numIsComposite: 
        numIsPrime = True

    return numIsPrime
