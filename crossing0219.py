1.from math import pi 
r = 20
S = pi * r * r
print(S)

2.import random
s = []
while len(s) <10:
    i = random.random()
    s.append(i)
s.sort(reverse=True)
print(s)
print(s[0])

3.import random
j = 0
s = 0
while True:
    j += 1
    i = 0
    num = random.randint(1,100)
    print('This is the %d th round(s)'%j)
    bingo = False
    while bingo == False:
        i += 1
        ans = int(input('input:'))
        if ans > num:
            print('too big!') 
        elif ans < num:
            print('too small!')
        else:
            print('bingo!')
            bingo = True
    print('You\'ve tried %d time(s)'%i)
    s += i
    ave = s / j
    trying = input('Do you wanna try again? (Yes or No)')
    if trying != 'Yes':
        print("Good Game! You've tried %d round(s), your average score are %.2f times to get right."%(j,ave))
        break
