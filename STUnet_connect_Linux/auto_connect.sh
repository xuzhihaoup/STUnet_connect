#!/bin/bash

# 自动获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 切换到脚本目录并执行 Python 脚本
cd "$SCRIPT_DIR"
python3 "$SCRIPT_DIR/auto_connect.py"

