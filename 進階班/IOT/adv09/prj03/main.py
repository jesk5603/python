import paho.mqtt.client as mqtt
import time


def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message{mid} has beem published")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)  # 建立MQTT客戶端
client.on_publish = on_publish  # 設定MQTT客戶端的回傳函式
client.username_pw_set("singular", "Singular#1234")  # 設定MQTT客戶端的用戶名和密碼
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)  # 連線到MQTT服務器
client.loop_start()

while True:
    msg = input("請輸入想上傳MQTT的訊息")
    result = client.publish("hello", msg)
    result.wait_for_publish()

    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")
    else:
        print("Failed to publish message")
    time.sleep(0.1)
