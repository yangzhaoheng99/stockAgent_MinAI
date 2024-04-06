from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from fastapi import FastAPI
from langserve import add_routes
import dotenv
dotenv.load_dotenv()

template = """请扮演一个资深的炒股专家，您将负责为用户解答股票相关的问题。
    分析出用户提出的问题，通过搜索相关内容综合给出专业性的回答。
"""

prompt = ChatPromptTemplate.from_messages([('system',template),("human","{input}")])

model = ChatOpenAI()

chain = prompt | model | StrOutputParser()

app = FastAPI(title="AIStockAgent",
              description="基于LangChain构建并由LangServe部署的智能股票分析API")

add_routes(app,chain,path="/stock")

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)


