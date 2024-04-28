###匯入模組
import adv07.mcu as mcu


###函式與類別定義


###宣告和設定
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)

if wi.connect():
    print(f"IP={wi.ip}")
