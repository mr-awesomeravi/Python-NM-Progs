x1 = 1
x2 = 2
count = 0
def y(x) :
    return (x**3 - x**2 - 2 )

while abs(x1 - x2)>0.01 :
    r = (x1+x2)/2
    if (  y(r)*y(x1) )<0:
        x2 = r
    else:
        x1 = r
        count+=1

print(count)
print(r)