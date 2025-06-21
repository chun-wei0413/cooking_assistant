from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def load_model():
    """
    載入並返回語言模型。
    目前使用 DistilGPT-2，你可以根據需求替換成其他模型。
    """
    model = HuggingFacePipeline.from_model_id(
        model_id="distilgpt2",
        task="text-generation",
        pipeline_kwargs={"max_new_tokens": 100}
    )
    return model