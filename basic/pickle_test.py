import pickle

data={ 1: 'python', 2: 'you need'}

f=open('test.txt','wb')
pickle.dump(data,f)
f.close()



print(data)
print(data1)
print(type(data1))