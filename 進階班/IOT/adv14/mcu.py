import sys
import network
from machine import Pin, PWM
from umqtt.simple import MQTTClient


class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SDD3 = 10
        self._SDD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SDD3(self):
        return self._SDD3

    @property
    def SDD2(self):
        return self._SDD2


class wifi:
    def __init__(self, ssid=None, password=None):
        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)
        self.ssid = ssid
        self.password = password
        self.ap_active = False
        self.sta_active = False
        self.ip = None

    def setup(self, ap_active=False, sta_active=False):
        self.ap_active = ap_active
        self.sta_active = sta_active
        self.ap.active(ap_active)
        self.sta.active(sta_active)

    def scan(self):
        if self.sta_active:
            wifi_list = self.sta.scan()
            print("Scan result:")
            for i in range(len(wifi_list)):
                print(wifi_list[i][0])
        else:
            print("STA模式未啟動")

    def connect(self, ssid=None, password=None) -> bool:
        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password

        if not self.sta_active:
            print("STA模式未啟動")
            return False

        if ssid is None or password is None:
            print("WIFI 名稱或密碼尚未設定")
            return False

        if self.sta_active:
            self.sta.connect(ssid, password)
            while not self.sta.isconnected():
                pass
            self.ip = self.sta.ifconfig()[0]
            print("connect successfully", self.sta.ifconfig())
            return True


class LED:
    def __init__(self, r_pin, g_pin, b_pin, pwm: bool = False):
        """
        LED 類別用於管理 RGB LED。

        屬性:
            RED (Pin): 紅色 LED。
            GREEN (Pin): 綠色 LED。
            BLUE (Pin): 藍色 LED。

        方法:
            __init__(r_pin, g_pin, b_pin, pwm=False): 初始化 LED。
            當 pwm=False 時，使用 Pin 控制 LED。
            當 pwm=True 時，使用 PWM 控制 LED。
        """
        if pwm == False:
            self.RED = Pin(r_pin, Pin.OUT)
            self.GREEN = Pin(g_pin, Pin.OUT)
            self.BLUE = Pin(b_pin, Pin.OUT)
        else:
            frequency = 1000
            duty_cycle = 0
            self.RED = PWM(Pin(r_pin), freq=frequency, duty=duty_cycle)
            self.GREEN = PWM(Pin(g_pin), freq=frequency, duty=duty_cycle)
            self.BLUE = PWM(Pin(b_pin), freq=frequency, duty=duty_cycle)


class MQTT:
    def __init__(self, mqttClientId, mq_server, mqtt_username, mqtt_password):
        self.mq_server = "mqtt.singularinnovation-ai.com"
        self.mqttClientId = "stepjen"
        self.mqtt_username = "singular"
        self.mqtt_password = "Singular#1234"
        self.Client = MQTTClient(
            mqttClientId,
            mq_server,
            user=mqtt_username,
            password=mqtt_password,
            keepalive=30,
        )

    def connect(self):
        try:
            self.Client.connect()
        except:
            sys.exit()
        finally:
            print("connected MQTT server")

    def subscribe(self, topic, on_message):
        self.Client.set_callback(on_message)  # 設定接收訊息的時候要呼叫的函式
        self.Client.subscribe(topic)

    def check_msg(self):
        self.Client.check_msg()  # 等待已訂閱的主題發送資料
        self.Client.ping()  # 持續確認是否還保持連線

    def publish(self, topic: str, msg: str):
        """
        發布一個訊息。

        參數:
            topic (str): 要發布的主題。
            msg (str): 要發布的訊息。
        """
        topic = topic.encode("utf-8")
        msg = msg.encode("utf-8")
        self.Client.publish(topic, msg)


class Servo:
    def __init__(self, sg_pin):
        self.sg = PWM(Pin(sg_pin), freq=50)

    def angle(self, angle: int):
        if 0 <= angle <= 180:
            self.sg.duty(int(1023 * (0.5 + angle / 90) / 20))
