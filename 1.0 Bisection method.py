#Ravi Rathee 16csu292
#Bisection Method

x1 = 1
x2 = 2
count = 0
def y(x) :
    #return (x**3 - x**2 - 2 )
    return x**4 - 7

while abs(x1 - x2)>0.01 :

    r = (x1+x2)/2
    print("{:10.3f}    {:10.3f}    {:10.3f}    {:10.3f}     {:10.3f}      {:10.3f}".format(float(x1),float(x2),float(y(x1)),float(y(x2)),float(r),float( y(r) ) ) )

    if (  y(r)*y(x1) )<0:
        x2 = r
    else:
        x1 = r
        count+=1

print(count)
print(r)
