# print('I %d savge' % 94)
# print('I %3d savge' % 94)
# print('I %03d savge' % 94)

# print('I {0:d} savge' .format (94))
# print('I {0:3d} savge'.format (94))
# print('I {0:03d} savge'.format (94))

# print('I %f savge' % 94)
# print('I %.2f savge' % 94)

# print('I {0:f} savge' .format (94))
# print('I {0:.2f} savge' .format(94) )

# print('I %s savge' % 94)
# print('I {0:s} savge' .format (94))

# A = int(input('輸入你要的值'))
# print('%d' % A)

# A = int(input('輸入你要的值'))
# print('%5d' % A)

# A = int(input('輸入你要的值'))
# print('%05d' % A)

# A = float(input('輸入你要的浮點數值'))
# print('%f' % A)
# print('%.2f' % A)

# a = eval(input())
# print(f'這個算式的答案是{a}')

# d = 5
# s = 2
# a = eval('d+s')
# print(a)

import datetime as d

# a = d.date.today()
# print(a)
# print(a.year)
# print(a.month)
# print(a.day)
# print(a.strftime)'''把datetime 變成字串'''

day = input('你的生日(年/月/日)')
print(day)
birth = d.datetime.strptime(day, '%Y/%m/%d')
print(birth.date())