import random
import time

number = random.randint(0,199)
print("----------猜数字小游戏----------")
num=0
temp = input("小猪猪，猜一下我心里的数字吧(0 to 199，七次机会),：")
if temp == number:
    print("哇，不愧是我心里的小蛔虫,太厉害啦，一下子就猜中了！")
    print("End")
else:
    while temp!= number:     
        while not temp.isdigit():
            temp = input("这是错误的类型，必须是整数哦，再试一试吧：")
        guess = int(temp)
        if guess == number:
           print("哇，不愧是我心里的小蛔虫！")
           print("End")
           break
        elif guess > number:
            print("大了大了")
        else:
            print("小了小了")    
        num=num+1   
        temp = input("错误了%d次，没关系，再试一试吧：" % num)
        if num == 6:
            print("错误7次,说好的小蛔虫呢? \nGameover...")
            break

answer = input("是不是笨猪猪（请回答：yes or no），回答正确则笨猪猪的魔咒解除:")
while answer!='yes or no':
    print("不对不对重新回答！\n")
    answer = input("是不是笨猪猪（请回答：yes or no）:")
    
print("好聪明！笨猪猪魔咒解除！")    
time.sleep(1000)

        
