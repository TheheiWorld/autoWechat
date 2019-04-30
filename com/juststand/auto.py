#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/4/30 上午10:47

import itchat
from com.juststand.Color import FontColor

CONTENT = ['开始预定','开始预约','开始约', '开始预','开始订']
CAN_SEND = ['maitaoJavakaifaerzu']

MESSAGE = ''

print(FontColor.green + FontColor.default + '*********** 关键字 ***********' + FontColor.end)
print(FontColor.red + FontColor.default + '默认回复关键字' + CONTENT.__str__() + FontColor.end )

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

    ### 回复
    MESSAGE = str(input('请输入回复内容，按回车键确认：'))

inputMessage()

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    username = msg.User.PYQuanPin
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


itchat.auto_login()
itchat.run()