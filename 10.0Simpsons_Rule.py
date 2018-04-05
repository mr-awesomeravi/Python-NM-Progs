#Ravi Rathee 16csu292
#Simpsons 3/8 Rule
def fx(x):
    return 1/(1 + x**2 )

def simpsons(a,b,n):
    h = (b-a)/n
    print("h = : {}".format(h), end="\n\n")


    print( "{:10}{:10.3f}{:10.3f}".format(int(0), float(a), float(fx(a)) ),end="\n\n" )

    mulof3 =0
    exceptmulof3 = 0
    i = a+h     #current_interval
    j = 1       #current_index_of_interval
    while(i<b):
        print( "{:10}{:10.3f}{:10.3f}".format( j, i , fx(i) ) )
        if(j%3==0):
            mulof3+= fx(i)
        elif(j%3!=0):
            exceptmulof3 += fx(i)

        j+=1
        i+=h

    print()
    print( "{:10}{:10.3}{:10.3}".format(j, float(b),float(fx(b)) ) )

    return (3.0*h/8.0)*(  ( fx(a)+fx(b) ) + 3*exceptmulof3  +2*mulof3  )

a = int(input("Enter initial value of limit: ") )
b = int(input("Enter final   value of limit: ") )
n = int(input("Enter number of intervals   : ") )

answer = simpsons(a,b,n)
print("{:<10.5}".format(float(answer)))

"""
Enter initial value of limit: 0
Enter final   value of limit: 6
Enter number of intervals   : 6
h = : 1.0

         0       0.0       1.0

         1       1.0       0.5
         2       2.0       0.2
         3       3.0       0.1
         4       4.0    0.0588
         5       5.0    0.0385

         6       6.0     0.027
1.3571
"""
