import random,time
#미완성!!!!!!!!!!


count=0 #마지막에 몇개 맞았는지 셀 때 필요
oper=['+','-','*','//']

input('엔터를 누르고 20초를 셉니다.')
start = time.time()
input('20초 후에 다시 엔터를 누릅니다.')

for x in range(0,5):
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper)

    quiz=str(a)+op+str(b)
    quiz='%d %s %d'%(a,op,b)

    print(quiz,'=')
    print(eval(quiz))
    c=int(input('정답='))

    if int(eval(quiz))==c:
        print('정답!')
        count+=1
    else:
        print('오답!')

end = time.time()
et = end - start
print('%.0f초동안 %d개 맞음'%(et,count))