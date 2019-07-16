money = True
if money:
    print('택시타고 가든지')
#내어쓰기는 쉬프드+탭
else:
    pass #내용 비워둘 때 사용함
    #print('걸어가든지')

#if조건문 비교연산

x=3
y=2

print(x>y)

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라.

money1 = 2000
if money1 >= 3000:
    print('택시ㄱ')
else:
    print('걸어서ㄱ')

jumsu = int(input('성적 입력: \n'))
print('입력한 성적은 %s 입니다.'%jumsu)
#print('입력한 성적은',jumsu,'입니다')

if jumsu >90:
    print('A')
elif jumsu >80:
    print('B')
elif jumsu>60:
    print('c')
else:
    print('F')