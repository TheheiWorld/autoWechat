#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/4/30 下午4:58

class FontColor():
    """
    调用方式：颜色/背景色/+下划线标志 + 需要加颜色的文字 + 结束标志
    """
    # 颜色码
    white = "\033[30;"  # default
    red = "\033[31;"
    green = "\033[32;"
    brown = "\033[33;"
    Pink = "\033[34;"
    Violet = "\033[35;"
    blue = "\033[36;"
    black = "\033[37;"

    # 背景色
    white_background = "\033[40;"  # default
    red_background = "\033[41;"
    green_background = "\033[42;"
    brown_background = "\033[43;"
    Pink_background = "\033[44;"
    Violet_background = "\033[45;"
    blue_background = "\033[46;"
    black_background = "\033[47;"

    # 下划线标志
    default = "0m"
    underline = "4m"

    # 结束标志位
    end = "\033[0m"
