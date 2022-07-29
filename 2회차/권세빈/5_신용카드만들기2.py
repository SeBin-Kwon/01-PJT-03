import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
start = ['3','4','5','6','9']

for tc in range(1, T+1):
    num = list(input())

    # 만약 시작 번호가 3,4,5,6,9 에 포함된다면
    if num[0] in start: 
        for i in num: # '-'빼는 작업
            if i == '-':
                # '-'가 있는 인덱스 찾아서 빼기
                num.pop(num.index('-'))

        if len(num) == 16: # 카드 번호 개수가 16개라면
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')
    else:
        print(f'#{tc} 0')  
