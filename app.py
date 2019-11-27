import tkinter
from tkinter import ttk
import tkinter.scrolledtext as tst
import json
import re
from new_product import new_product_alarm as Alarm
import threading
import queue
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
        #输入网址
        self.url = tkinter.Text(self.tab2, width='50', height='2')
        self.url.pack()
        #网址按钮
        self.button_go = tkinter.Button(self.tab2, text='GO!', command = self.go)
        self.button_go.pack()
        #通知方式列表显示
        self.b_mighty = tkinter.ttk.tkinter.LabelFrame(self.tab2)
        self.b_mighty.pack(fill=tkinter.BOTH, expand=1)
        self.b_listbox1 = tkinter.Listbox(self.b_mighty, width=33, height=10)
        self.b_listbox2 = tkinter.Listbox(self.b_mighty, width=33, height=10)
        self.b_listbox1.pack(padx=5, side=tkinter.LEFT,  anchor=tkinter.NW)
        self.b_listbox2.pack(padx=5, side=tkinter.RIGHT,  anchor=tkinter.NW)
        #qq输入
        self.b_lable1 = tkinter.Label(self.tab2, text="QQ")
        self.b_lable1.pack(padx=0, pady=5, side=tkinter.LEFT)
        self.b_qq_input = tst.ScrolledText(self.tab2, width=22, height=2)
        self.b_qq_input.pack(padx=0, pady=5, side=tkinter.LEFT)
        #邮箱输入
        self.b_lable2 = tkinter.Label(self.tab2, text="邮箱")
        self.b_lable2.pack(padx=0, pady=0, side=tkinter.LEFT)
        self.b_email_input = tst.ScrolledText(self.tab2, width=22, height=2)
        self.b_email_input.pack(padx=0, pady=0, side=tkinter.LEFT, anchor=tkinter.S)
        #qq 邮件增加删除按钮
        self.button_add_email = tkinter.Button(
            self.tab2, text='增加', command=self.AddKeyword)
        self.button_add_email.pack(padx=0, pady=0, side=tkinter.BOTTOM, anchor=tkinter.NW)
        self.button_delete_email = tkinter.Button(
            self.tab2, text='删除', command=self.DeleteKeyword)
        self.button_delete_email.pack(padx=0, pady=0, side=tkinter.LEFT, anchor=tkinter.S)
        

    def mainloop(self):
        self.root.mainloop()

    def AddKeyword(self):
        global notice_list
        qq = None
        email = None
        qq = self.b_qq_input.get(1.0, tkinter.END)
        email = self.b_email_input.get(1.0, tkinter.END)

        if(qq.isspace() != True):
            try:
                notice_list.append('qq'+ '|' + str(qq))
                self.js.writejson('notice.json',notice_list)
            except:
                pass
            finally:
                self.b_qq_input.delete(1.0, tkinter.END)
        if(email.isspace() != True):
            try:
                notice_list.append('email' + '|' + str(email))
                self.js.writejson('notice.json',notice_list)
            except:
                pass
            finally:
                self.b_email_input.delete(1.0, tkinter.END)
        self.ShowKeyWord()

    def ShowKeyWord(self):
        global notice_list
        try:
            notice_list = self.js.readjson('notice.json')
            notice_list_len =  len(notice_list)
        except:
            notice_list_len = 0

        self.b_listbox1.delete(0,'end')
        self.b_listbox2.delete(0,'end')
        if(notice_list_len != 0):
            for notice in notice_list:
                if  ( str(notice).startswith('qq') ):
                    self.b_listbox1.insert(tkinter.END, 'qq')
                    self.b_listbox2.insert(tkinter.END, str(notice).split('|')[1])
                elif ( str(notice).startswith('email') ):
                    self.b_listbox1.insert(tkinter.END, 'email')
                    self.b_listbox2.insert(tkinter.END, str(notice).split('|')[1])
    
    def DeleteKeyword(self):
        global notice_list
        for i in range(len(notice_list)):
            if(self.b_listbox1.selection_includes(i) == True):
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
        try:
            url = q.get()
            alarm = Alarm()
            if(True == alarm.yes_or_no(url, 20)):
                alarm.music_notice()
                
        except:
            pass

class jsonManage(object):
    def __init__(self):
        pass

    def writejson(self, filename, data):
        with open(filename, 'w',encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False)

    def readjson(self, filename):
        with open(filename,'r',encoding="utf-8") as f:
            notice_list = json.load(f)
        return notice_list


if __name__ == "__main__":
    s = App()
    s.ShowKeyWord()
    s.mainloop()
    