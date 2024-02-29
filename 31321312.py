import random
##1

stroka = ''
for i in range(3):
    a = input()
    stroka += a + " "
print(stroka)

##2
a=input()
stroka = ''
while (a!='stop'):
    stroka += a + " "
    a = input('Enter stop to break')
print(stroka)

##3

slovo = input()

if 'ф' in slovo:
    print('Ого! Это редкое слово!')
else:
    print('Эх, это не очень редкое слово...')

##4
i=0
while i < 3:
    a = (random.randint(1,10))
    b = random.randint(1,10)
    stroka = str(a) + '+' + str(b) + '='
    rez=input(stroka)
    if int(rez) == int(a)+int(b):
        print("Правильно")
    else:
        print('Неправильно')
        i+=1
print("Игра окончена")