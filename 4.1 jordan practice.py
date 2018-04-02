#gauss Jordan

def print_mat(a):
    for i in range(n):
        for j in range(n+1):
            print("{:10.1f}".format( float(a[i][j] ) ),end = " " )
        print()
        print()
    print()

def print_mat_sol(x):
    for i in range(n):
        print("{:10.1f}".format( float(x[i] ) ),end = " " )
        print()
        print()


n=3
a = [[1, 2, 1, 2], [2, 1, 1, 2], [1, 1, 3, -1]]
print_mat(a)

#forward elemination
for j in range(n):
    for i in range(n):
        if i!=j:
            c=a[i][j]/a[j][j]
            for k in range(n+1):
                a[i][k]=a[i][k]-c*a[j][k]

#back substitution
x=[0,0,0]
for i in range(n-1,-1,-1):
    x[i]=x[i][n]
    for j in range(n):
        if i!=j:
            x[i]=x[i]-a[i][j]*x[j]

    x[i]=x[i]/a[i][i]
