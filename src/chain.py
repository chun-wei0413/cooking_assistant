# src/chain.py
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from src.model import load_model
from src.prompts import get_cooking_prompt


def get_session_history(session_id: str):
    """
    獲取特定會話的歷史記錄。
    這裡使用一個簡單的 InMemoryChatMessageHistory 實例。
    """
    return InMemoryChatMessageHistory()


def create_conversation_chain():
    """
    創建並返回對話鏈。
    使用 RunnableWithMessageHistory 並確保輸出為 AIMessage。
    """
    model = load_model()
    memory = InMemoryChatMessageHistory()
    prompt = get_cooking_prompt()

    # 定義輸入格式，提取 input 和 history
    def format_input(input_data):
        return {
            "history": "\n".join([msg.content for msg in memory.messages]) if memory.messages else "",
            "input": input_data
        }

    # 將模型輸出包裝為 AIMessage
    def format_output(output):
        return AIMessage(content=output.strip() if isinstance(output, str) else str(output))

    # 創建鏈條
    chain = (
            format_input  # 格式化輸入
            | prompt  # 應用提示模板
            | model  # 讓模型生成回應
            | format_output  # 格式化輸出
    )

    conversation = RunnableWithMessageHistory(
        runnable=chain,
        get_session_history=get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    return conversation