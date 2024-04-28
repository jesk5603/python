###匯入模組
import paho.mqtt.client as mqtt


###函式與類別定義
def on_connect(client, underdata, connect_flags, reason_code, properties):
    print(f"連線結果:{reason_code}")
    client.subscribe("watermelon")  # 訂閱主題a


def on_massage(client, userdata, msg):
    print(f'我訂閱的主題式:{msg.topic},收到訊息:{msg.payload.decode("utf-8")}')


###宣告與設定
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_massage
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_forever()
