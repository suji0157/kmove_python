
import random

count=0 #마지막에 몇개 맞았는지 셀 때 필요
oper=['+','-','*','//']
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
print('%d개 맞음'%count)
