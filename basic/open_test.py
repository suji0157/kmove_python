'''
#파일 생성

f=open("basic/test.txt",'w',encoding='utf8')

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#외부에 저장된 파일 읽기

f=open('basic/test.txt','r',encoding='utf8')
line=f.readlines()
print(line)
print(type(line))

for i in line:
    print(i.replace('\n',''))

f.close()


#파일에 새로운 내용 추가하기

f= open('basic/test.txt','a',encoding='utf8')

for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

# with문과 함께 사용하기

with open('basic/test.txt','a',encoding='utf8') as f:
    f.write('Life is too short, you need python')