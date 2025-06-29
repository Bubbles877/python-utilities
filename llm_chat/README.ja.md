# llm_chat - LLM チャット

[English Readme](./README.md)

## 1. 概要

LLM とのチャットを管理します。

## 2. 主な機能

- システムプロンプトの設定・更新
- LLM に渡す会話履歴の最大数の設定
- LLM の呼び出し (同期/非同期)

## 3. インストール

以下を `util/` などに配置してください。

- [llm_chat - LLM チャット](./llm_chat.py)

## 4. 使い方

以下の例のように呼び出します。

```python
from typing import Optional

from langchain_core.messages import AIMessage, AnyMessage, HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from util.llm_chat import LLMChat


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    base_url="https://api.openai.com/",
    api_key=SecretStr("***"),
    temperature=0.8,
)
llm_chat = LLMChat(llm, max_messages=-1)
llm_chat.configure("You are a helpful assistant.")

message = "What is the capital of Japan?"
history: list[AnyMessage] = []  # 必要に応じて会話履歴を設定する
history.append(HumanMessage(content="What is the capital of France?"))
history.append(AIMessage(content="The capital of France is Paris."))

response = llm_chat.invoke(message, history)
print(response)  # e.g. The capital of Japan is Tokyo.
```

## 5. 依存関係 & 動作確認済みバージョン

- Python 3.12.10
- langchain 0.3.25
- langchain-core 0.3.59
- loguru 0.7.3

## 6. リポジトリ

- [Bubbles877/python-utilities](https://github.com/Bubbles877/python-utilities)
