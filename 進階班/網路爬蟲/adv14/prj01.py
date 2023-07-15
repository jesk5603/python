######################匯入模組########################
import sys
import os
from apple.apple import *

#######################初始化########################
os.chdir(sys.path[0])  # 將工作目錄設置為目前檔案所在的目錄

#######################取得影片資訊########################
url = "https://www.youtube.com/watch?v=WlfIYn8-1pI"
title, author, length, thumbnail_url, res = get_video_info(url)
print(f"影片解析度:{res}")

#######################下載影片########################
r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p):")
result = "下載完成" if download_video(url, r) else "下載失敗"
print(result)

#######################切割影片########################

beg = int(input("請輸入要切割的開始時間(秒):"))
end = int(input("請輸入要切割的結束時間(秒):"))
result = "剪輯完成" if cut_video(f"{title}.mp4", beg, end) else "剪輯失敗"
print(result)