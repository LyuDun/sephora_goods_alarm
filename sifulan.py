from selenium import webdriver
import time
import itchat
import pygame
pygame.mixer.init() 

file_dir =r'noise.mp3'
send_userid = '王娓'
#send_userid = '我们一起去捉水母吧'

def Login(buy_url,call_flag):
    if (call_flag == '2'):
        print('第四步：扫描二维码登陆微信\n')
        try:
            #itchat.auto_login()
            itchat.auto_login(enableCmdQR=1)
            time.sleep(2)
        except:
            pass
    browser = webdriver.Chrome()
    browser.get(buy_url)
    browser.maximize_window()

    while True:
        try:
            button = browser.find_element_by_css_selector("button[data-comp='AddToBasketButton Button Box']") 
            print('########现在有货########')
            if (call_flag == '1'):
                print('播放声音')
                track = pygame.mixer.music.load(file_dir)
                pygame.mixer.music.play()
                time.sleep(30)
                pygame.mixer.music.stop()
            if (call_flag == '2'):
                itcaht_user_name = itchat.search_friends(name=send_userid)[0]['UserName']
                itchat.send_msg(msg="你监控的丝芙兰商品有货", toUserName=itcaht_user_name)

        except:
            print('现在无货，30秒后程序再次监控')
        finally:
            browser.refresh()
            time.sleep(30)
            

    
if __name__ == '__main__':
    print('此程序只适用于丝芙兰\n根据提示输入信息\n\n')
    print('第一步：打开翻墙软件\n')
    buy_url = input('第二步：把你要监控的商品的网址粘贴到下方,然后按回车\n')
    call_flag = input('第三步：选择提醒方式,请输入1或2（1：闹钟提醒；2：微信消息提醒）\n')
    Login(buy_url,call_flag)
