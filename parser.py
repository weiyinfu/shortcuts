from fu import xml2json
import os
import json

import pandas as pd
import re


def rep(s: str):
    """
    s是一个快捷键字符串，把它进行规范化
    """
    ma = [
        ("Ctrl", "Ctrl"), ('control', 'Ctrl'), ('Page_down', "PageDown"), ("CLOSE_BRACKET", "]"), ("open_bracket", '['),
        ('close_bracket', ']'),
        ("button4", "鼠标后退"),
        ("button5", '鼠标前进'),
        ('button1', '鼠标左键'), ("button2", '鼠标右键'),
        ('SPACE', " 空格"), ("back_space", "退格"), ("page_up", "上翻"), ('meta', 'Win'), ("right", ' 右'), ('up', ' 上'), ('left', '左'), ('down', ' 下'),
    ]

    def upfirst(match):
        s = match.group()
        s = s.replace('_', "")
        return s[0].upper() + s[1:].lower()

    def replace_word(s):
        for o, n in ma:
            # ignorecase不管用
            s = re.sub(f"([^\w]|^){o[0].upper() + o[1:]}", ' ' + n, s, re.IGNORECASE)
            s = re.sub(f"([^\w]|^){o[0].lower() + o[1:]}", ' ' + n, s, re.IGNORECASE)
        return s

    s = re.sub("\w+", upfirst, s)
    s = replace_word(s)
    return s


def shortcut2string(it):
    # 把shortcut转成string
    if not it:
        return ""
    sep = ","
    or_sep = " | "

    if type(it) == list:
        s = or_sep.join(shortcut2string(i) for i in it)
        return rep(s)
    elif type(it) == str:
        assert not it.strip()
        return ""
    else:
        s = sep.join(it.values())
        return rep(s)


def command2string(command):
    # 把命令转成string
    s = ''
    last_is_big = True
    for i in command:
        if i == '.':
            s += '>'
            last_is_big = False
        elif 'A' <= i <= 'Z':
            if not last_is_big:
                s += ' '
            s += i
            last_is_big = True
        else:
            s += i
            last_is_big = False
    return s


def parse_file(filepath):
    a = {}
    s = xml2json.xml2json(open(filepath).read(), pretty=True)
    s = json.loads(s)
    s = s['keymap']['action']
    for i in s:
        k = command2string(i['@id'])
        keyboard_shortcut = shortcut2string(i.get('keyboard-shortcut'))
        mouse_shortcut = shortcut2string(i.get("mouse-shortcut"))
        shortcut = [keyboard_shortcut, mouse_shortcut]
        shortcut = [i for i in shortcut if i]
        a[k] = " | ".join(shortcut)
        if not a[k]:
            del a[k]
    return a


def get_data():
    a = []
    columns = []
    for file in os.listdir("ideaKeymap"):
        if not file.endswith(".xml"): continue
        filepath = os.path.join("ideaKeymap", file)
        dic = parse_file(filepath)
        filename = os.path.basename(file)
        filename = os.path.splitext(filename)[0]
        columns.append(filename)
        a.append(dic)
    return a, columns
