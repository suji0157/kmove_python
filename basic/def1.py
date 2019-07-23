import re,pickle,os
custlist=[]
page=-1

while True:
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
    exe(choice)

def exe(choice):
        if choice=='I': #고객 정보 입력
            insertData()
        
        elif choice=='C': #현재 고객 정보 조회
            curSearch()
        
        elif choice=='P': #이전 고객 정보 조회
            preSearch()

        elif choice=='N': #다음 고객 정보 조회
            nextSearch()

        elif choice=='U': #고객 정보 수정
            updateData()
        
        elif choice=='D': #고객 정보 삭제
            deleteData()
        
        elif choice=='Q': #프로그램 종료
            saveData()
            quit()

def insertData():
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

def curSearch():
    global page
    print("현재 고객 정보 조회")  
        
    if page >= 0:
        print('현재 페이지는 {} 쪽 입니다.'.format(page + 1))
        print(custlist[page])

    else:
        print('입력된 정보가 없습니다.')

def preSearch():
    global page
    print("이전 고객 정보 조회") 
        
    if page <= 0:
        print('첫 번째 페이지 이므로 이전 페이지 이동이 불가합니다.')
        print(page)

    else:
        page -= 1
        print('현재 페이지는 {} 쪽 입니다.'.format(page + 1))
        print(custlist[page])

def nextSearch():
    global page
    print("다음 고객 정보 조회")
        
    if page >= len(custlist-1):
        print('마지막 페이지 이므로 다음 페이지 이동이 불가합니다.')
        print(page)

    else:
        page += 1
        print('현재 페이지는 {} 쪽 입니다.'.format(page + 1))
        print(custlist[page])

def updateData():
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

def deleteData():
    print("고객 정보 삭제") 
    choice3 = input('삭제하려는 고객의 이메일을 입력하세요.')
    delok = 0
    for i in range(0,len(custlist)):
        if custlist[i]['email']== choice3:
            print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            print(custlist)
            delok = 1
            break

    if delok == 0:
        print('등록되지 않은 이메일입니다.')
        print(custlist)

def quit():
    print("프로그램 종료")
    

def saveData():
    with open('basic/data.pkl','wb',encoding='utf8') as f: # pkl도 되고 txt도 됨
        pickle.dump(custlist,f)

def loadData():
    #파일 크기가 0보다 클 경우에 읽어옴
    #if os.path.getsize('basic/data.pkl')>0:
    #파일이 존재할 경우에 읽어옴
    
    global page,custlist
    if os.path.exists('basic/data.pkl',encoding='utf8'):
        with open('basic/data.pkl','rb') as f:
            custlist=pickle.load(f)
            page=len(custlist)-1