#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
命令行待办事项程序（Todo CLI）

一个纯 Python 标准库实现的命令行待办事项管理工具。
功能包括：添加任务、列出任务、标记完成、删除任务。
数据持久化存储在 JSON 文件中。

【使用方法】
    python3 todo_cli.py add "买牛奶"         # 添加任务
    python3 todo_cli.py list               # 列出所有任务
    python3 todo_cli.py done 1             # 标记第 1 个任务为完成
    python3 todo_cli.py delete 1           # 删除第 1 个任务
    python3 todo_cli.py clear              # 清空所有任务
    python3 todo_cli.py help               # 显示帮助信息

数据文件默认保存在同一目录下的 todo_data.json 中。
"""

import json
import os
import sys
from datetime import datetime

# 数据文件路径
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo_data.json")


def load_tasks() -> list:
    """
    从 JSON 文件加载任务列表。

    返回:
        任务列表，每个任务是一个字典
    """
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("[警告] 数据文件损坏，已创建新的任务列表。")
        return []


def save_tasks(tasks: list) -> None:
    """
    将任务列表保存到 JSON 文件。

    参数:
        tasks: 任务列表
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(description: str) -> None:
    """
    添加新任务。

    参数:
        description: 任务描述
    """
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    # 重新编号
    for i, t in enumerate(tasks, 1):
        t["id"] = i
    save_tasks(tasks)
    print(f"[成功] 已添加任务：{description}")


def list_tasks() -> None:
    """列出所有任务。"""
    tasks = load_tasks()
    if not tasks:
        print("当前没有任务，使用 'add' 命令添加一个吧！")
        return

    print("\n" + "=" * 50)
    print("待办事项列表")
    print("=" * 50)
    for task in tasks:
        status = "[x]" if task["done"] else "[ ]"
        created = task.get("created_at", "未知时间")
        print(f"  {status} #{task['id']} {task['description']}")
        print(f"       创建时间: {created}")
    print("=" * 50)
    print(f"总计: {len(tasks)} 个任务")
    done_count = sum(1 for t in tasks if t["done"])
    print(f"已完成: {done_count} | 待完成: {len(tasks) - done_count}")
    print("=" * 50 + "\n")


def mark_done(task_id: int) -> None:
    """
    标记任务为已完成。

    参数:
        task_id: 任务编号
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"[成功] 任务 #{task_id} 已标记为完成：{task['description']}")
            return
    print(f"[错误] 找不到编号为 {task_id} 的任务。")


def delete_task(task_id: int) -> None:
    """
    删除指定任务。

    参数:
        task_id: 任务编号
    """
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(i)
            # 重新编号
            for j, t in enumerate(tasks, 1):
                t["id"] = j
            save_tasks(tasks)
            print(f"[成功] 已删除任务 #{task_id}：{removed['description']}")
            return
    print(f"[错误] 找不到编号为 {task_id} 的任务。")


def clear_tasks() -> None:
    """清空所有任务。"""
    confirm = input("确定要清空所有任务吗？此操作不可恢复 (y/n): ")
    if confirm.lower() == "y":
        save_tasks([])
        print("[成功] 已清空所有任务。")
    else:
        print("操作已取消。")


def show_help() -> None:
    """显示帮助信息。"""
    help_text = """
========================================
          Todo CLI 使用说明
========================================

命令格式：
    python3 todo_cli.py <命令> [参数]

可用命令：
    add <描述>        添加新任务
    list              列出所有任务
    done <编号>       标记任务为已完成
    delete <编号>     删除指定任务
    clear             清空所有任务
    help              显示此帮助信息

示例：
    python3 todo_cli.py add "学习 Python"
    python3 todo_cli.py list
    python3 todo_cli.py done 1
    python3 todo_cli.py delete 2

数据存储：
    任务数据保存在 todo_data.json 文件中。
========================================
"""
    print(help_text)


def main():
    """主函数：解析命令行参数并执行对应操作。"""
    args = sys.argv[1:]

    if not args or args[0] in ("help", "-h", "--help"):
        show_help()
        return

    command = args[0].lower()

    if command == "add":
        if len(args) < 2:
            print("[错误] 请提供任务描述。")
            print("用法: python3 todo_cli.py add <描述>")
            return
        description = " ".join(args[1:])
        add_task(description)

    elif command == "list":
        list_tasks()

    elif command == "done":
        if len(args) < 2:
            print("[错误] 请提供任务编号。")
            print("用法: python3 todo_cli.py done <编号>")
            return
        try:
            task_id = int(args[1])
            mark_done(task_id)
        except ValueError:
            print("[错误] 任务编号必须是整数。")

    elif command == "delete":
        if len(args) < 2:
            print("[错误] 请提供任务编号。")
            print("用法: python3 todo_cli.py delete <编号>")
            return
        try:
            task_id = int(args[1])
            delete_task(task_id)
        except ValueError:
            print("[错误] 任务编号必须是整数。")

    elif command == "clear":
        clear_tasks()

    else:
        print(f"[错误] 未知命令: {command}")
        print("使用 'help' 命令查看可用命令列表。")


if __name__ == "__main__":
    main()
