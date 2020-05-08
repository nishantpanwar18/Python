import math
n, m = input().split(" ")
n = int(n)
m = int(m)
print(n//3)

for i in range(m//n):
    (math.floor(m/2)-1)*'-'.ljust()
