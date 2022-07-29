import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
odd = 0 # 홀수 자리
even = 0 # 짝수 자리

for tc in range(1, T+1):
    num = list(map(int,input().split()))

    # 카드번호 자리수 만들기
    for i in range(1,len(num)+1): 
        if i % 2 != 0:          # 자리 수 가 홀수라면
            odd += num[i-1] * 2 # 인덱스의 값과 곱하기
        else:
            even += num[i-1] # 짝수 자리라면 그냥 더하기
            
    r = (odd + even) % 10 # 홀짝 더했을 때의 일의 자리
    result = (10 - r)%10  # 10을 뺐을 때 나머지, 0이면 0이 나오게하기
    print(f'#{tc} {result}')
    odd = 0  # 변수 초기화
    even = 0  