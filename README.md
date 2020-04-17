# sephora_goods_alarm监控丝芙兰网站是否补货

已完成的功能：
- 自动监控此商品是否上新。
- 提醒方式: 电脑播放声音
- 图形化界面
- 提醒方式：邮箱提醒
- 优化提醒邮件不显示主题，容易被当作垃圾邮件

待完成的功能：
- 优化软件UI，增加显示运行状态的窗口

## 必读：
1. **支持邮件提醒功能，但是想要开启本功能，必须开启QQ邮箱的SMTP功能，并将你的QQ邮箱号、授权码，填到软件的email、password位置。开启方法可以[点击链接参考](https://jingyan.baidu.com/article/b0b63dbf1b2ef54a49307054.html)。**
3. **暂不支持qq提醒功能，虽然有QQ号输入栏，但是目前不支持**
4. **本程序仅适用于丝芙兰美网， 其他地区不适用**
5. **打开丝芙兰网址(美网)需要代理，本程序不提供代理 ！**
6. **新版本不再需要chromedriver，和chrome浏览器，但是目前还未打包为exe release为旧版本，无法使用**

## 使用方法
1. git clone https://github.com/LvDunn/sephora_goods_alarm.git
2. cd sephora_goods_alarm
3. pip install -r requirements.txt
4. pip install tkinter
5. python app.py



遇到其他问题可以提issues, 或者发邮件(cqcqhelloworld@gmail.com)
