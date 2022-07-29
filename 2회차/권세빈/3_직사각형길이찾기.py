import sys

sys.stdin = open("_직사각형길이찾기.txt")

# 직사각형은 같은 길이 2개씩 존재, 정사각형은 4개 존재

T = int(input())

for tc in range(1, T+1):
    length = list(map(int,input().split()))

    for i in range(3):
        # 만약 주어진 변의 길이 중 1개만 다른게 있다면
        if length.count(length[i]) == 1:
            # 해당 수 출력
            print(f'#{tc} {length[i]}')
        # 변의 길이가 모두 같다면
        elif length.count(length[i]) == 3:
            # 해당 수 출력
            print(f'#{tc} {length[i]}')
            break
