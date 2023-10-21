######################匯入模組########################
import sys
import os
from apple.apple import *

#######################初始化########################
os.chdir(sys.path[0])  # 將工作目錄設置為目前檔案所在的目錄

#######################取得影片資訊########################
ur = input('請輸入影片網址(n:跳過):')
if ur != 'n':
    url = "https://www.youtube.com/watch?v=J7tBiUCOap0"
    title, author, length, thumbnail_url, res = get_video_info(url)
    print(f"影片解析度:{res}")

# #######################下載影片########################

r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p/n為跳過):")
if r != 'n':
    result = "下載完成" if download_video(url, r) else "下載失敗"
    print(result)

#######################切割影片########################
r = input('要不要切割影片(n:跳過):')
if r != 'n':
    beg = int(input("請輸入要切割的開始時間(秒):"))
    end = int(input("請輸入要切割的結束時間(秒):"))
    result = "剪輯完成" if cut_video(f"{title}.mp4", beg, end) else "剪輯失敗"
    print(result)

#######################合併影片########################
r = input('要不要合併影片(n:跳過):')
if r != 'n':
    file_name_list = [
        "Minecraft 你可以變成【麥塊♂️植物人】破關麥塊嗎？不能移動😂！只有01高手可以通關 !! 生存１００天【變超強🔥大樹哥】!! 麥塊♡超爆笑♡的【變身生存】😂!! 全字幕.mp4",
        'Minecraft 我下載了【盜版麥塊💲超騙錢】你敢信😂！鑽石居然要600台幣😰！史上最爆笑♂️只能【花錢通關】的麥塊版本XD！從頭到尾瘋狂課金！全字幕.mp4'
    ]
    # for i in range(1):
    #     file_name_list.append()

    # file_name_list = ["【小小兵】第三支精采可愛預告-9-10.mp4", "【小小兵】第三支精采可愛預告-9-10.mp4", "【小小兵】第三支精采可愛預告-9-10.mp4"]
    result = "合併影片成功" if merge_video(file_name_list, "合併影片.mp4") else "合併影片失敗"
    print(result)

# 影片轉GIF
r = input('要不要影片轉GIF(n:跳過):')
if r != 'n':
    video_path = '合併影片.mp4'
    gif_path = 'BoB.gif'
    result = '影片轉GIF成功' if video_to_gif(video_path, gif_path) else '影片轉GIF失敗'
    print(result)