import random as r

ans = r.randint(1, 101)
ma = 100
mi = 1
while True:
    user = int(input('請輸入數字{}~{}:'.format(mi, ma)))
    if user == ans:
        print('恭喜猜中了')
        break
    elif user > ans:
        if user < ma:
            ma = user
        print('在小一點')
    elif user < ans:
        if user > mi:
            mi = user
        print('在大一點')
