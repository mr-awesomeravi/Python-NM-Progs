q = int (input("Number of values of x and y :"))

sumx = 0
sumy = 0
sumx2 = 0
sumx3 = 0
sumx4 = 0
sumxy = 0
sumx2y = 0



a=[]

for i in range(q):
    a.append(int(input("Enter value {}".format(i))))
    sumx+= a[i]

b=[]

for i in range(q):
    b.append(float(input("Enter value {}".format(i))))
    sumy += b[i]

print(a)
print(b)


for i in range(q):
    print("{:5}{:5}{:5}{:5}{:5}{:5}{:5}".format(a[i],b[i],a[i]**2,a[i]**3,a[i]**4,a[i]*b[i],(a[i]**2)*b[i]))
    sumx2 += a[i]**2
    sumx3 += a[i]**3
    sumx4 += a[i]**4
    sumxy += a[i]*b[i]
    p = (a[i]**2)*b[i]
    sumx2y += p


print()
print()


print("{}       {}        {}          {}        {}       {}       {}".format(sumx,sumy,sumx2,sumx3,sumx4,sumxy,sumx2y))



c = [[q,sumx,sumx2,sumy], [sumx,sumx2,sumx3,sumxy], [sumx2,sumx3,sumx4,sumx2y]]
n = 3
x =[0,0,0]
eps = 10e-19
print(eps)


print(c)


#To make it diagonally dominant
for i in range(n):
    for k in range(i+1,n):
        if c[i][i] < c[k][i]:
            for j in range(n+1):
                c[i][j],c[k][j] = c[k][j],c[i][j]   #swap aij with akj

print(c)

#Now to find the Solution of equations
flag = 0
iter = 0
while flag<3:
    print(x)
    for i in range(n):
        y = x[i]
        x[i] = c[i][n]
        for j in range(n):
            if i!=j:
                x[i] = x[i] - c[i][j]*x[j]

        x[i] = x[i] / c[i][i]

        if abs(x[i]-y) <= eps:
            flag+=1

    iter+=1
    if iter >50:
        break

#Print the answer
print(x)
print("Number of iteration to reach solution are : {}".format(iter))
