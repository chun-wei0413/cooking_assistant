# src/main.py
from src.chain import create_conversation_chain


def main():
    """
    主程式，運行烹飪對話助手。
    """
    print("歡迎使用烹飪對話助手！輸入 '退出' 以結束對話。")
    conversation = create_conversation_chain()

    while True:
        user_input = input("你：")
        if user_input.lower() == "退出":
            print("助手：再見！")
            break
        config = {"configurable": {"session_id": "default_session"}}
        response = conversation.invoke({"input": user_input}, config)
        print("助手：" + response.content)


if __name__ == "__main__":
    main()