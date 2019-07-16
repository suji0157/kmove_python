#리스트 + while문 + if문

listdata=[]
while True:
    print('''
    ======================== 리스트 데이터 관리 ==========================
    1.리스트에 추가 2.리스트데이터 수정 3.리스트데이터 삭제 4.종료
    ''')
    menu = int(input('메뉴를 선택하세요'))
    if menu == 4:
        break
    elif menu == 1:
        data=input('추가할 데이터를 입력하세요')
        listdata.append(data)
        print(listdata)
    elif menu == 2:
        pass
    elif menu == 3:
        pass

# 수정하는거 삭제하는거 해보기
