#Ravi Rathee 16csu292
#Runge - Kutta Method
def fxy(x,y):
    #return (-1)*(x)*(y**2)
    #return x**2 + y
    return x*y + y**2
    
def rungekutta(x,y,xn,n):
    h = (xn - x) / n     #step size
    print("value of h : {:4.4}".format(h))

    print("{:>10}{:>10}".format('x','y'))

    i=0
    while(i<n):
        print("{:10.4f}{:10.4f}".format(x,y))

        k1 = h * fxy( x , y )
        k2 = h * fxy( ( x+h / 2.0 ),( y+k1*h/2.0))
        k3 = h * fxy( ( x+h / 2.0 ),( y+k2*h/2.0))
        k4 = h * fxy( ( x+h ),( y+k3 * h))
        k  = ((k1 + 2*k2 + 2*k3 + k4) / 6)

        y = y + k
        x+=h
        i+=1

    print("{:10.4f}{:10.4f}".format(x,y))

    return y

x = float(input("Enter initial value of x0: "))
y = float(input("Enter initial value of y0: "))
xn = float(input("Enter value of xn: "))
n = float(input("Enter value of n: "))

answer = rungekutta(x,y,xn,n)

print("{:6.4}".format(answer))


"""
OUTPUT

Enter initial value of x0: 0
Enter initial value of y0: 1
Enter value of xn: 1.4
Enter value of n: 7
value of h :  0.2
         x         y
    0.0000    1.0000
    0.2000    0.9801
    0.4000    0.9231
    0.6000    0.8394
    0.8000    0.7431
    1.0000    0.6463
    1.2000    0.5569
    1.4000    0.4785
0.4785
"""
