# 파일 열기 모드
# "r" ahem : 읽기 모드
#          : 파일이 존재하지 않으면 에러!
f = open("./test.txt", "r", encoding='UTF8')
result = f.read()
f.close()
print(result)