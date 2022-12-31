# import datetime as d

# a = (d.date.today())
# b = d.datetime.strptime((input('請輸入你的生日(月/日/年)')), '%m/%d/%Y').date()
# s = b - a
# print(f'距離下次生日還有{s.days}天')

# import datetime
# Time = datetime.datetime.now()
# print(Time)
# print(Time.hour)
# print(Time.minute)
# print(Time.second)

# #  #1. 要開啟的檔名
# fileName = "class13/class/class.txt"
# #2. 指定w/ r /a mode
# Mode = "w"
# #3. 開啟檔案
# myFile = open(fileName, Mode)
# #4. 寫入檔案 \n 換行符號
# myFile.write("Hi\n")
# myFile.write("How old are you?")
# #5. 關閉檔案
# myFile.close()

# fileName = "class13/class/class.txt"
# #2. 指定w/ r /a mode
# Mode = "a"
# #3. 開啟檔案
# myFile = open(fileName, Mode)
# #4. 寫入檔案 \n 換行符號
# myFile.write("Hi\n")
# myFile.write("My age is 18")
# #5. 關閉檔案
# myFile.close()

# #1. 要開啟的檔名
# path = "class13/class/class.txt"
# #2. 指定w/ r /a mode
# f = open(path, 'r')
# #3. 讀取檔案並顯示
# total = f.read()
# print(total)
# f = open(path, 'r')
# lines = f.readline()
# print(lines)
# f = open(path, 'r')
# line = f.readlines()
# print(line)
# #4. 關閉檔案
# f.close()

fileName = 'class13/class/score.txt'
Mode = 'w'
myFile = open(fileName, Mode)
myFile.write("Peter:90\n")
myFile.write("Tom:70\n")
myFile.write("John:80")
myFile.close()
fileName = 'class13/class/score.txt'
Mode = 'a'
myFile = open(fileName, Mode)
myFile.write('\nRob:95')
myFile.close()
path = "class13/class/score.txt"
f = open(path, 'r')
total = f.read()
print(total)
f.close()