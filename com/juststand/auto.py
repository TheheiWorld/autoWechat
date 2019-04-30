#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/4/30 上午10:47

import itchat

print('''
    关键字回复操作
    预定默认字，
''')

CONTENT = ['开始预定','开始预约','开始约', '开始预','开始订']
def inputMessage():
    keyword_booking = str(input('请输入今日预定关键字，按回车键确认，如不输入，直接回车，将采取默认关键字：'))


MESSAGE = str(input("请输入今日预定回复内容:"))

CAN_SEND = ['maitaoJavakaifaerzu']

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(MESSAGE)
    username = msg.User.PYQuanPin
    message = msg.Content
    if message in CONTENT:
        return MESSAGE
    return

@itchat.msg_register(itchat.content.INCOME_MSG, isGroupChat=True)
def download_files(msg):
    username = msg.User.PYQuanPin
    if username in CAN_SEND:
        return msg.text
    return


itchat.auto_login()
itchat.run()