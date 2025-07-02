import sys
from functools import lru_cache
from pathlib import Path
from typing import Optional


def runtime_path(relative_path: str) -> Optional[str]:
    """実行時の絶対パスを取得する

    以下の順番で探索を試行します。
    1. プロジェクトのルートディレクトリ基準
    2. EXE ファイル実行時の EXE 内部のルートディレクトリ基準
    3. カレントワーキングディレクトリ基準

    .env ファイルのパスの取得にも利用できます。
    見つからない場合は None を返しますが、そのまま load_dotenv() に渡すと
    load_dotenv() による探索が試行されます。

    Args:
        relative_path (str): プロジェクトのルートディレクトリからの相対パス
    Returns:
        optional[str]: 絶対パス
    """
    path = Path(project_root()) / relative_path
    if path.exists():
        return str(path)

    if exe_internal_root_dir := exe_internal_root():
        path = Path(exe_internal_root_dir) / relative_path
        if path.exists():
            return str(path)

    path = Path.cwd() / relative_path
    return str(path) if path.exists() else None


@lru_cache(maxsize=1)
def project_root() -> str:
    """プロジェクトのルートディレクトリの絶対パスを取得する

    Returns:
        str: 絶対パス
    """
    if getattr(sys, "frozen", False):
        # PyInstaller でビルドされている場合 (EXE ファイル実行)
        return str(Path(sys.executable).resolve().parent)

    if dir := _resolve_project_root_from_module_depth():
        return dir

    # 対話モードや Notebook で実行されている場合はカレントワーキングディレクトリとする
    return str(Path.cwd())


@lru_cache(maxsize=1)
def exe_internal_root() -> Optional[str]:
    """EXE ファイル実行時の EXE 内部のルートディレクトリの絶対パスを取得する

    Returns:
        Optional[str]: 絶対パス
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return str(sys._MEIPASS)

    # ビルドされていない場合
    return None


@lru_cache(maxsize=1)
def _resolve_project_root_from_module_depth() -> Optional[str]:
    """このモジュール基準でプロジェクトのルートディレクトリの絶対パスを解決して取得する

    Returns:
        optional[str]: 絶対パス
    """
    if globals().get("__file__") is None:
        # 対話モードや Notebook で実行されている場合
        return None

    dir = Path(__file__).resolve().parent

    for _ in range(_module_depth_from_project_root()):
        dir = dir.parent

    return str(dir)


@lru_cache(maxsize=1)
def _module_depth_from_project_root() -> int:
    """プロジェクトのルートディレクトリからの、このモジュールの階層数を取得する

    e.g. util/path_utils.py -> 1

    Returns:
        int: 階層数
    """
    # 注: __name__ が "__main__" である場合は想定していない
    # e.g. "util.path_utils" -> ["util", "path_utils"]
    package_parts = __name__.split(".")
    return len(package_parts) - 1
