#!/bin/bash

# STUnet Connect Linux 安装脚本
# 自动配置定时任务，简化部署流程

echo "================================================"
echo "   STUnet Connect Linux 自动安装脚本"
echo "================================================"
echo ""

# 获取脚本所在目录的绝对路径
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "✓ 检测到脚本目录: $SCRIPT_DIR"
echo ""

# 检查必需文件
echo "检查必需文件..."
REQUIRED_FILES=("auto_connect.sh" "hand_connect.sh" "auto_connect.py" "main.py")
MISSING_FILES=()

for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$SCRIPT_DIR/$file" ]; then
        MISSING_FILES+=("$file")
    fi
done

if [ ${#MISSING_FILES[@]} -gt 0 ]; then
    echo "✗ 错误: 以下必需文件缺失:"
    for file in "${MISSING_FILES[@]}"; do
        echo "  - $file"
    done
    echo ""
    echo "请确保所有文件都在同一目录下。"
    exit 1
fi

echo "✓ 所有必需文件已就绪"
echo ""

# 添加执行权限
echo "设置执行权限..."
chmod +x "$SCRIPT_DIR/auto_connect.sh" 2>/dev/null
chmod +x "$SCRIPT_DIR/hand_connect.sh" 2>/dev/null
echo "✓ 执行权限已设置"
echo ""

# 检查 Python3
echo "检查 Python3..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    echo "✓ 检测到 $PYTHON_VERSION"
else
    echo "✗ 错误: 未找到 Python3"
    echo "请先安装 Python3: sudo apt-get install python3"
    exit 1
fi
echo ""

# 询问是否配置定时任务
echo "================================================"
echo "是否要配置自动定时任务？"
echo "================================================"
echo ""
echo "推荐的定时任务配置："
echo "  - 每天 6:30 自动连接"
echo "  - 每天 7:30 自动连接"
echo "  - 每天 8:30 自动连接"
echo "  - 每天 12:00 自动连接"
echo ""
read -p "是否立即配置定时任务？(y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "准备配置定时任务..."
    echo ""
    
    # 生成 crontab 配置
    CRON_ENTRIES="
# STUnet Connect 自动认证任务
30 6 * * * $SCRIPT_DIR/auto_connect.sh
30 7 * * * $SCRIPT_DIR/auto_connect.sh
30 8 * * * $SCRIPT_DIR/auto_connect.sh
0 12 * * * $SCRIPT_DIR/auto_connect.sh
"
    
    # 检查是否已有相同的配置
    if crontab -l 2>/dev/null | grep -q "STUnet Connect"; then
        echo "⚠ 检测到已存在 STUnet Connect 定时任务"
        read -p "是否覆盖现有配置？(y/n): " -n 1 -r
        echo ""
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "取消配置定时任务"
            echo ""
            echo "你可以稍后手动配置，使用以下命令："
            echo "  crontab -e"
            echo ""
            echo "添加以下内容："
            echo "$CRON_ENTRIES"
            exit 0
        fi
        # 删除旧的 STUnet Connect 配置
        crontab -l 2>/dev/null | grep -v "STUnet Connect" | grep -v "$SCRIPT_DIR/auto_connect.sh" | crontab -
    fi
    
    # 添加新的配置
    (crontab -l 2>/dev/null; echo "$CRON_ENTRIES") | crontab -
    
    echo "✓ 定时任务配置完成"
    echo ""
    echo "当前的定时任务列表："
    echo "----------------------------------------"
    crontab -l | grep -A 5 "STUnet Connect"
    echo "----------------------------------------"
else
    echo ""
    echo "跳过定时任务配置"
    echo ""
    echo "你可以稍后手动配置，使用以下命令："
    echo "  crontab -e"
    echo ""
    echo "添加以下内容："
    echo "$CRON_ENTRIES"
fi

echo ""
echo "================================================"
echo "   安装完成！"
echo "================================================"
echo ""
echo "下一步操作："
echo "  1. 运行手动连接脚本进行首次登录："
echo "     cd $SCRIPT_DIR"
echo "     ./hand_connect.sh"
echo ""
echo "  2. 首次登录后会生成 credentials.json 和 cookies.pkl"
echo "  3. 之后定时任务会自动运行"
echo ""
echo "查看定时任务日志："
echo "  tail -f /var/log/syslog | grep CRON"
echo ""
echo "管理定时任务："
echo "  crontab -l  # 查看所有定时任务"
echo "  crontab -e  # 编辑定时任务"
echo ""
