#!/sw/bin/python2.7


import sys

# the original recursive code
def specialMath0(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return n + specialMath(n-1)	+ specialMath(n-2)

def specialMath(n):

    # zero and one are special cases.
    if(n==0):
        return 0
    elif(n==1):
        return 1

    # anything above zero is a recurrance.  This has an an equivalence function of
    # f(n) = (Fn + Ln)/2  which is nth Fibonanci sequence number and nth Lucas number.
    # However, it would be simpler to just calculate the result instead of implmenting
    # those routines for the purposes of a test.  See below:
    # https://www.wolframalpha.com/input/?i=f(n)%3Df(n-1)%2Bf(n-2)%2C+f(1)%3D1%2C+f(2)%3D2&lk=3
    # and
    # http://math.stackexchange.com/questions/536350/how-to-solve-recurrence-relation-fn-fn-1-2n-1-when-f1-1

    F = range(n)
    F[0] = 0
    F[1] = 1
    the_len = len(F)
    for i in xrange(2,the_len):
        F[i] = i + F[i-1] + F[i-2]

    # do it one more time since the "array" will be from 0-n-1
    return (n + F[n-1] + F[n-2])

print specialMath(int(sys.argv[1]))
#print specialMath0(17)
#print specialMath(17)
