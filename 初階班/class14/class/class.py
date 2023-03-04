1.
'''請問下列變數哪一些有問題?問題出在哪裡?
()Var = "Data"
(V 因為不能有空格)Your Name = "Data"
()Date = "Data"
(V 因為數字不能開頭)3Name = "Data"
()S12345 = "Data"
()YourPythonareVeryVeryGood = "Data"'''

2.
'''A = input("輸入您要的數值") 
#e.g. A = 1234
1.將 A 格式化成整數，並使用print顯示出來
2.以 5 個字元寬度顯示整數A，不滿 5 個則補空白
3.以 5 個字元寬度顯示整數A，不滿 5 個則補零'''
# A = int(input("輸入您要的數值"))
# print(A)
# print('%5d' % A)
# print('%05d' % A)

3.
'''A = input("輸入您要的浮點數值") 
#e.g. A = 123.456
1.將 A 格式化成浮點數，並使用print顯示出來
2.以 2 個字元寬度顯示浮點數A，不滿 2 個則補空白
3.以 2 個字元寬度顯示浮點數A，不滿 2 個則補零'''
# A = float(input("輸入您要的浮點數值"))
# print(A)
# print('%2.1f' % A)
# print('%02.1f' % A)

4.
'''請排列下方執行的先後順序
( 4 ) 加減法( +, - )
( 3 ) 乘除法( *, / )
( 2) 次方( ** )
( 1) 括弧( ( ) )
( 5) 且，或( and, or, &, | )'''

5.
'''你有4個list, 
list1裡有3個元素: 1, 2 ,3
list2裡有3個元素: 4, 5 ,6
list3等於list1加list2
list4等於list3*2
請問程式執行結果為何:'''
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = list1 + list2
# list4 = list3 * 2
# A:[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

6.
'''有一個list = ["Savage", "Orz", "Apple" ]
1.請將"94"加在list的最前面
2.請將"Pen"加在list的最後面
3.請印出"Orz" 的index
4.請印出倒數第2個元素的值
5.請將"Orz" 改成"GG"
6.請移除"GG"'''
# list = ["Savage", "Orz", "Apple"]
# list.insert(0, 94)
# list.append('Pen')
# print(list[2])
# print(list[-2])
# list[2] = 'GG'
# list.remove('GG')

7.
'''A="123456789abcdefg"
1.只顯示出efg，請將?代換掉
print( A[ -3: ] )
print( A[ 13: ] )
print( A[ -3 : 1] )
2.只顯示出147adg，請將?代換掉
print( A[ :: 3] )'''

8.
'''A="123456789abcdefg"
3.只顯示出47a，請將?代換掉
print( A[ 3: -6: 3 ] )
4.只顯示出a74，請將?代換掉
print( A[ -7 : 2 : 3 ] )'''
a = [0, 1, 2, 3, 4]
print(4 in a)
