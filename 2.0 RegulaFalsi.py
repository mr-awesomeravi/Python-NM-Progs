x1 = 1
x2 = 2
count = 0
def y(x) :
    return (x**3 - x**2 - 2 )

while abs(x1 - x2)>0.01 :
    f_a = y(x1)
    f_b = y(x2)

    r = (x1 * f_b - x2 * f_a) / (f_b - f_a)


    print("{}          {}           {} ".format(x1,x2,r))
    if (  y(r)*y(x1) )<0:
        x2 = r
    else:
        x1 = r
        count+=1

print(count)
print(r)