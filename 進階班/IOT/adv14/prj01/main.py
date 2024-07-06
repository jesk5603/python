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


#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()

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
    你只能根據使用者的回應來決定要回答'ON','OFF','open','close','None'
                """
            ),
            HumanMessage(content=ans),
        ]
    ).content
    result = client.publish("hello", msg)  # 發布訊息
    result.wait_for_publish()  # 等待發布完成

    # 檢查發布是否成功
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")
    else:
        print("Failed to publish message")
    time.sleep(0.1)
