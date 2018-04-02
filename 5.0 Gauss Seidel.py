#Gauss Seidel

def print_mat(a):
    for i in range(n):
        for j in range(n+1):
            print(    "{:10.1f}".format(  float(a[i][j]) ),end=" "   )
        print("\n")
    print("\n")

def print_sol_mat(x):
    for i in range(n):
        print(   "{:10.3}".format(  float(x[i])  ) ,end=" "  )
        print("\n")
    print("\n")

# #Input Augmented Matrix a=[] and intial guess x=[]
# n = int(input("Enter the number of equations : "))
# print("Enter the augmented matrix : ")
# a=[]
# for i in range(n):
#     a.append([])
#     for j in range(n+1):
#         a[i].append( int(input("Enter element in i = {} and j = {}   : ".format(i,j))) )
#
# print_mat(a)
#
# #Take initial guess of solution
# x =[]
# print("Enter your guess of solution : ")
# for i in range(n):
#     x.append( int(input("Enter i = {} for x :".format(i))))
# print_sol_mat(x)

n = 3
#a = [[2, 1, 6, 9], [8, 3, 2, 13], [1, 5, 1, 7]]    #ans = [1, 1, 1]
a = [[1, 2, 1, 2], [2, 1, 1, 2], [1, 1, 3, -1]]
x =[0,0,0]
eps = 10e-19


#To make it diagonally dominant
for i in range(n):
    for k in range(i+1,n):
        if a[i][i] < a[k][i]:
            for j in range(n+1):
                a[i][j],a[k][j] = a[k][j],a[i][j]   #swap aij with akj

print_mat(a)

#Now to find the Solution of equations
flag = 0
iter = 0
while flag<n:
    print_sol_mat(x)
    for i in range(n):
        y = x[i]
        x[i] = a[i][n]
        for j in range(n):
            if i!=j:
                x[i] = x[i] - a[i][j]*x[j]

        x[i] = x[i] / a[i][i]

        if abs(x[i]-y) <= eps:
            flag+=1

    iter+=1


print("Number of iteration to reach solution are : {}".format(iter))
