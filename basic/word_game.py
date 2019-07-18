import random,time

word = ['critic','appiontment','fantastic','cancel','apology','mixed','recipient','convenience','public']
#print(word)

quiz = random.sample(word,5)
print(quiz)

input('게임 준비가 되면 enter를 누르세요')

start = time.time()
while 