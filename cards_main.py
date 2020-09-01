# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：cards_main
   Date：2020/8/31
   Author：Jason
   Description：显示名片管理系统的主界面以及功能选项。
                【1】新建名片
                【2】显示名片
                【3】查询名片->【1】删除名片 /【2】修改名片 /【0】返回主页
                【0】退出系统
-------------------------------------------------
   Change Activity:2020/8/31             
-------------------------------------------------
"""
import cards_tools

while True:
    # 0.显示功能菜单。
    cards_tools.show_menu()

    # 1.提示用户输入需要执行的任务数字。
    action_str = input("请输入需要执行的数字：")

    # 2.判断用户需要执行的功能
    function_list = ["0", "1", "2", "3"]
    if action_str in function_list:
        if action_str == "1":  # 新建名片
            cards_tools.new_card()

        elif action_str == "2":  # 显示所有名片信息
            cards_tools.show_cards()

        elif action_str == "3":  # 查询名片
            cards_tools.search_card()

        elif action_str == "0":  # 退出系统
            break
    else:
        print("输入有误！请检查输入内容。")
