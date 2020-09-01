# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：card_input
   Date：2020/9/1
   Author：Jason
   Description：用于改造input函数的默认功能的不足
-------------------------------------------------
   Change Activity:2020/9/1             
-------------------------------------------------
"""


def input_card_info(dict_value, tip_message):
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value

























