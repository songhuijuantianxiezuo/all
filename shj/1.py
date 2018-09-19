import requests
import itchat
import itchat
from itchat.content import *
import re
#
# # @itchat.msg_register([TEXT])
# # def replay(msg):
# #     itchat.send("hahahhahahahhahaha",msg["FromUserName"])
# # @itchat.msg_register([PICTURE])
# # def pic_replay(msg):
# #     itchat.send("照片",msg["FromUserName"])
# # itchat.auto_login()
# # itchat.run()
#
# @itchat.msg_register([TEXT])
# def replay(msg):
#    a=re.compile('.+?(学习).+？',re.S)
#    # b=re.findall(a,msg)
#    b=a.seach(msg)
#    if b == []:
#       itchat.send("学习吗？可能吧",msg["FromUserName"])
#    else:
#       itchat.send("你四不四撒",msg["FromUserName"])
# @itchat.msg_register([PICTURE])
# def pic_replay(msg):
#    itchat.send("照片",msg["FromUserName"])
# itchat.auto_login()
# itchat.run()
@itchat.msg_register([TEXT])
def reply(msg):
    pattern = re.search('五一',msg['Text']).span()  #用saerch进行匹配，找到满足的条件就直接中断寻找
    if pattern:
        itchat.send(('同乐同乐，一起好好享受五一吧'),msg['FromUserName'])
itchat.auto_login()
itchat.run()