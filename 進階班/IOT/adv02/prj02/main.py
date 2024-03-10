import os

# 檔案管理


# 列出當前工作目錄
print(os.listdir())
# 創建新文件
with open("new_file.txt", "w") as f:
    f.write("Hellow,MicroPython")

print(os.listdir())
# 刪除文件
os.remove("new_file.txt")

print(os.listdir())
