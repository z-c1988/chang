#1. 计算100以内所有3的倍数的和（即：计算3、6、9 ... 96、99 的和）
sum = 0
for i in range(1,101):
    if i % 3 ==0:
        sum += i
print(sum)

#2. 分别输入高和宽两个整数，输出对应高度和宽度的矩形
h = int(input('请输入高度:'))
w = int(input('请输入宽度:'))
for i in range(h):
        for j in range(w):
            print('*', end=' ')
        print()

#3.输出九九乘法口诀表
for i in range(1, 10):
    for j in range(1,i+1):
        print('%d x %d = %d' % ( i,j,i*j), end='  ')
    print()

for i in range(1, 10):
    for j in range(1,10):
        print('%d x %d = %d' % (i,j,i*j))
        
#4.跳出循环
nums = [23, 45, 8, 13, 50, 43, 21]
sum = 0
for n in nums:
    sum += n
    if sum > 100:
        break
print(sum)

        
