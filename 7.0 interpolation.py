import math
n = int(input("Enter the no. of values :"))

a = []
a.append([])
for i in range(n):
    x = float(input("Enter value of x {}".format(i)))
    a[0].append(x)

print(a)

a.append([])
for i in range(n):
    x = float(input("Enter value of y {}".format(i)))
    a[1].append(x)

print(a)

k = n-2
for i in range(2, n+1):
    a.append([])
    for j in range(k+1):
        var = a[i-1][j] - a[i-1][j+1]
        var = round(var,4)
        a[i].append(var)
    k -= 1

print(a)

z = float(input("Enter the value of x to find correspoding value f(x)"))
print("z={}".format(z))

diff = a[0][1] - a[0][0]
print("diff={}".format(diff))

P = (z - a[0][0]) / diff
print("P = {}".format(P))

ans = a[1][0]
print("ans = {}".format(ans))

for i in range(2, n+1):
    Pnew = 1
    LeftNewTerm = 1
    NewTerm = 1
    for j in range(0, i-1):
        Pnew = Pnew * (P - j)
        Pnew = round(Pnew, 6)
    print("Pnew for {} = {}".format(i, Pnew))
    LeftNewTerm = Pnew / math.factorial(i-1)
    LeftNewTerm = round(LeftNewTerm, 6)
    print("LeftNewTerm for {} = {}".format(i, LeftNewTerm))
    NewTerm = LeftNewTerm * a[i][0]
    NewTerm = round(NewTerm, 6)
    print("NewTerm for {} = {}".format(i, NewTerm))

    ans += NewTerm
    print("Ans = {}".format(ans))

print("Final Answer of   f({}) is : {}".format(z, ans))














