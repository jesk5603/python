d = {}
num = int(input('input number:'))
for i in range(num):
    key = input('input key')
    value = input('input value')
    d[key] = value
print(d)

c = input('input del key')
a = d.pop(c, '哈哈沒有這東西')
print(f'移除資料{a}')

for key, value in d.items():
    print(f'{key}={value}')

s = input('input search key:')
if s in d:
    print(True)
else:
    print(False)