#Ravi Rathee #16csu292
#Milne's Predictor Corrector method
def fxy(x,y):
    return x - y**2

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

    f1 = fxy(x1,y1)
    f2 = fxy(x2,y2)
    f3 = fxy(x3,y3)
    i=3
    while(i<n):
        x4 = x3 + h
        #Milne's Predictor
        y4 = y0 + ((4*h)/3)*( 2*f1 - f2 + 2*f3 )
        f4 = fxy(x4,y4)

        yold = y4
        #Milne's Corrector
        y4 = y2 + (h/3)*(f2 + 4*f3 + f4)
        f4 = fxy(x4,y4)


        while(yold - y4)>10**(-3):
            yold = y4
            #Milne's Corrector
            y4 = y2 + (h/3)*(f2 + 4*f3 + f4)
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
    0.4000    0.0400
    0.6000    0.1197
    0.8000    0.2712
    1.0000    0.3323
Final answer is : 0.3323
"""
