import random
secret = random.randint (1,20)
print('人活着多半不知感激，现在我们来玩一个游戏(输入数字即可,且必须是正数)')
temp = input("珍惜一切，不管是一杯水还是一次公园的散步。但大多数人都很幸运，他们不知道什么时候会停。讽刺的是就因为这个，他们才不能好好地活着，他们喝水却从不感受它的甘甜:")
geek = int(temp)
while geek != secret:
    temp = input("你可以重新来过:")
    geek = int(temp)
    if geek < secret:
        print("别以为活着是理所当然，别等到来不及才知道珍惜")
        print("你的出路只有赢，忽视周围的一切")
    if geek < 0:
        print("你得照我的规矩来！")    
    else:
        if geek > secret:
            print("是生是死，你自己选择")
        else:
            print("人们活着多半不会感激，你以后不会了")
print("Game Over!")