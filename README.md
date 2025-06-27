# Intro
[Langchain](docs/langchain.md)

# 烹飪對話助手

這是一個使用 LangChain 構建的簡單烹飪對話助手，能夠回答烹飪相關問題並記住對話上下文。

## 安裝

1. 克隆此專案。
2. 創建虛擬環境並啟動：`python -m venv venv && source venv/bin/activate`
3. 安裝依賴：`pip install -r requirements.txt`

## 運行

運行 `python src/main.py` 即可啟動對話助手。

## 擴展

- 替換模型：修改 `src/model.py` 中的 `model_id`。
- 調整提示：修改 `src/prompts.py` 中的模板。
- 添加新功能：例如加入工具或網頁介面。
