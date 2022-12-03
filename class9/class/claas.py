'''
remove:刪除[]裡面的東西
l=[1,2,1,3,1,4,1,5,1,6]
判斷1在不再裡面:
if 1 in l:
    print('True')
else:
    print("False")
刪除再l裡面的1
while i in l:
    l.remove
print(l)
判斷1在不再裡面:
print (not(1 in l))
'''
# l = ['a', 'b', 'c']
# l
# l[0] = 'A'
# l

# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a)

# l = [1, 2, 3]
# l.append(4)
# print(l)

# l = [9, 1, -4, 3, 7, 11, 3]
# print(l.count(3))

# l = ['a', 'b', 'c', 'a']
# l.remove('a')
# print(l)

# l = [1, 2, 3]
# l.insert(0, 'A')將A移到0的位置
# print(l)

# l = [1, 2, 3]
# l.pop():移除最後的數字
# print(l)

# l = [1, 2, 3]
# l.pop(0):移除編號(0)
# print(l)

# l = [3, 1, 5, 4, 2]
# l.sort():由小排到大
# print(l)

# l = [3, 1, 5, 4, 2]
# l.sort(reverse(相反)=True):由大排到小
# print(l)

# l = [3, 1, 5, 4, 2]
# l.reverse():左右相反，l變成[2,4,5,1,3]
# print(l)

# l = ['a', 'b', 'c', 'a']
# index = l.index('a'):找a的位置
# print(index)
l = []
while True:
    x = input('輸入e就離開程式，請輸入想新增的資料:')
    if x == 'e':
        print('881')
        break
    else:
        l.append(x)
        print(l)
while True:
    ans = input('輸入e就離開程式，請輸入想移除的資料:')
    if ans == 'e':
        break
    else:
        while ans in l:
            l.remove(ans)
            print(l)
b = []
for x in l:
    if x in b:
        continue
    else:
        b.append(x)
for x in b:
    print(f'{x}有{l.count(x)}個')