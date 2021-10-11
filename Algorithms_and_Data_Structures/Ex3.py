m = list(input().replace("[",'').replace("]",'').split(','))
m = list(map(lambda x: int(x), m ))
target = int(input())
for i in range(len(m)):
    if m[i] == target:
        print(i)
        exit(0)
    if target < m[i]:
        print(i)
        exit(0)
print(len(m))