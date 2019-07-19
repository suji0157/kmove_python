#함수사용

def add(a,b):
    return a+b

print(add(5,4))
c=add(5,6)
print(c)

#매개변수

def add_many(chioce, *a):
    result = 0
    print(type(a))
    print(a)
    for i in a:
        result = result + i
    return result

total = add_many(1,2,3,4,5,6,7,8,9,10)
print(total)

print()

def add_and_mul(a,b):
    return a+b, a*b

add,mul=add_and_mul(3,6)
print(type(add))
print(type(mul))
print(add)
print(mul)

print()

def say_myself(name, old ,man):
    print('나의 이름은 %s 입니다. ' %name)
    print('나이는 %d 살 입니다. ' %old)

    if man:
        print('남자입니다. ')

    else:
        print('여자입니다. ')

say_myself('김수지',24,False)

print()

a=1
alist=[1,2,3]

def add_data():
    a=2
    alist.append(4)
    print('안 %d ' %a)

add_data()
print('바깥쪽 %d '%a)
print(type(a))
print(type(alist))