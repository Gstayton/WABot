from inspect import getmembers, isfunction, getdoc
from enum import Enum
import random

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
    def roll(cmd, args):
        "Roll the dice!\n !roll [number] d [sides]"
        roll = args.replace(" ", "")
        num, sides = roll.split('d')

        num = int(num)
        sides = int(sides)

        if (sides >= 1) and (sides <= 9999) and (num >= 1) and (num <= 9999):
            roll = sum(random.randrange(sides)+1 for die in range(num))

        return Payload(
                0,
                PayloadType.CHAT_MESSAGE,
                str(roll)
                )

    @staticmethod
    def about(cmd, args):
        "General information about this bot"
        message = "A bot for WhatsApp written in Python by Nathan Thomas (AKA Kosan Nicholas)\n"
        message += "Source available at http://github.com/Gstayton/WABot\n"
        message += "Current version: 0.0.2"

        return Payload(
                0,
                PayloadType.CHAT_MESSAGE,
                message
                )

    @staticmethod
    def ping(cmd, args):
        "Check alive status of bot"
        return Payload(
                0,
                PayloadType.CHAT_MESSAGE,
                "pong {0}".format(args)
                )

    @staticmethod
    def ud_define(cmd, args):
        """
        !ud_define [search term]
        Returns the first result from urbandictionary.com for [search term], truncated to 300 characters or less
        """
        define = utilities.Urban.search(args, 300)
        return Payload(
                0,
                PayloadType.CHAT_MESSAGE,
                define
                )

    @staticmethod
    def help(cmd, args):
        "Display available commands"
        func_list = [o for o in getmembers(Commands) if isfunction(o[1])]
        helpText = ""
        if args:
            if " " in args:
                helpText = "Invalid search"
            else:
                for f in func_list:
                    if args.lower() == f[0] and getdoc(f[1]):
                        helpText = "Usage for {0}{1}: \n".format(Chat.cmdChar, args)
                        helpText += getdoc(f[1])
                if not helpText:
                    helpText = "No help available for '{0}'".format(args)
        else:
            helpText = "Currently implemented commands: \n"
            for f in func_list:
                helpText += Chat.cmdChar + f[0] + ", "

            helpText += "\nFor more info, try !help [command]"

        return Payload(
                0,
                PayloadType.CHAT_MESSAGE,
                helpText
                )

class Chat():
    cmdChar = "!"
    def __init__(self):
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

