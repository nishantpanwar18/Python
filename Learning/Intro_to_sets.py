n = int(input())
array = list(map(int, input().split()))

print(n)
print(array)
print(set(array))

print(sum(set(array))/len(array))