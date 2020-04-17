'''from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait'''
import time
import pygame
import re
import threading
import requests
pygame.mixer.init()

#button = browser.find_element_by_css_selector("button[data-comp='AddToBasketButton Button Box']") 
     
class new_product_alarm(object):
    def __init__(self):
        #chrome_options=Options()
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')
        #self.browser = webdriver.Chrome(chrome_options=chrome_options)
        #self.browser = webdriver.Chrome()
        self.file_dir =r'noise.mp3'
    
    def login(self, url):
        print('login+' + url)
        self.thread = threading.Thread(target=self.login_child(url))
        self.thread.setDaemon(True)
        self.thread.start()
        
    def login_child(self, url):
        pass
    
    def yes_or_no(self, url):
        # 例如url:https://www.sephora.com/product/matte-velvet-skin-blurring-powder-foundation-P443566?skuId=2210052
        # 获取商品的编号
        pattern = re.compile(r"(?<=P)\d+")
        product_no = pattern.search(url).group(0)
        # 获取商品具体型号的编号skuid, 如果获取不到：提取网页中的默认skuid
        try:
            pattern2 = re.compile(r"(?<=skuId=)\d+")
            m = pattern2.search(url)
            if m is not None:
                skuId = m.group(0)
            else:
                skuId_list = response.xpath('//div[@data-comp="SizeAndItemNumber Box "]/text()').extract()
                for skuId_str in skuId_list:
                    m  = re.search(r'\d{4,8}', skuId_str) 
                    if m is not None:
                        skuId = m.group(0)
                        break
        except Exception as e:
            print('skuId' + str(e))
        print('id是:'+ str(skuId)) 
        # 拼接查是否有库存的api，请求api地址，解析json获取商品库存状态
        # https://www.sephora.com/api/users/profiles/current/product/P453916?skipAddToRecentlyViewed=false&preferedSku=2310324
        api_url = 'https://www.sephora.com/api/users/profiles/current/product/P' + str(product_no)

        #print(api_url)
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Referer' : url,
            'Host' : 'www.sephora.com'
        }
        
        try:
            api_response = requests.get(api_url, headers=headers)
            if api_response.status_code == 200:
                api_json = api_response.json()
                if api_json['currentSku']['skuId'] == skuId:
                    if api_json['currentSku']['actionFlags']['isAddToBasket'] == True:
                        return True
                    else:
                        return False
                else:
                    for i in api_json['regularChildSkus']:
                        if i['skuId'] == skuId:
                            if i['actionFlags']['isAddToBasket'] == True:
                                return True
                            else:
                                return False
        except Exception as e:
            print('error-----' + str(e))

    def music_notice(self):
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

    
    
        

'''if __name__ == '__main__':
    
    alarm = new_product_alarm()
    alarm.yes_or_no('https://www.sephora.com/product/ultra-repair-barriair-cream-P437995?icid2=homepage_bi_rewards_us_d_carousel_091019:p124402:product')
    time.sleep(10)'''