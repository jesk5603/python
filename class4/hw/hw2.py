a = int(input('請輸入三角形的第1個邊'))
b = int(input('請輸入三角形的第2個邊'))
c = int(input('請輸入三角形的第3個邊'))
if a + b > c and a + c > b and b + c > a:
    print('這是三角形')
    p = 1 / 2 * (a + b + c)
    area = (p * (p - a) * (p - b) * (p - c))**0.5
    print(f"周長{a+b+c} 面積{area}")
else:
    print('無法形成')
