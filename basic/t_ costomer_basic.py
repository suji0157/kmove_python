import re # 정규 표현식
import pickle
custlist=[] # 고객 전체정보를 리스트로 관리
page=-1 # 현재 데이터가 있는지 없는지 확인 
data={ 'name':'김수지','sex':'F',"email":'suji97@naver.com',"birthyear":'1997'}

while True: # 무한반복
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    O - 고객 정보 불러오기
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    S - 고객 정보 저장하기
    Q - 프로그램 종료
    ''').upper() # 소문자를 대문자로 변환

    if choice=="I":
        customer={'name':'','sex':'',"email":'',"birthyear":''} # 전체정보 리스트에 저장   
        print("고객 정보 입력")
        customer['name']=input('이름 :')
        while True:
            customer['sex']=input('성별 :').upper()
            if customer['sex'] in ('M','F'):
                break
            else:
                print('다시 입력하세요')
    
        while True: # 중복되지 않게 입력
            regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$') # 정규표현식
            # ^는 시작 지정, $는 끝 지정, {}는 자리수 지정
            while True:
                customer['email']= input('이메일 : ')
                globang = regex.search(customer['email'])
                if globang:
                    break
                else:
                    print('@를 포함한 정확한 이메일을 써주세요')

            check = 0
            for i in custlist:
                if i['email']==customer['email']:
                    check = 1

            if check==0:
                break
            print('중복되는 이메일이 있습니다')    

        while True:
            customer['birthyear'] = input('출생년도 4자리를 입력해주세요 :')
            
            if len(customer['birthyear'])==4 and customer['birthyear'].isdigit():
                break
        
        print(customer)
        custlist.append(customer)
        print(custlist)

        page = len(custlist)-1
        print(page)
    
    elif choice=="C":
        print("현재 고객 정보 조회")  
        
        if page >= 0:
            print('현재 페이지는 {} 쪽 입니다.'.format(page + 1))
            print(custlist[page])

        else:
            print('입력된 정보가 없습니다.')

    elif choice == 'P':
        print("이전 고객 정보 조회") 
        
        if page <= 0:
            print('첫 번째 페이지 이므로 이전 페이지 이동이 불가합니다.')
            print(page)

        else:
            page -= 1
            print('현재 페이지는 {} 쪽 입니다.'.format(page + 1))
            print(custlist[page])

    elif choice == 'N':
        print("다음 고객 정보 조회")
        
        if page >= len(custlist-1):
            print('마지막 페이지 이므로 다음 페이지 이동이 불가합니다.')
            print(page)

        else:
            page += 1
            print('현재 페이지는 {} 쪽 입니다.'.format(page + 1))
            print(custlist[page])

    elif choice=="U": 
        print("고객 정보 수정")

        while True:
            choice1 = input('수정하시려는 고객의 이메일을 입력하세요.')
            idx = -1
            for i in range(0,len(custlist)):
                if custlist[i]['email']==choice1:
                    idx=i
                    break
            if idx==-1:
                print('등록되지 않은 이메일입니다.')
                break

            choice2=input('''
            다음 중 수정하실 정보를 골라주세요
                name, sex, birthyear
            (수정할 정보가 없으면 'exit' 입력)
            ''')

            if choice2 in ('name','sex','birthyear'):
                custlist[idx][choice2]= input('수정할 {} 를 입력하세요.'.format(choice2))
                break
            elif choice2 == 'exit' :
                break
            else:
                print('존재하지 않는 정보입니다.')
                break


# 유일한 값(중복되지 않는 값)을 찾아서 수정하거나 삭제해야함
# key = email (유일한 값)

    elif choice=='D':
        print("고객 정보 삭제") 
        choice1 = input('삭제하려는 고객의 이메일을 입력하세요.')
        delok = 0
        for i in range(0,len(custlist)):
            if custlist[i]['email']== choice:
                print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
                del custlist[i]
                print(custlist)
                delok = 1
                break

        if delok == 0:
            print('등록되지 않은 이메일입니다.')
            print(custlist)
            
    
    elif choice=="Q":
        print("프로그램 종료")
        break
    
    else:
        print("잘못입력하셨습니다.")
