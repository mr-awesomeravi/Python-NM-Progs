#Ravi Rathee 16csu292
#Modified Eulers Method
def fxy(x,y):
    #return x+y+x*y
    return x+y**2
def eulers(x,y,xn,n):
    h = (xn - x) / n     #step size
    print("value of h : {:4.4}".format(h))
    a=x
    b=y
    print("               {:>10}{:>10}".format('x','y'))

    i=0
    while(i<n):
        print("Simple Euler   {:10.4f}{:10.4f}".format(x,y))
        a = x
        b = y
        y = y + h*fxy(x,y)
        j=0
        while(j<2): #for modifying current values

            y = b + ((h/2)*( fxy(a,b)+fxy(x,y) ))
            a = x
            b = y
            j+=1
            print("Modified :     {:10.4f}{:10.4f}".format(x,y))

        x+=h
        i+=1

    print("Modified :     {:10.4f}{:10.4f}".format(x,y))

    return y


x = float(input("Enter initial value of x0: "))
y = float(input("Enter initial value of y0: "))
xn = float(input("Enter value of xn: "))
n = float(input("Enter value of n: "))

answer = eulers(x,y,xn,n)

print("\nFinal Answer : {:6.4}".format(answer))

"""
OUTPUT

Enter initial value of x0: 0
Enter initial value of y0: 1
Enter value of xn: 0.2
Enter value of n: 2
value of h :  0.1
                        x         y
Simple Euler       0.0000    1.0000
Modified :         0.0000    1.1105
Modified :         0.0000    1.2338
Simple Euler       0.1000    1.2338
Modified :         0.1000    1.4174
Modified :         0.1000    1.6283
Modified :         0.2000    1.6283

Final Answer :  1.628
"""
