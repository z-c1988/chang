#1. if条件判断
money = 88
if money>100:
    print("rich")
else:
    print("poor")

#2. 逻辑判断
(a) == True
(b) == False
(c) 
请输入内容1
True
请输入内容
False
(d) 
False
True
False
True
False
True
False

#3. BMI 计算器
height = float(input("height:"))
weight = float(input("weight:"))
BMI = weight/(height*height)      
if BMI < 18.5:
    print("体重偏轻")
elif 18.5 <= BMI < 24:
    print("体重正常")
elif BMI >= 24:
    print("体重偏重")
