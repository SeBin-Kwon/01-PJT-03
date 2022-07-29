import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for tc in range(1, T+1):
    n = list(input()[::-1]) # 역순으로 바꾸기

    for i in range(len(n)): # 해당 문자 하나하나 바꾸기
        if n[i] == 'b':
            n[i] = 'd'
        elif n[i] == 'd':
            n[i] = 'b'
        elif n[i] == 'p':
            n[i] = 'q'
        elif n[i] == 'q':
            n[i] = 'p'

    print(f'#{tc} {"".join(n)}') # 리스트를 문자열로 바꾸기