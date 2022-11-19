# j = ['蘋果汁', '柳橙汁', '葡萄汁', '政翮果汁', '系統關閉']
# while True:
#     for i in range(len(j)):
#         print(f'{i+1}. {j[i]}')
#     ans = int(input('請輸入編號'))
#     if ans == len(j):
#         print('系統關閉')
#         break
#     elif ans > len(j) or ans <= 0:
#         print('輸入錯誤查無此果汁，請重新輸入')
#     else:
#         print(f'您點的商品是{j[ans-1]})
a = []
while True:
    x = input('輸入e就離開程式，請輸入想新增的資料:')
    if x == 'e':
        print('881')
        break
    else:
        a.append(x)
        print(a)
