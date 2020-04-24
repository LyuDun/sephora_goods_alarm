import tkinter
from tkinter import ttk
import tkinter.scrolledtext as tst
import json
import re
import time
from new_product import new_product_alarm as Alarm
import threading
import queue
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from contextlib import contextmanager
notice_list = []
q = queue.Queue()


class App(object):
    def __init__(self):
        self.js = jsonManage()
        self.root = tkinter.Tk()
        self.root.size = '440*440'
        self.root.title('新品监控')
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.tabControl = tkinter.ttk.Notebook(self.root)

        self.tab2 = ttk.Frame(self.tabControl)
        self.tab2.columnconfigure(0, weight=1)
        self.tab2.rowconfigure(0, weight=1)
        self.tabControl.add(self.tab2, text='主页面')
        self.tabControl.pack()
        # 输入网址
        self.url = tkinter.Text(self.tab2, width='50', height='2')
        self.url.pack()
        # 网址按钮
        self.button_go = tkinter.Button(self.tab2, text='GO!', command=self.go)
        self.button_go.pack()
        # 邮箱地址和密码
        self.show1 = tkinter.StringVar()
        self.sender_email = tkinter.Entry(self.tab2, textvariable=self.show1)
        self.show1.set('email')
        self.sender_email.pack()
        self.show2 = tkinter.StringVar()
        self.sender_pass = tkinter.Entry(self.tab2, textvariable=self.show2)
        self.show2.set('password')
        self.sender_pass.pack()
        # 通知方式列表显示
        self.b_mighty = tkinter.ttk.tkinter.LabelFrame(self.tab2)
        self.b_mighty.pack(fill=tkinter.BOTH, expand=1)
        self.b_listbox1 = tkinter.Listbox(self.b_mighty, width=33, height=10)
        self.b_listbox2 = tkinter.Listbox(self.b_mighty, width=33, height=10)
        self.b_listbox1.pack(padx=5, side=tkinter.LEFT,  anchor=tkinter.NW)
        self.b_listbox2.pack(padx=5, side=tkinter.RIGHT,  anchor=tkinter.NW)
        # qq输入
        self.b_lable1 = tkinter.Label(self.tab2, text="QQ")
        self.b_lable1.pack(padx=0, pady=5, side=tkinter.LEFT)
        self.b_qq_input = tst.ScrolledText(self.tab2, width=22, height=2)
        self.b_qq_input.pack(padx=0, pady=5, side=tkinter.LEFT)
        # 邮箱输入
        self.b_lable2 = tkinter.Label(self.tab2, text="邮箱")
        self.b_lable2.pack(padx=0, pady=0, side=tkinter.LEFT)
        self.b_email_input = tst.ScrolledText(self.tab2, width=22, height=2)
        self.b_email_input.pack(
            padx=0, pady=0, side=tkinter.LEFT, anchor=tkinter.S)
        # qq 邮件增加删除按钮
        self.button_add_email = tkinter.Button(
            self.tab2, text='增加', command=self.AddKeyword)
        self.button_add_email.pack(
            padx=0, pady=0, side=tkinter.BOTTOM, anchor=tkinter.NW)
        self.button_delete_email = tkinter.Button(
            self.tab2, text='删除', command=self.DeleteKeyword)
        self.button_delete_email.pack(
            padx=0, pady=0, side=tkinter.LEFT, anchor=tkinter.S)

    def mainloop(self):
        self.root.mainloop()

    def AddKeyword(self):
        global notice_list
        qq = None
        email = None
        qq = self.b_qq_input.get(1.0, tkinter.END)
        email = self.b_email_input.get(1.0, tkinter.END)

        if(qq.isspace() is not True):
            try:
                notice_list.append('qq' + '|' + str(qq))
                self.js.writejson('notice.json', notice_list)
            finally:
                self.b_qq_input.delete(1.0, tkinter.END)
        if(email.isspace() is not True):
            try:
                notice_list.append('email' + '|' + str(email))
                self.js.writejson('notice.json', notice_list)
            finally:
                self.b_email_input.delete(1.0, tkinter.END)
        self.ShowKeyWord()

    def ShowKeyWord(self):
        global notice_list
        try:
            notice_list = self.js.readjson('notice.json')
            notice_list_len = len(notice_list)
            self.b_listbox1.delete(0, 'end')
            self.b_listbox2.delete(0, 'end')

            if(notice_list_len != 0):
                for notice in notice_list:
                    if (str(notice).startswith('qq')):
                        self.b_listbox1.insert(tkinter.END, 'qq')
                        self.b_listbox2.insert(
                            tkinter.END, str(notice).split('|')[1])
                    elif (str(notice).startswith('email')):
                        self.b_listbox1.insert(tkinter.END, 'email')
                        self.b_listbox2.insert(
                            tkinter.END, str(notice).split('|')[1])
        except:
            pass

    def DeleteKeyword(self):
        global notice_list
        for i in range(len(notice_list)):
            if(self.b_listbox1.selection_includes(i) is True):
                notice_list.pop(i)
        self.js.writejson('notice.json', notice_list)
        self.ShowKeyWord()

    def go(self):
        url = self.url.get('1.0', tkinter.END)
        q.put(url)
        self.thread = threading.Thread(target=self.go_child)
        self.thread.setDaemon(True)
        self.thread.start()
        self.url.delete(1.0, tkinter.END)

    def go_child(self):
        global notice_list
        while True:
            url = q.get()
            alarm = Alarm()
            if(alarm.yes_or_no(url) is True):
                try:
                    alarm.music_notice()
                    for notice in notice_list:
                        if (str(notice).startswith('email')):
                            #print(str(notice).split('|')[1])
                            self.email_notice(url, str(notice).split('|')[1])
                finally:
                    break
            else:
                time.sleep(20)

    def email_notice(self, url, email):
        sender = self.sender_email.get()
        sender_pass = self.sender_pass.get()
        #print('sender:' + sender + 'email_pass:' + sender_pass + 'email' + email)
        if (sender == 'email') or (sender_pass == 'email_pass'):
            print('sender2:' + sender + 'email_pass:' + sender_pass + 'email' + email)
            return
        else:
            with logined(sender, sender_pass) as smtp_serv:
                msg = MIMEText('你的丝芙兰商品已到货,网址:' + url, 'plain', 'utf-8')
                # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                msg['From'] = formataddr(["商品监控", sender])
                # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                msg['To'] = formataddr(["收件人", email])
                # 邮件的主题，也可以说是标题
                msg['Subject'] = "邮件主题-提醒到货"
                # 发件人邮箱中的SMTP服务器，端口是465
                server = smtplib.SMTP_SSL("smtp.qq.com", 465)
                # 括号中对应的是发件人邮箱账号、邮箱密码
                server.login(sender, sender_pass)
                # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                try:
                    smtp_serv.send_message(msg)
                finally:
                    pass
    @contextmanager
    def logined(sender, password, smtp_host='smtp.qq.com', smtp_port=587):
        smtp_serv = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
        try: # make smtp server and login
            smtp_serv.ehlo_or_helo_if_needed()
            smtp_serv.starttls()
            smtp_serv.ehlo()
            smtp_serv.login(sender, password)
            yield smtp_serv
        finally:
            pass


class jsonManage(object):
    def __init__(self):
        pass

    def writejson(self, filename, data):
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    def readjson(self, filename):
        with open(filename, 'r', encoding="utf-8") as f:
            notice_list = json.load(f)
        return notice_list


if __name__ == "__main__":
    s = App()
    s.ShowKeyWord()
    s.mainloop()
