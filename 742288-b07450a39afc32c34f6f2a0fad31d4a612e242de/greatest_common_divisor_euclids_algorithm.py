#!usr/bin/python

# Author - Sudheer Satyanarayana, http://techchorus.net
# Greatest common divisor using Euclid's algorithm
# Python 2.6 has Fractions module, see Fractions.gcd(a, b)

def gcd(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        m = n
        n = r
        return gcd(m, n)
        
print "The greatest common divisor of 8 and 12 is %s"%gcd(8, 12) # 4
print "The greatest common divisor of 180 and 48 is %s"%gcd(180, 48) # 13
