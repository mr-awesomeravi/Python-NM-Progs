#Gauss Elemination    - Forward Elemination + Back Substitutino

def print_mat(a):
    for i in range(n):
        for j in range(n+1):
            print(    "{:7}".format(  a[i][j]  ),end=" "   )
        print("\n")
    print("\n")

def print_sol_mat(x):
    for i in range(n):
        print(   "{:4}".format(  x[i]  ) ,end=" "  )
        print("\n")
    print("\n")


# #Input Augmented Matrix
# n = int(input("Enter the number of equations : "))
# print("Enter the augmented matrix : ")
# a=[]
# for i in range(n):
#     a.append([])
#     for j in range(n+1):
#         a[i].append( int(input("Enter element in i = {} and j = {}   : ".format(i,j))) )
# print(a)

#Without input Augmented Matrix
n = 3
a = [[2, 1, -2, -1], [2, -3, 2, 9], [-1, 1, -1, -3.5]]
#a = [[2, -3, 1, -1], [1, 4, 5, 25], [3, -4, 1, 2]]

print_mat(a)

#forward elemination
for j in range(n):
    for i in range(n):
        if i>j:
            c = a[i][j] / a[j][j]
            for k in range(n+1):
                a[i][k] = a[i][k] - c * a[j][k]

print_mat(a)

#back substitution
x = [0,0,0]
for i in range(n-1,-1,-1):
    x[i] = a[i][n]
    for j in range(n):
        if i!=j:
            x[i]=x[i] - a[i][j]*x[j]
    x[i] = x[i] / a[i][i]

print_sol_mat(x)














#
