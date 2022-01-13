phoneList = []
numOfDate = 0
while True:
    print("============================")
    print("현재 데이터 개수 : {}개".format(numOfDate))
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체출력")
    print("5. 종료")
    print("============================")
    menu = int(input("선택 >> "))
    if menu == 1:
        name = input("이름 입력 : ")
        number = input("번호 입력 : ")
        phoneList.append({"name":name, "number":number})
        numOfDate += 1
    elif menu == 2:
        pass
    elif menu == 3:
        pass
    elif menu == 4:
        for data in phoneList:
            print("-------------------------")
            print("이름 :", data["name"])
            print("번호 :", data["number"])
            print("-------------------------")
    elif menu == 5:
        print("종료 되었습니다.")
        break
    else:
        print("올바른 선택이 아닙니다.")