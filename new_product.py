from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pygame
import re
import threading
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

#button = browser.find_element_by_css_selector("button[data-comp='AddToBasketButton Button Box']") 
     
class new_product_alarm(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.file_dir =r'noise.mp3'
        pygame.mixer.init()
    
    def login(self, url):
        print('login+' + url)
        self.thread = threading.Thread(target=self.login_child(url))
        self.thread.setDaemon(True)
        self.thread.start()
        
    def login_child(self, url):
        pass
    

    def yes_or_no(self, url, default_time = 10):
        self.browser.get(url)
        time.sleep(5)
        while True:
            try:
                button = self.browser.find_elements_by_css_selector("[class='css-squbya ']")
                if len(button) == 0:
                    return False
                elif len(button) == 1:
                    return True
                else:
                    print ("找到元素个数：",len(button))
            except:
                pass
            finally:
                print ("找到元素个数：",len(button))
                time.sleep(default_time)
                self.browser.refresh()

    def music_notice(self, default_time = 10):
        pygame.mixer.music.load(self.file_dir)
        pygame.mixer.music.play()
        time.sleep(default_time)
        pygame.pygame.mixer.music.stop()

    def email_notice(self,url, email_list, email_info):
        for email in email_list:
            try:
                msg=MIMEText('你的丝芙兰商品已到货:网址'+ url,'plain','utf-8')
                msg['From']=formataddr(["商品监控", email_info['my_sender'] ])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                msg['To']=formataddr(["收件人", email ])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                msg['Subject']="邮件主题-提醒到货"                # 邮件的主题，也可以说是标题
                server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
                server.login(email_info['my_sender'], email_info['my_pass'] )  # 括号中对应的是发件人邮箱账号、邮箱密码
                server.sendmail(email_info['my_sender'],[email,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                server.quit()# 关闭连接
            except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
                pass

    def qq_notice(self):
        pass

    
    
        

if __name__ == '__main__':
    
    alarm = new_product_alarm()
    alarm.yes_or_no('https://www.sephora.com/product/ultra-repair-barriair-cream-P437995?icid2=homepage_bi_rewards_us_d_carousel_091019:p124402:product')
    time.sleep(10)