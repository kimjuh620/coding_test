n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

result = ''

for j in range(m):
    if arr2[j] in arr1:
        result += 'yes'
    else:
        result += 'no'

    if j != m-1:
        result += ' '

print(result)