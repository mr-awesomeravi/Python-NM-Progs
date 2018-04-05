#Ravi Rathee 16csu292
#Trapezoidal Rule
import math

def fx(x):
    #return 1/(1 + x**2 )
    return math.sqrt(1+x**4)

def trapezoidal(a,b,n):
    h = (b-a)/n
    print("h = : {}".format(h), end="\n\n")

    print( "{:>10}{:>10}".format( "x","f(x)" ) )
    print( "{:10.3}{:10.3}".format( float(a), float(fx(a)) ) )

    sum=0
    i = a+h
    while(i<b):
        print( "{:10.3}{:10.3}".format( i,fx(i) ) )
        sum+= fx(i)
        i += h


    print( "{:10.3}{:10.3}".format( float(b),float(fx(b)) ) )

    return (h/2.0)*(  ( fx(a)+fx(b) ) + 2*sum   )

a = int(input("Enter initial value of limit: ") )
b = int(input("Enter final   value of limit: ") )
n = int(input("Enter number of intervals   : ") )

answer = trapezoidal(a,b,n)
print("{:<10.5}".format(answer))

"""
Enter initial value of limit: 0
Enter final   value of limit: 6
Enter number of intervals   : 6
h = : 1.0

                 0.0                 1.0
                 1.0                 0.5
                 2.0                 0.2
                 3.0                 0.1
                 4.0              0.0588
                 5.0              0.0385
                 6.0               0.027
1.4107985813868167
"""
