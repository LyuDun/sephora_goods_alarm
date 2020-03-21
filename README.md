# sephora_goods_alarm监控丝芙兰网站是否补货

已完成的功能：
- 自动监控此商品是否上新。
- 提醒方式: 电脑播放声音
- 图形化界面
- 提醒方式：邮箱提醒
- 打包为exe执行文件，并发布版本
- 去除运行时弹出的控制台窗口
- 优化提醒邮件不显示主题，容易被当作垃圾邮件

待完成的功能：
- qq提醒
- 优化软件UI，增加显示运行状态的窗口

## 必读：
1. **你的电脑必须有chrome浏览器，其他浏览器不支持**
2. **支持邮件提醒功能，但是想要开启本功能，必须开启QQ邮箱的SMTP功能，并将你的QQ邮箱号、授权码，填到软件的email、password位置。开启方法可以[点击链接参考](https://jingyan.baidu.com/article/b0b63dbf1b2ef54a49307054.html)。**
3. **暂不支持qq提醒功能，虽然有QQ号输入栏，但是目前不支持，后续可能会更新。**
4. **本程序仅适用于丝芙兰美网， 其他地区不适用**
5. **打开丝芙兰网址(美网)需要代理，本程序不提供代理 ！**

## 使用方法
1. 下载chromedriver：  [http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html)，如果访问不了，也可以访问淘宝搭建的国内镜像地址下载，[https://npm.taobao.org/mirrors/chromedriver/](https://npm.taobao.org/mirrors/chromedriver/)  根据自己浏览器的版本选择相应的Chromedriver
2. 将解压后的chromedriver.exe文件放到chrome浏览器的安装位置，安装位置可以在chrome浏览器的导航栏输入chrome://version/ 来查看。
3. 将chrome浏览器的安装位置加到PATH: 点击我的电脑->属性->高级系统设置->环境变量->系统环境修改path：双击path->右边按钮添加文本,然后在最后面添加浏览器的安装地址，例如：C:\Program Files (x86)\Google\Chrome\Application\
4. 下载本软件，[下载链接](https://github.com/LvDunn/sephora_goods_alarm/releases/tag/%E4%B8%9D%E8%8A%99%E5%85%B0%E6%96%B0%E5%93%81%E7%9B%91%E6%8E%A7v0.1),开始使用



遇到其他问题可以提issues, 或者发邮件(cqcqhelloworld@gmail.com)
