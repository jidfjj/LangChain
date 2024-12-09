import os
import time

def printENV():
    # 获取所有环境变量
    env_vars = os.environ
    # 打印指定的环境变量
    for key, value in env_vars.items():
        if key in ["OPENAI_API_KEY", "TAVILY_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]:
            print(f"{key}: {value}")

def evalEndTime(start_time):
    # 获取结束时间
    end_time = time.time()
    # 计算程序运行时间
    execution_time = "(程序运行时间：%.2f 秒)" % (
        end_time - start_time
    )
    return execution_time
