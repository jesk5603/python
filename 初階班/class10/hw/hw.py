d = {}
while True:

    for key, value in d.items():
        print(f'{key}={value}')
    print('1.新增科目與成績')
    print('2.刪除某科目的成績')
    print('3.關閉系統')
    y = int(input('請輸入功能選項:'))
    if y == 1:
        key = input('input 科目')
        value = input('input 成績')
        d[key] = value
    if y == 2:
        c = input('input 要刪除的科目')
        a = d.pop(c, '哈哈沒有這科目')
        print(f'移除資料{a}')
    if y == 3:
        e = sum(d.values())
        z = len(d)
        q = e / z
        print(f'總平均為{q}')
        break
    else:
        print('輸入錯誤，請重新輸入')
