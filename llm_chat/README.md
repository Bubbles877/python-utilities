# llm_chat - LLM Chat

[日本語 Readme](./README.ja.md)

## 1. Overview

Manage chats with LLM.

## 2. Key Features

- Set and update system prompts
- Set the maximum number of conversation-history entries to pass to the LLM
- Call the LLM (synchronous / asynchronous)

## 3. Installation

Place the following file under `util/` (or your preferred package directory):

- [llm_chat - LLM Chat](./llm_chat.py)

## 4. Usage

Call as in the example below.

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
history: list[AnyMessage] = []  # Set conversation history if necessary
history.append(HumanMessage(content="What is the capital of France?"))
history.append(AIMessage(content="The capital of France is Paris."))

response = llm_chat.invoke(message, history)
print(response)  # e.g. The capital of Japan is Tokyo.
```

## 5. Dependencies & Verified Versions

- Python 3.12.10
- langchain 0.3.25
- langchain-core 0.3.59
- loguru 0.7.3

## 6. Repository

- [Bubbles877/python-utilities](https://github.com/Bubbles877/python-utilities)
