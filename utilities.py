import requests
import json

class Urban():
    @staticmethod
    def search(term, length):
        req = requests.get(
                "http://api.urbandictionary.com/v0/define", {'page': 1, 'term': term}
                )
        define = req.json()['list'][0]['definition'].replace('\r\n', ' ')
        short = define[:define.rfind(" ", 0, length)]
        return short + "\n" + req.json()['list'][0]['permalink']
