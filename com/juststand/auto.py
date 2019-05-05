#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/4/30 上午10:47

import itchat


CONTENT = ['开始预定', '开始预约', '开始约', '开始预', '开始订']
CAN_SEND = []

MESSAGE = ''

print('*********** 关键字 ***********')
print('默认回复关键字' + CONTENT.__str__())


def inputMessage():
    global CONTENT
    global MESSAGE
    # 关键字
    print("notes: 请逐次输入今日预定关键字，输入 e 代表结束；若没有输入任何关键字，则采取默认关键字")
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

    # 自动回复人群
    print('')
    print('')
    print("notes: 请逐次输入需要自动回复的人，输入 e 代表结束；若没有输入，则无法自动回复")
    while True:
        nickname = str(input('请输入微信昵称:'))
        if nickname == 'e':
            break
        if nickname:
            CAN_SEND.append(nickname)

inputMessage()

@itchat.msg_register(itchat.content.TEXT)
def person_reply(msg):
    username = msg.User.NickName
    message = msg.Content
    if username not in CAN_SEND:
        return
    if message in CONTENT:
        return MESSAGE
    return


@itchat.msg_register(itchat.content.INCOME_MSG, isGroupChat=True)
def group_reply(msg):
    username = msg.User.NickName
    message = msg.Content
    if username not in CAN_SEND:
        return
    if message in CONTENT:
        return MESSAGE
    return


itchat.auto_login(hotReload=True)
itchat.run()
