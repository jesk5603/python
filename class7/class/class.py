# for i in range(2, 6):
#     print(i)
# else:
#     print("迴圈正常結束")

# i = 2
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("迴圈正常結束")

# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i < 6:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# while True:
#     print('1、蘋果汁   2. 柳橙汁   3. 葡萄汁   4. 系統關閉')
#     i = input('請輸入編號')

#     if i == "1":
#         print('您點的商品是蘋果汁')
#     elif i == "2":
#         print('您點的商品是柳橙汁')
#     elif i == "3":
#         print('您點的商品是葡萄汁')
#     elif i == "4":
#         print('~~系統關閉~~')
#         break
#     else:
#         print('輸入錯誤查無此果汁，請重新輸入')

# r.randrange(3)    r.randrange(0, 10, 2)     隨機取數0-2

# print(r.randint(1, 3))         隨機取數1-3
# print(r.randint(1, 10))
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
