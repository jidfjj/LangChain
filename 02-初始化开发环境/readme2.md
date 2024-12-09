ctrl shilf p
select interpreter

python -V
python -m venv _pvenv_

source _pvenv_/bin/activate
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
_pvenv_\Scripts\activate


python -m pip install --upgrade pip

pip install \
langchain==0.2.7 \
langchain-community==0.2.7 \
langchain-aws==0.1.11 \
langchain-openai==0.1.16 \
langchainhub==0.1.20 \
chromadb==0.5.4 \
wikipedia==1.4.0 \
tavily-python==0.3.5 \
python-dotenv==1.0.1

pip install langchain==0.2.7 langchain-community==0.2.7 langchain-aws==0.1.11 langchain-openai==0.1.16 langchainhub==0.1.20 chromadb==0.5.4 wikipedia==1.4.0 tavily-python==0.3.5 python-dotenv==1.0.1

# 生成环境文件
cat << EOF > .env
OPENAI_API_KEY=123
TAVILY_API_KEY=456
ANTHROPIC_API_KEY=789
GOOGLE_API_KEY=XYZ
EOF

echo OPENAI_API_KEY=123 > .env
echo TAVILY_API_KEY=456 >> .env
echo ANTHROPIC_API_KEY=789 >> .env
echo GOOGLE_API_KEY=XYZ >> .env
＊这个文件要保存为utf-8否则会出错

# 编辑程序
nano common.py
nano main.py

# 运行程序
python main.py

.gitignore
_pvenv_/
