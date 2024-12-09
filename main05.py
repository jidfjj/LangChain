import os, pprint, json, time
from common import *
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

start_time = time.time()  # 获取开始时间
load_dotenv()

messages = [
    # SystemMessage("你是一位幽默大师,你的回答经常会让客户捧腹大笑。"),
    # HumanMessage("你好"),
    # HumanMessage("我想去澳洲留学,给我一些建议好吗?"),

    # example 2
    SystemMessage("你是一位语言专家，精通英文和中文"),
    AIMessage("当然可以，请告诉我你需要翻译的英文内容，我会尽力帮我翻译成中文"),
    HumanMessage("book"),
]

model = ChatOpenAI(model="gpt-4o-mini")

result = model.invoke(messages)
print(result.content)

print()
print(evalEndTime(start_time))
