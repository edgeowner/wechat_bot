# coding:utf-8

from wxpy import *

bot = Bot(cache_path=True)


class SendTool:

    @bot.register()
    def send_messages(self, groupname, msg):
        target_group = bot.groups().search(groupname)[0]
        target_group.send(msg)


send_tool = SendTool()
# if __name__ == '__main__':
#     msg = '12312321312'
#     sendTool = SendTool()
#     sendTool.send_messages(msg)
#     msg = bot.messages
#     embed()
