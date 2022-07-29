import sys

sys.stdin = open("_최빈수구하기.txt")

# 10 8 7 2 2 4 8 9 8 9 5 5 9 10 10 10

T = int(input())
cnt = 0 # 최빈수 구하기

for _ in range(T):
    tc = int(input())
    student = list(map(int,input().split()))

    # 어떤 숫자가 여러번 나오는지 비교하기 위한 반복문
    for i in student:
        if cnt < student.count(i):  # 카운트한 수가 더 크다면
            cnt = student.count(i)  # cnt 변수에 할당
            m = i                   # 해당 수를 결과값 변수에 할당
        elif cnt == student.count(i): # 만약 카운트한 수가 같다면
            m = max(m, i) # 둘중에 더 큰 수 할당
    print(f'#{tc} {m}')
    cnt = 0               # 카운트 초기화

