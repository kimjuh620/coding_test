"""
큰 수의 법칙

    N 개의 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
    배열의 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

<입력 조건>
    첫째 줄에 N, M, K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
    둘째 줄에 N 개의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
    입력으로 주어지는 K는 항상 M보다 작거나 같다.

<출력 조건>
    큰 수의 법칙에 따라 더해진 답을 출력한다.

<입력 예시>
    5 8 3
    2 4 5 4 6

<출력 예시>
    46
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

num1 = max(data)

while True:
    if max(data) == num1:
        data.pop()
    else:
        num2 = max(data)
        break

result = 0

for i in range(m):
    if (i + 1) % k == 0:
        result += num2
    else:
        result += num1

print(result)
