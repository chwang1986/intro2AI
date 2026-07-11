#!/bin/bash
# ============================================================
# Intro2AI GitHub 推送脚本
# 功能：安全地拉取、提交、推送到 GitHub
# 用法：
#   ./push-to-github.sh              # 交互式输入提交信息
#   ./push-to-github.sh "提交说明"   # 直接指定提交信息
# ============================================================

cd "$(dirname "$0")"

REPO_URL="https://github.com/chwang1986/intro2AI"
REMOTE="origin"
MAIN_BRANCH="main"
MAX_RETRY=3

# ---------- 颜色定义 ----------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ---------- 函数 ----------

# 打印带颜色的信息
info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warn() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# 检查命令是否存在
check_command() {
    if ! command -v "$1" &> /dev/null; then
        error "$1 未安装，请先安装。"
        exit 1
    fi
}

# 带重试的 git push
push_with_retry() {
    local retry=0
    while [ $retry -lt $MAX_RETRY ]; do
        if git push "$REMOTE" "$MAIN_BRANCH"; then
            return 0
        fi
        retry=$((retry + 1))
        if [ $retry -lt $MAX_RETRY ]; then
            warn "推送失败，$retry/$MAX_RETRY，5秒后重试..."
            sleep 5
        fi
    done
    return 1
}

# ---------- 主流程 ----------

echo ""
echo "========================================"
echo "  Intro2AI GitHub 推送脚本"
echo "========================================"
echo ""

# 1. 检查依赖
check_command git

# 2. 检查是否在 git 仓库中
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    error "当前目录不是 Git 仓库。"
    exit 1
fi

# 3. 获取当前分支
CURRENT_BRANCH=$(git branch --show-current)
info "当前分支：$CURRENT_BRANCH"

# 4. 如果在 main 分支上，给出提示
if [ "$CURRENT_BRANCH" = "$MAIN_BRANCH" ]; then
    warn "你正在 $MAIN_BRANCH 分支上直接工作。"
    warn "建议先创建 feature 分支：git checkout -b feature/xxx"
    echo ""
    read -p "是否继续在 main 分支上推送？(y/N): " confirm
    if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
        info "已取消。请创建 feature 分支后再试。"
        exit 0
    fi
    echo ""
fi

# 5. 显示当前状态
info "当前修改状态："
echo "----------------------------------------"
git status --short
MODIFIED_COUNT=$(git status --short | wc -l | tr -d ' ')
echo "----------------------------------------"
echo ""

if [ "$MODIFIED_COUNT" -eq 0 ]; then
    info "没有待提交的修改。"
    # 检查是否有未推送的提交
    UNPUSHED=$(git log "$REMOTE/$CURRENT_BRANCH..$CURRENT_BRANCH" --oneline 2>/dev/null | wc -l | tr -d ' ')
    if [ "$UNPUSHED" -gt 0 ]; then
        info "有 $UNPUSHED 个本地提交尚未推送。"
        echo ""
        git log "$REMOTE/$CURRENT_BRANCH..$CURRENT_BRANCH" --oneline
        echo ""
        read -p "是否直接推送这些提交？(y/N): " confirm
        if [[ "$confirm" =~ ^[Yy]$ ]]; then
            echo ""
            info "正在推送到 GitHub..."
            if push_with_retry; then
                echo ""
                success "推送成功！"
                info "仓库地址：$REPO_URL"
            else
                error "推送失败，请检查网络连接。"
                exit 1
            fi
        fi
    else
        info "本地与远程同步，无需操作。"
    fi
    exit 0
fi

# 6. 获取提交信息
COMMIT_MSG=""
if [ $# -ge 1 ]; then
    COMMIT_MSG="$1"
    shift
    # 如果有更多参数，拼接起来
    while [ $# -gt 0 ]; do
        COMMIT_MSG="$COMMIT_MSG $1"
        shift
    done
else
    echo "💡 提交信息规范："
    echo "   feat:   新增功能/内容"
    echo "   fix:    修复问题"
    echo "   docs:   文档/教程更新"
    echo "   style:  格式调整（不影响功能）"
    echo "   ref:    重构/优化"
    echo ""
    read -p "请输入提交信息：" COMMIT_MSG
    echo ""
fi

if [ -z "$COMMIT_MSG" ]; then
    error "提交信息不能为空。"
    exit 1
fi

# 7. 确认提交
info "即将执行："
echo "   git add -A"
echo "   git commit -m \"$COMMIT_MSG\""
echo "   git pull $REMOTE $MAIN_BRANCH --rebase"
echo "   git push $REMOTE $CURRENT_BRANCH"
echo ""
read -p "确认执行？(y/N): " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    info "已取消。"
    exit 0
fi
echo ""

# 8. 添加并提交
info "正在添加文件..."
git add -A

info "正在提交..."
if ! git commit -m "$COMMIT_MSG"; then
    error "提交失败。"
    exit 1
fi

# 9. 先拉取更新（避免冲突）
echo ""
info "正在拉取远程更新..."
if ! git pull "$REMOTE" "$MAIN_BRANCH" --rebase; then
    error "拉取失败，可能存在冲突。请手动解决后再试。"
    error "解决冲突后运行：git rebase --continue"
    exit 1
fi

# 10. 推送到远程
echo ""
info "正在推送到 GitHub..."
if push_with_retry; then
    echo ""
    success "推送成功！"
    echo ""
    info "仓库地址：$REPO_URL"
    info "当前分支：$CURRENT_BRANCH"
    echo ""
else
    error "推送失败，$MAX_RETRY 次重试后仍未成功。"
    error "请检查网络连接，或稍后手动运行：git push $REMOTE $CURRENT_BRANCH"
    exit 1
fi
