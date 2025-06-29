# path_utils - パスユーティリティ

## 1. 概要

ファイルパスのユーティリティです。

## 2. 主な機能

- プロジェクトのルートディレクトリからの相対パスを指定して、実行時の状況に合わせた絶対パスを取得
  - Python スクリプトでの実行と EXE ファイルでの実行による違いや、カレントディレクトリの差異などを吸収
- プロジェクトのルートディレクトリの絶対パスを取得
- EXE ファイル実行時の EXE 内部のルートディレクトリの絶対パスを取得

## 3. インストール

以下を `util/` などに配置してください。

- [path_utils - パスユーティリティ](./path_utils.py)

## 4. 使い方

以下の例のように呼び出します。

```python
import util.path_utils as path_utils

env_file_path = path_utils.runtime_path(".env")
setting_file_path = path_utils.runtime_path("data/setting.txt")
```

## 5. 依存関係 & 動作確認済みバージョン

- Python 3.12.10

## 6. リポジトリ

- [Bubbles877/python-utilities](https://github.com/Bubbles877/python-utilities)
