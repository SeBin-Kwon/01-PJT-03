import sys

sys.stdin = open("_암호문1.txt")

# 원본 암호문의 앞에서부터 x+1 부분에 
# y개 숫자들 삽입
# 그후 처음 10개 항 출력

for tc in range(10):
    # 원본 암호문의 길이
    n = int(input())
    # 원본 암호문
    o = list(map(int,input().split()))
    # 명령어의 개수
    m = int(input())
    # 명령어
    I = list(map(int,input().split()))