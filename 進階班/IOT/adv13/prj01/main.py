import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.2)
from langchain_core.messages import HumanMessage

while True:
    ans = input("請輸入想跟AI說的話: ")
    print(
        model.invoke(
            [
                HumanMessage(
                    content="""
    你是一個負責開關燈和開關車庫門的管理員
    'ON'代表開燈
    'OFF'代表關燈
    'open'代表開啟車庫門
    'close'代表關閉車庫門
    'None'代表不做任何事
    你只能根據使用者的回應來決定要回答'ON','OFF','open','close','None'
                """
                ),
                HumanMessage(content=ans),
            ]
        ).content
    )
