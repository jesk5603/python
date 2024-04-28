#########################匯入模組#########################
from umqtt.simple import MQTTClient
import sys
import time as t
import mcu


#########################函式與類別定義#########################
def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
if wi.connect():
    print(f"IP={wi.ip}")
mq_sever = "mqtt.singularinnovation-ai.com"
mqttClientID = "watermelon"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    mqttClientID, mq_sever, user=mqtt_username, password=mqtt_password, keepalive=30
)
try:
    mqClient0.connect()
except:
    sys.exit()
finally:
    print("connected MQTT sever")
mqClient0.set_callback(on_message)
mqClient0.subscribe("stephen")
#########################主程式#########################
while True:
    mqClient0.check_msg()
    mqClient0.ping()
    t.sleep(0.5)
