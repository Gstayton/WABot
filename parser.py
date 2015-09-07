from inspect import getmembers, isfunction
from helpers import Chat
from enum import Enum
import utilities

class Payload:
    def __init__(self, status, payloadType, response):
        self.__dict__.update({
            'Status': status,
            'Type': payloadType,
            'Response': response
        })

class PayloadType(Enum):
    CHAT_MESSAGE = 'chatmsg'
    NONE         = 'none'

class Commands():
    @staticmethod
    def ping(cmd, args):
        return Payload(
                0,
                PayloadType.CHAT_MESSAGE,
                "pong {0}".format(args)
                )

    @staticmethod
    def ud_define(cmd, args):
        define = utilities.Urban.search(args, 300)
        return Payload(
                0,
                PayloadType.CHAT_MESSAGE,
                define
                )


class Chat():
    def __init__(self):
        self.cmdChar = "!"
        self.commands = {}

        func_list = [o for o in getmembers(Commands) if isfunction(o[1])]

        for func in func_list:
            self.commands[func[0]] = func[1]

    def parse(self, msg):
        if msg[0] != self.cmdChar:
            return Payload(
                    1,
                    PayloadType.NONE,
                    None
                    )
        if " " in msg:
            cmd = msg[1:msg.find(" ")]
            args = msg[msg.find(" ") + 1:]
        else:
            cmd = msg[1:]
            args = ""
        print("COMMAND : " + cmd)
        if cmd in self.commands:
            return self.commands[cmd](cmd, args)
        else:
            return Payload(
                    1,
                    PayloadType.NONE,
                    None
                    )

