from langchain.prompts import PromptTemplate

def get_cooking_prompt():
    """
    返回烹飪助手的提示模板。
    這個模板可以根據需求進行調整。
    """
    template = """
    你是一個烹飪助手，請提供簡潔實用的建議。
    以下是對話歷史：
    {history}
    用戶：{input}
    助手：
    """
    return PromptTemplate(input_variables=["history", "input"], template=template)