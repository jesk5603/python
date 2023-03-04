x = []
while True:
    print(f'目前已點的餐:{x}')
    print('1. 新增餐點')
    print('2. 移除餐點')
    print('3. 提交菜單')
    y = int(input('請輸入功能選項:'))
    if y == 1:
        print('蘋果汁', '柳橙汁', '葡萄汁')
        q = input('請輸入想新增的餐點:')
        x.append(q)
    elif y == 2:
        ans = input('請輸入想移除的餐點:')
        x.remove(ans)
    elif y == 3:
        print('已提交菜單')
        b = []
        for i in x:
            if i in b:
                continue
            else:
                b.append(x)
        for i in b:
            print(f'{i}有{x.count(i)}個')
        break
    else:
        print("查無此選項!!")
