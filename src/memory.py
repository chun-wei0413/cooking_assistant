from langchain.memory import ConversationBufferMemory

def create_memory():
    """
    創建並返回對話記憶。
    目前使用 ConversationBufferMemory，你可以根據需求替換成其他記憶類型。
    """
    memory = ConversationBufferMemory()
    return memory