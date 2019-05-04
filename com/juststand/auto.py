#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/4/30 上午10:47

import itchat


class FontColor:
    """
    调用方式：颜色/背景色/+下划线标志 + 需要加颜色的文字 + 结束标志
    """
    # 颜色码
    white = "\033[30;"
    red = "\033[31;"
    green = "\033[32;"
    brown = "\033[33;"
    Pink = "\033[34;"
    Violet = "\033[35;"
    blue = "\033[36;"
    black = "\033[37;"

    # 背景色
    white_background = "\033[40;"
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


CONTENT = ['开始预定', '开始预约', '开始约', '开始预', '开始订']
CAN_SEND = ('✨Pobaby',)

MESSAGE = ''

print(FontColor.green + FontColor.default + '*********** 关键字 ***********' + FontColor.end)
print(FontColor.red + FontColor.default + '默认回复关键字' + CONTENT.__str__() + FontColor.end)


def inputMessage():
    global CONTENT
    global MESSAGE
    # 关键字
    print(FontColor.green + FontColor.default + "notes: 请逐次输入今日预定关键字，输入 e 代表结束；若没有输入任何关键字，则采取默认关键字" + FontColor.end)
    CONTENT_TEMP = []
    while True:
        keyword_booking = str(input('请输入关键字:'))
        if keyword_booking == 'e':
            break
        if keyword_booking:
            CONTENT_TEMP.append(keyword_booking)
    if CONTENT_TEMP.__len__() > 0:
        CONTENT = CONTENT_TEMP

    # 回复
    MESSAGE = str(input('请输入回复内容，按回车键确认：'))


inputMessage()


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    username = msg.User.NickName
    print(username)
    message = msg.Content
    if username not in CAN_SEND:
        return
    if message in CONTENT:
        return MESSAGE
    return


@itchat.msg_register(itchat.content.INCOME_MSG, isGroupChat=True)
def download_files(msg):
    username = msg.User.PYQuanPin
    message = msg.Content
    if username not in CAN_SEND:
        return
    if message in CONTENT:
        return MESSAGE
    return


def chatrooms():
    rooms = itchat.get_chatrooms()
    print(rooms.__str__())


itchat.auto_login()
chatrooms()
itchat.run()
