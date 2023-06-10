#######################模組#######################
import discord  # pip install -U py-cord
import os
from dotenv import load_dotenv  # pip install -U python-dotenv
from apple import apple
#######################初始化#######################

# 載入環境變數
load_dotenv()

# 建立機器人
bot = discord.Bot()


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


#######################指令#######################
@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    """輸入hello, 會回傳Hey!"""
    await ctx.respond("Hey!")


@bot.slash_command(name="weather",
                   description="Get the weather of the next 7 days")
async def weather(ctx):
    """輸入weather, 會回傳未來七天溫度的圖表"""
    info = apple.call_weather_api()
    dates, temps = apple.get_7_Days_weather(info)
    icon_code = info["current"]["weather"][0]["icon"]
    apple.save_weather_icon(icon_code)
    fig = apple.get_plot_fig(dates, temps, f"{info['timezone']}未來七天溫度", "日期",
                             "溫度")
    fig.savefig("weather.png")
    await ctx.respond(file=discord.File("weather.png"))
    await ctx.respond(file=discord.File(f"{icon_code}.png"))


@bot.slash_command(name='repeat', description='可以重複顯示特定次數的文字')
@discord.option(name='times', description='要重複的次數')
async def repeat(ctx, times: int):
    result = ''
    for i in range(times):
        result += f'重複第{i+1}次\n'
    await ctx.respond(result)


@bot.slash_command(name='yt_info', description='顯示影片資訊')
@discord.option(name='url', description='輸入連結', required=True)
async def yt_info(ctx, url: str):
    title, author, length, image_url, res = apple.get_video_info(url)
    result = f'標題:{title}\n作者:{author}\n長度:{length}\n圖片:{image_url}\n可下載的解析度有:{res}'
    await ctx.respond(result)


#######################啟動#######################
def main():
    # 讀取環境變數, 並啟動機器人
    bot.run(os.getenv('TOKEN'))


# 主程式, 這樣寫是為了讓程式碼更有模組化, 同時可以當作模組使用
if __name__ == "__main__":
    main()