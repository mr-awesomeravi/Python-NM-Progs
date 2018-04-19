#Ravi Rathee #16csu292
#Adamns Bashforth Moulton Predictor Corrector method
def fxy(x,y):
    return y - x**2

def milne(x,y,xn,n):
    h = (xn - x) / n     #step size
    print("value of h : {:4.4}".format(h))

    print("{:>10}{:>10}".format('x','y'))
    print("{:10.4f}{:10.4f}".format(x,y))
    x0 = x
    y0 = y
    x1 = x0 + h
    y1 = y0 + h*fxy(x0,y0)
    print("{:10.4f}{:10.4f}".format(x1,y1))
    x2 = x1 + h
    y2 = y1 + h*fxy(x1,y1)
    print("{:10.4f}{:10.4f}".format(x2,y2))
    x3 = x2 + h
    y3 = y2 + h*fxy(x2,y2)
    print("{:10.4f}{:10.4f}".format(x3,y3))

    f0 = fxy(x0,y0)
    f1 = fxy(x1,y1)
    f2 = fxy(x2,y2)
    f3 = fxy(x3,y3)
    i=3
    while(i<n):
        x4 = x3 + h
        #Adams's Predictor
        y4 = y3 + (h/24)*( 55*f3 - 59*f2 + 37*f1 - 9*f0 )
        f4 = fxy(x4,y4)

        yold = y4
        #Adams's Corrector
        y4 = y3 + (h/24)*( 9*f4 + 19*f3 - 5*f2 + f1)
        f4 = fxy(x4,y4)


        while(yold - y4)>10**(-3):
            yold = y4
            #Adams's Corrector
            y4 = y3 + (h/24)*( 9*f4 + 19*f3 - 5*f2 + f1)
            f4 = fxy(x4,y4)

        print("{:10.4f}{:10.4f}".format(x4,y4))

        x0,x1,x2,x3 = x1,x2,x3,x4
        y0,y2,y3,y4 = y1,y2,y3,y4
        f1,f2,f3 = f2,f3,f4

        i+=1

    return y4




x = float(input("Enter initial value of x0: "))
y = float(input("Enter initial value of y0: "))
xn = float(input("Enter value of xn: "))
n = float(input("Enter value of n: "))

answer = milne(x,y,xn,n)

print("Final answer is : {:6.4}".format(answer))

"""
OUTPUT

Enter initial value of x0: 0
Enter initial value of y0: 0
Enter value of xn: 1
Enter value of n: 5
value of h :  0.2
         x         y
    0.0000    0.0000
    0.2000    0.0000
    0.4000   -0.0080
    0.6000   -0.0416
    0.8000   -0.1582
    1.0000   -0.2473
Final answer is : -0.2473
"""
