#Ravi Rathee 16csu292
#Simpsons 1/3 Rule
def fx(x):
    return 1/(1 + x**2 )

def simpsons(a,b,n):
    h = (b-a)/n
    print("h = : {}".format(h), end="\n\n")

    print( "{:>10}{:>10}{:>10}".format("index","x","f(x)" ) )
    print( "{:10}{:10.3}{:10.3}".format(0, float(a), float(fx(a)) ),end="\n\n" )

    oddsum =0
    evensum = 0
    i = a+h
    j=1
    while(i<b):
        print( "{:10}{:10.3}{:10.3}".format(j, i,fx(i) ) )
        if j%2==1:
            oddsum+= fx(i)
        elif j%2==0:
            evensum +=fx(i)
        i += h
        j+=1



    print()
    j+=1
    print( "{:10}{:10.3}{:10.3}".format(j, float(b),float(fx(b)) ) )

    return (h/3.0)*(  ( fx(a)+fx(b) ) + 4*oddsum  +2*evensum   )

a = int(input("Enter initial value of limit: ") )
b = int(input("Enter final   value of limit: ") )
n = int(input("Enter number of intervals   : ") )

answer = simpsons(a,b,n)
print("{:<10.5}".format(answer))

"""
Enter initial value of limit: 0
Enter final   value of limit: 6
Enter number of intervals   : 6
h = : 1.0

     index         x      f(x)
         0       0.0       1.0

         1       1.0       0.5
         2       2.0       0.2
         3       3.0       0.1
         4       4.0    0.0588
         5       5.0    0.0385

         7       6.0     0.027
1.3662 
"""
