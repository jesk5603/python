#########################匯入模組#########################
import paho.mqtt.client as mqtt
import time
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.2)
from langchain_core.messages import HumanMessage


#########################函式與類別定義#########################
def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


def on_connect(client, userdata, connect_flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("home")


def on_message(client, userdata, msg):
    global home_config
    print(f"我訂閱的主題是 {msg.topic},收到的訊息是 {msg.payload.decode('utf-8')}")
    home_config = msg.payload.decode("utf-8")


#########################宣告與設定#########################
# client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
# client.on_publish = on_publish
# client.username_pw_set("singular", "Singular#1234")
# client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
# client.loop_start()
# home_config = "None"
home_config = """
{"humidity": 0, "temperature": 0, "lightsensor": 1000}
"""
#########################主程式#########################

while True:
    ans = input("請輸入想跟AI說的話: ")
    msg = model.invoke(
        [
            HumanMessage(
                content="""
    你是一個負責開關燈和開關車庫門的管理員
    'ON'代表開燈
    'OFF'代表關燈
    'open'代表開啟車庫門
    'close'代表關閉車庫門
    'None'代表不做任何事
    'HOME_CONFIG'代表正在詢問目前家裡狀態
    你只能根據使用者的回應來決定要回答'ON','OFF','open','close','None','HOME_CONFIG'
                """
            ),
            HumanMessage(content=ans),
        ]
    ).content
    # result = client.publish("hello", msg)  # 發布訊息
    # result.wait_for_publish()  # 等待發布完成
    print(f"發布的訊息是 {msg}")

    # 檢查發布是否成功
    # if result.rc == mqtt.MQTT_ERR_SUCCESS:
    #     print("Message published successfully")
    # else:
    #     print("Failed to publish message")
    # time.sleep(0.1)
    if msg == "HOME_CONFIG":
        msg = model.invoke(
            [
                HumanMessage(
                    content="""
        你是一個負責解釋家裡狀態的小幫手，你只能回答100個字，
                感測器位置沒有問題，光感應器數值越大代表越暗，數值範圍在0~1023之間，
                有問題請解釋可能發生災難或狀況，
                家裡感測器不可能壞掉喔!，目前家裡的狀態是:
                """
                ),
                HumanMessage(content=home_config),
            ]
        ).content
        print(msg)
