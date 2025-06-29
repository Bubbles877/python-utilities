# env_settings - Environment Variable Settings

[日本語 Readme](./README.ja.md)

## 1. Overview

Collection of environment-variable settings classes using `pydantic-settings`.

## 2. Key Features

Simply instantiating a class loads values from environment variables.

The following settings classes are provided:

- LLM settings
- Slack settings

## 3. Installation

Place the following files under `util/` (or your preferred package directory):

- [llm_settings - LLM settings](./llm_settings.py)
- [slack_settings - Slack settings](./slack_settings.py)

## 4. Usage

1. Set up the required environment variables
2. Call the classes from your code

### 4.1. Setting environment variables

Environment variables are required.

Create a `.env` file at the project root in your local environment and set the environment variables.  
[.env.example](./.env.example) is the template.

Available environment variables:

#### LLM settings

- LLM_PROVIDER
  - LLM provider (e.g. `azure`, `ollama`, `openai`)
- LLM_NAME
  - LLM model name (e.g. Azure: gpt-4.1-mini, Ollama: qwen2.5:32b, gemma3:12b)
- LLM_DEPLOY_NAME
  - LLM deployment name (e.g. Azure: gpt-4.1-mini-dev-001)
- LLM_ENDPOINT
  - URL of the LLM API (e.g. Azure: `https://oai-foo-dev.openai.azure.com/`, Ollama: `http://localhost:11434/`, OpenAI: `https://api.openai.com/`)
- LLM_API_KEY
  - LLM API key
- LLM_API_VER
  - LLM API version (e.g. Azure: 2025-01-01-preview)
- LLM_TEMPERATURE
  - Diversity of LLM Outputs (0.0–1.0)

#### Slack settings

- SLACK_IS_SOCKET_MODE
  - Whether to run in socket mode (`True`, `False`)
  - For local development purposes
- SLACK_APP_TOKEN
  - App-level token
  - Required for socket mode
- SLACK_BOT_TOKEN
  - Bot token
- SLACK_SIGNING_SECRET
  - Signing secret
- SLACK_MAX_THREAD_MESSAGES
  - Maximum number of messages to retrieve within a thread

### 4.2. Calling from code

Call as in the example below.  
**Note:** If placed in `util/setting/`

```python
from util.setting.llm_settings import LLMSettings
from util.setting.slack_settings import SlackSettings

llm_settings = LLMSettings()
# If you want to change the file specified in the class, specify it with _env_file
slack_settings = SlackSettings(_env_file="test/.env")

print(f"LLM settings:\n{llm_settings.model_dump_json(indent=2)}")
print(f"Slack settings:\n{slack_settings.model_dump_json(indent=2)}")
```

## 5. Dependencies & Verified Versions

- Python 3.12.10
- pydantic-settings 2.9.1

## 6. Repository

- [Bubbles877/python-utilities](https://github.com/Bubbles877/python-utilities)
