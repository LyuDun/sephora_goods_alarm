# sephora_goods_alarm监控丝芙兰网站是否补货

## 本程序仅适用于丝芙兰美网， 其他地区不适用

## 打开丝芙兰网址(美网)需要代理，本程序不提供代理 ！

已完成的功能：
- 自动监控此商品是否上新。
- 提醒方式: 电脑播放声音
- 图形化界面
- 提醒方式：邮箱提醒
- 打包为exe执行文件，并发布版本

待完成的功能：
- qq提醒
- 去除运行时弹出的控制台窗口
- 优化提醒邮件不显示主题，容易被当作垃圾邮件
- 优化软件UI，增加显示运行状态的窗口



使用方法
1. 下载chromedriver：  [http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html)，将解压后的chromedriver.exe文件放到，chrome浏览器的安装位置。
2. 将chrome浏览器的安装位置加到PATH，
3. 下载本软件，[链接](https://github.com/LvDunn/sephora_goods_alarm/releases/tag/%E4%B8%9D%E8%8A%99%E5%85%B0%E6%96%B0%E5%93%81%E7%9B%91%E6%8E%A7v0.1)
4. 邮件提醒功能：商品到货后，会向你输入的的邮箱发送一条邮件。想要开启本功能，必须开启QQ邮箱的SMTP功能，开启方法可以[点击链接参考](https://jingyan.baidu.com/article/b0b63dbf1b2ef54a49307054.html), 获取到授权码后，将你的QQ邮箱号、授权码，填到软件的email、password位置。

遇到其他问题可以提issues, 或者发邮件(cqcqhelloworld@gmail.com)
