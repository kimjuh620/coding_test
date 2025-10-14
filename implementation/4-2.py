"""
시각
    정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

<입력 조건>
    첫째 줄에 정수 N이 입력된다.

<출력 조건>
    00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

<입력 예시>
    5

<출력 예시>
    11475
"""

n = int(input())

cnt = 0

for hh in range(n + 1):
    for mm in range(60):
        for ss in range(60):
            str_h = str(hh)
            str_m = str(mm)
            str_s = str(ss)
            tt = str_h + str_m + str_s
            if "3" in tt:
                cnt += 1

print(cnt)