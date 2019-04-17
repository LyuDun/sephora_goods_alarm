from selenium import webdriver
import time
import pygame

Login_url = 'https://www.sephora.com/'
file_dir =r'noise.mp3'

def Login(buy_url):
    browser = webdriver.Chrome()
    browser.get(Login_url)
    try:
        #browser.find_element_by_id('signin_username').send_keys(user)
        #time.sleep(3)
        #browser.find_element_by_id('signin_password').send_keys(passwd)
        #time.sleep(3)
        #browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[1]/div/div/div[2]/form/div[3]/div/div[2]/button').click()
        #time.sleep(20)
        Gotobuy(browser, buy_url)

    except:
        pass
        #print('登陆失败')

def Gotobuy(browser,buy_url):
    browser.get(buy_url)
    while True:
        try:
            button = browser.find_element_by_css_selector("button[data-comp='AddToBasketButton Button Box']")
            print('########现在有货########')
            pygame.mixer.init()
            track = pygame.mixer.music.load(file_dir)
            pygame.mixer.music.play()

        except:
            print('现在无货，20秒后程序再次监控')
        finally:
            time.sleep(50)
            pygame.mixer.music.stop()

if __name__ == '__main__':
    print('此程序只适用于丝芙兰\n根据提示输入信息\n第一步：打开翻墙软件\n')
    #user = input('在下方输入登陆账户：\n')
    #passwd = input('在下方输入密码：\n')
    #buy_url ='https://www.sephora.com/product/protect-play-set-active-sunscreen-set-P443551?icid2=similar%20products:p443551:product'
    #buy_url = 'https://www.sephora.com/product/defend-daily-everyday-sunscreen-set-P443348'
    buy_url = input('第二步：把你要监控的商品的网址粘贴到下方,然后按回车\n')
    Login(buy_url)
