h = float(input('請輸入身高:'))
w = float(input('請輸入體重:'))
bmi = w / h**2
print('你的BMI為', bmi)
if bmi <= 14.7:
    print('體重過輕')
elif bmi >= 20.8:
    print('體重過重')
else:
    print('體重正常')