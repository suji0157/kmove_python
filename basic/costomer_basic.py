import re # 정규표현식
custlist=[] # 고객 전체정보를 리스트로 관리
page=-1 # 현재 데이터가 있는지 없는지 확인 

while True: # 무한반복
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

    if choice=="I":
        customer={'name':'','sex':'',"email":'',"birthyear":''} # 전체정보 리스트에 저장   
        print("고객 정보 입력")
        name = input('이름 : ')
        sex = input('성별 [ M,m or F,f ] :')
        sex = (sex.upper())
        print(sex)
        email = input('이메일 : ')
        p = re.compile('^\w+[@]+\w')
        m = p.search(email)
        print(m)
            

    elif choice=="C":
        print("현재 고객 정보 조회")  
    elif choice == 'P':
        print("이전 고객 정보 조회") 
    elif choice == 'N':
        print("다음 고객 정보 조회")
    elif choice=='D':
        print("고객 정보 삭제")
    elif choice=="U": 
        print("고객 정보 수정")
    elif choice=="Q":
        print("프로그램 종료")
        break
    else:
        print("잘못입력하셨습니다.")
