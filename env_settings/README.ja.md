# env_settings - 環境変数設定

[English Readme](./README.md)

## 1. 概要

`pydantic-settings` を利用した環境変数設定クラスのコレクションです。

## 2. 主な機能

クラスをインスタンス化するだけで、環境変数から設定を読み込めます。

以下、定義したものがあります。

- LLM 設定
- Slack 設定

## 3. インストール

以下を `util/setting/` などに配置してください。

- [llm_settings - LLM 設定](./llm_settings.py)
- [slack_settings - Slack 設定](./slack_settings.py)

## 4. 使い方

1. 環境変数を設定する
2. プログラムから呼び出す

### 4.1. 環境変数の設定

環境変数の設定が必要です。

ローカル環境ではプロジェクトのルートに `.env` を作成して環境変数を設定してください。  
[.env.example](./.env.example) がテンプレートです。

以下の環境変数があります。

#### LLM 設定

- LLM_PROVIDER
  - LLM プロバイダ (e.g. `azure`, `ollama`, `openai`)
- LLM_NAME
  - LLM のモデル名 (e.g. Azure: gpt-4.1-mini, Ollama: qwen2.5:32b, gemma3:12b)
- LLM_DEPLOY_NAME
  - LLM デプロイ名 (e.g. Azure: gpt-4.1-mini-dev-001)
- LLM_ENDPOINT
  - LLM API の URL (e.g. Azure: `https://oai-foo-dev.openai.azure.com/`, Ollama: `http://localhost:11434/`, OpenAI: `https://api.openai.com/`)
- LLM_API_KEY
  - LLM API のキー
- LLM_API_VER
  - LLM API のバージョン (e.g. Azure: 2025-01-01-preview)
- LLM_TEMPERATURE
  - LLM の出力の多様性 (0.0-1.0)

#### Slack 設定

- SLACK_IS_SOCKET_MODE
  - ソケットモードで実行するかどうか (`True`, `False`)
  - ローカルでの開発用途
- SLACK_APP_TOKEN
  - アプリレベルトークン
  - ソケットモードで必要
- SLACK_BOT_TOKEN
  - ボットトークン
- SLACK_SIGNING_SECRET
  - 署名シークレット
- SLACK_MAX_THREAD_MESSAGES
  - スレッド内の取得するメッセージの最大数

### 4.2. プログラムからの呼び出し

以下の例のように呼び出します。  
※`util/setting/` に配置している場合

```python
from util.setting.llm_settings import LLMSettings
from util.setting.slack_settings import SlackSettings

llm_settings = LLMSettings()
# クラス内で指定しているファイルと変えたい場合は _env_file で指定する
slack_settings = SlackSettings(_env_file="test/.env")

print(f"LLM settings:\n{llm_settings.model_dump_json(indent=2)}")
print(f"Slack settings:\n{slack_settings.model_dump_json(indent=2)}")
```

## 5. 依存関係 & 動作確認済みバージョン

- Python 3.12.10
- pydantic-settings 2.9.1

## 6. リポジトリ

- [Bubbles877/python-utilities](https://github.com/Bubbles877/python-utilities)
