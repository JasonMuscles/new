# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：cards_tools
   Date：2020/8/31
   Author：Jason
   Description：实现main中用户选择的具体功能的相关函数。功能如下：
                【1】新建名片
                【2】显示名片
                【3】查询名片->【1】删除名片 /【2】修改名片 /【0】返回主页
                【0】退出系统
-------------------------------------------------
   Change Activity:2020/8/31             
-------------------------------------------------
"""
# 定义一个公共的名片列表。
card_list = []


def show_menu():
    print("*" * 50)
    print(" Business Card System V1.1")
    print("【1】新建名片")
    print("【2】显示名片")
    print("【3】查询名片")
    print("【0】退出系统")
    print("*" * 50)


# 新建名片函数
def new_card():
    name_str = input("你的姓名：")
    sex_str = input("你的性别：")
    phone_str = input("你的手机：")
    email_str = input("你的邮箱：")
    card_dict = {"name": name_str, "sex": sex_str, "phone": phone_str, "email": email_str}
    card_list.append(card_dict)


# 显示名片函数
def show_cards():
    # 1.如列表中无数据提示用户新增名片。
    if len(card_list) == 0:
        print("无数据，请先增加名片信息！")
        return

    # 2.如列表中有数据时显示全部数据--建立表头
    for name in ["姓名", "性别", "手机", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("-" * 50)

    # 3.如列表中有数据时显示全部数据--显示数据
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["sex"],
                                        card_dict["phone"],
                                        card_dict["email"]))
    print("-" * 50)


# 查询名片函数
def search_card():
    find_card = input("请输入需要查询姓名：")
    for card_dict in card_list:
        if find_card == card_dict["name"]:
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["sex"],
                                            card_dict["phone"],
                                            card_dict["email"]))
            print("-" * 50)
        else:
            print("未查询到【%s】的相关信息" % find_card)
        # TODO 提示查询出结果后的操作

        break


def deal_card(card_dict):
    action_str = input("选择需要执行的操作：\n【1】删除名片\n【2】修改名片\n【0】返回主页")
    if action_str == 1:
        card_list.remove(card_dict)




