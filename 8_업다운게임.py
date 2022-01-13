import random

ans = random.randint(1,100) # 1~100사이의 랜덤한 숫자를 뽑아줌
print(ans)

print("------ 업 다운 게임을 시작합니다 ------")
cnt = 0 # 카운트 변수
while True:
    num = int(input("숫자 입력 >> "))
    cnt += 1 # 숫자 입력 할 때마다 카운트 추가
    if num == ans: # 숫자를 맞췄을 경우
        print("{}회 만에 정답을 맞추셨습니다!".format(cnt))
        break
    elif num > ans: # 정답보다 큰 숫자를 말했을 경우
        print("DOWN!")
    elif num < ans: # 정답보다 작은 숫자를 말했을 경우
        print("UP!")
