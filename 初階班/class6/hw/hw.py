x = int(input('請輸入正整數'))
i = 1
a = 3
b = 7
while i <= x:
    if i % 3 == 0 or i % 7 == 0:
        print(i)
    i += 1
