'''
你是運動App的程式設計師。你必須製作一個函式為跑者計算步速,
所謂步速就是每公里所花的時間就是步速。輸出結必須盡可能精準。
要如何完成程式碼?請在回答區中擇適當的程式碼片段。
其中距離轉換為浮點數，分秒的輸入值都要轉換為整數。
'''
#步速計算器
distance = (1)(input("請輸入以公尺為單位的行驶距離"))
distance_kms = distance / 1000  # 轉換為公里
time_minute = (2)(input("請输入經過分鐘"))
time_sec = (3)(input("請輸入經過秒数"))
time = time_minute * 60 + time_sec
pace = time / distance_kms
print("步速是: ", str((pace // 60)) + ":" + str((pace % 60)))
'''
以上空格分別要填入的函式名為:
(C)(1) A. int B. string C. float
(A)(2) A. int B. string C. float
(A)(3) A. int B. string C. float
'''
