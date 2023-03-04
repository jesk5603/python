#  5/9 乘(華氏溫度- 32)
try:
    f = float(input('請輸入華氏溫度:'))
except:
    print('輸入錯誤')
else:
    c = 5 / 9 * (f - 32)
    print(f'華氏溫度{f}F等於攝氏溫度{c}C')
print('程式結束')
