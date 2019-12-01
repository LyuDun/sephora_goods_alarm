from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import pygame
import re
import threading
pygame.mixer.init()

#button = browser.find_element_by_css_selector("button[data-comp='AddToBasketButton Button Box']") 
     
class new_product_alarm(object):
    def __init__(self):
        #chrome_options=Options()
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')
        #self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser = webdriver.Chrome()
        self.file_dir =r'noise.mp3'
    
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
        self.thread = threading.Thread(target=self.music_notice_child)
        self.thread.setDaemon(True)
        self.thread.start()

    def music_notice_child(self):
        pygame.mixer.music.load(self.file_dir)
        pygame.mixer.music.play()
        time.sleep(30)
        pygame.pygame.mixer.music.stop()

    

    def qq_notice(self):
        pass

    
    
        

if __name__ == '__main__':
    
    alarm = new_product_alarm()
    alarm.yes_or_no('https://www.sephora.com/product/ultra-repair-barriair-cream-P437995?icid2=homepage_bi_rewards_us_d_carousel_091019:p124402:product')
    time.sleep(10)