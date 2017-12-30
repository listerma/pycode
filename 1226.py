# -*- coding: utf-8 -*-
# @Date    : 2017-12-26 19:57:29
# @Author  : brkstone
import json
import re


class addressbook(object):
    """通讯录保存模式
    win10下有gbk utf8问题，还没完全解决
        {
            "1": {
                "姓名": "Envy",
                "手机": "123456789",
                "邮箱": ""
            },
            "2": {
                "姓名": "HP",
                "手机": "123456789",
                "邮箱": "jlj@hool.com"
            }
        }
    """

    def __init__(self):
        self.path = 'C:\\Users\\D\\Desktop\\address_list.json'  # 联系人文件存放路径
        self.indent_num = 4
        self.dictdata = {"姓名": "", "手机": "", "邮箱": ""}

    def savein(self):
        name = self.input_name()
        rddata = self.opf()
        # print('this is rddata:', rddata)
        while [rd_content for rd_content in rddata.values() if rd_content["姓名"] == name]:
            print('哎...撞名啦，谁丑谁尴尬@-@\n')
            name = self.input_name()
        else:
            self.dictdata["姓名"] = name
        # print('>>>>>>>>>>>', self.dictdata["姓名"])
        self.dictdata["手机"] = self.input_phone()
        # print('++++++++++++', self.dictdata["手机"])
        self.dictdata["邮箱"] = self.input_mail()
        # print('++++++++++++', self.dictdata["邮箱"])
        # 通讯录ID
        addressbook_ID = len(rddata) + 1
        # print('addressbook_ID:', addressbook_ID)
        rddata[str(addressbook_ID)] = self.dictdata
        # print('this is rddata after', rddata)
        self.wrf(rddata)
        print('联系人保存成功。')

    # 以关键字查找符合联系人
    def find_key(self):
        rddata = self.opf()
        inkey = input('查询关键字:')
        for key in rddata.keys():
            if str(rddata[key]).find(inkey) != -1:
                print('{} {} {} {}'.format(key, rddata[key]["姓名"], rddata[key]["手机"], rddata[key]["邮箱"]))
    # 显示所有联系人

    def showall(self):
        rddata = self.opf()
        for i in rddata:
            print('{} {} {} {}'.format(i, rddata[i]["姓名"], rddata[i]["手机"], rddata[i]["邮箱"]))
    # 删除对应ID的联系人

    def del_id(self):
        rddata = self.opf()
        inID = input('联系人ID:')
        if int(inID) > 0 and rddata.get(inID):
            flag = input('确认删除此联系人？(y/[n])')
            if flag == '' or flag == 'y':
                wrdata = {}  # 联系人重新排序
                try:
                    rddata.pop(inID)
                    for i in rddata:
                        toint = int(i)
                        if toint < int(inID):
                            wrdata[i] = rddata[i]
                        elif toint > int(inID):
                            wrdata[str(toint - 1)] = rddata[i]
                    self.wrf(wrdata)
                    print('删除联系人成功。')
                except:
                    print('不存在此ID联系人！')
            else:
                print('已经取消删除。')

        else:
            print('联系人ID不正确!')


# 以rb打开文件,返回数据
# 空文件中有个{}才能正确打开？？？

    def opf(self):
        with open(self.path, 'r', encoding='gbk') as f:
            rddata = json.load(f)
            # print(type(rddata))
        return rddata
# 以w打开文件，存入数据

    def wrf(self, data):
        with open(self.path, 'w', encoding='gbk') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
# 合法输入姓名，手机，邮箱

    def input_name(self):
        name = input('姓名:')
        while re.search('\w{1,15}', name) == None:
            # 姓名匹配字母下划线检查
            name = input('请重新输入姓名，只允许字符下划线:')
        # print(name)
        return name

    def input_phone(self):
        phonenum = input('手机:')
        while re.search('^1\d{10,}', phonenum) == None:  # 简单匹配以1开头的11位手机号码
            phonenum = input('>暂时不支持地球外运营商<\n请重新输入手机号码:')
        return phonenum

    def input_mail(self):
        mail_add = input('例如:example@xxx.xxx\n邮箱:')
        while mail_add == "":
            return mail_add
        else:
            while re.search('(\w+(.)?\w+)@(\w+(.)?\w+)', mail_add) == None:
                mail_add = input('请重新输入邮箱')
        return mail_add

# 请选择：1.录入 2.查找 3.全部显示 4.删除 (回车退出)   限制从1-2-3-4 Enter 中输入


def choose():
    try:
        tempin = eval(input('请选择：1.录入 2.查找 3.全部显示 4.删除 (回车退出)\n'))
        while re.search('[1234]', str(tempin)) == None:
            tempin = eval(input('请从1/2/3/4中选择(回车退出):'))
    except:
        tempin = ''
    return tempin

action = addressbook()
chs = choose()
while chs != '':
    if chs == 1:
        action.savein()
    elif chs == 2:
        action.find_key()
    elif chs == 3:
        action.showall()
    elif chs == 4:
        action.del_id()
    chs = choose()
else:
    print('欢迎您的使用！')
