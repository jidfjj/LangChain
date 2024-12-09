import os, pprint, json, time
from common import *
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

start_time = time.time()  # 获取开始时间

load_dotenv()  # 读取 .env 文件

model = ChatOpenAI(model="gpt-4o-mini")

result = model.invoke("你好")
# result = model.invoke("我想去澳洲留学，给我一些建议好吗？")
pprint.pprint(result)
pprint.pprint(result.content)

print()
print(evalEndTime(start_time))
