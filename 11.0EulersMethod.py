#Ravi Rathee 16csu292
#Eulers Method
def fxy(x,y):
    #return (-1)*(x)*(y**2)
    #return x+y+x*y
    return x+y**2
def eulers(x,y,xn,n):
    h = (xn - x) / n     #step size
    print("value of h : {:4.4}".format(h))

    print("{:>10}{:>10}".format('x','y'))

    i=0
    while(i<n):
        print("{:10.4f}{:10.4f}".format(x,y))
        y = y + h*fxy(x,y)
        x+=h
        i+=1

    print("{:10.4f}{:10.4f}".format(x,y))

    return y


x = float(input("Enter initial value of x0: "))
y = float(input("Enter initial value of y0: "))
xn = float(input("Enter value of xn: "))
n = float(input("Enter value of n: "))

answer = eulers(x,y,xn,n)

print("{:6.4}".format(answer))

"""
OUTPUT

Enter initial value of x0: 2
Enter initial value of y0: 1
Enter value of xn: 2.2
Enter value of n: 4
value of h : 0.05
         x         y
    2.0000    1.0000
    2.0500    0.9000
    2.1000    0.8170
    2.1500    0.7469
    2.2000    0.6869
0.6869
"""
