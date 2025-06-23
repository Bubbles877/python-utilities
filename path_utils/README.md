# path_utils - パスユーティリティ

## 1. 概要

ファイルパスのユーティリティです。

## 2. 主な機能

Python スクリプトでの実行、EXE ファイルでの実行による違いや、カレントディレクトリの差異などを吸収して、  
実行時の絶対パスを取得します。

- プロジェクトのルートディレクトリからの相対パスから、実行時の状況に合わせて絶対パスを取得する
- プロジェクトのルートディレクトリの絶対パスを取得する
- EXE ファイル実行時の内部のルートディレクトリの絶対パスを取得する

## 3. 組み込み

以下を util/ などにインポートしてください。

- [path_utils - パスユーティリティ](path_utils.py)

## 4. 使い方

以下の例のように呼び出します。

```python
import util.path_utils as path_utils

env_file_path = path_utils.runtime_path(".env")
setting_file_path = path_utils.runtime_path("data/setting.txt")
```

## 5. 対応環境

以下のバージョンで動作を確認しています。

- Python 3.12.10

## 6. リポジトリ

- [Bubbles877/python-utilities](https://github.com/Bubbles877/python-utilities)
