
import random

#gen_count = 5

#1번째방법

#arr = [x for x in range(1,46)]
#for x in range(0, gen_count):
#    random.shuffle(arr)
#    arr_selected = arr[:6]
#    arr_selected.sort()
#    print(arr_selected)


#2번째방법

#for x in range(0, gen_count):
#    arr_selected = random.sample(range(1,46), 6)
#    arr_selected.sort()
#    print((' %2d '*6) % tuple(arr_selected))


#3번째방법

for i in range(5):
    lotto = [0,0,0,0,0,0]
    for x in range(6):
        num=0
        while(num in lotto):
            num=random.randint(1,46)
        lotto[x]=num
    print('lotto :',sorted(lotto))
    