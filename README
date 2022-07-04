# README  v0.6.0

# 声明｜Statement

**该脚本仅供学习，请合理使用！！！切勿二次传播或用作商业用途！！！若出现任何纠纷，本人概不负责！！！**

# 准备｜Preparation

## 环境准备｜Environment Requirements

- **Python3**
- **Selenium Module**
- **Crontab(if you need automation)**
- **Chrome & Chrome Driver** 
备注：ChromeDriver的版本**必需要和Chrome一致**，并且由于Chrome默认开启了自动升级，所以在Chrome自动更新之后，请从[**此链接**](https://chromedriver.chromium.org)下载对应版本的ChromeDriver。

## 个人建议(仅参考)｜Personal Recommendation & Explanation

- **系统平台**：
    - **macOS：**个人建议在macOS上部署此项目用于自动化打卡。脚本中需要填写的「Information」板块中，「#」后备注的参考信息都是基于macOS平台给出的。
    - **Windows：**由于Windows的文件路径比较独特，本人并不清楚应如何填写相关的路径信息，如果你有此需求，你可以检索关键字「Windows+python+文件绝对路径」获取相关信息。理论上，涉及文件路径的内容仅在「Information」板块，如果你通过查阅资料或者有能力搞定路径的问题，在Windows平台上应该也是能使用此脚本自动打卡的。
    - **Linux：**Linux系统的文件路径设计基本与macOS相同，如果你选择将此脚本部署在Linux上，相信你也有能力解决文件路径填写的问题。不过值得注意的是，此脚本并未设计QQ登录时“风控”要求填写验证码的功能，如果你将其部署在Linux服务器上，有可能会遭遇由于“风控”要求填写验证码继而无法正常登录的情况。所以最妥善的做法是将其部署在自己常用的电脑上。
- **文件路径：**
    - 建议文件路径或文件名中不要包含任何的中文或空格和特殊符号，以避免不必要的错误。

# 如何使用｜How to Use

## 环境准备

根据环境要求，分别安装好「**Python3**」&「**Selenium Module**」&「**Chrome & Chrome Driver** 」。macOS和Linux自带「**Crontab**」不必安装，Windows上需要另外安装。

## 班级魔方上的准备工作

由于班级魔方后台的更新，原1.0版本的脚本已经无法正常使用。并且由于相关法律的更新，班级魔方已经不再支持通过手机号和密码的方式登录，请先通过微信小程序登录班级魔方，绑定登录的qq账号。

## 根据备注内容修改脚本中的Information板块

注意：不要删除脚本中information项目的「‘」「’」两个引号

## 每日自动化（基于Crontab）

1. 切换到英文输入法。
2. 在macOS上打开terminal.app，输入「crontab -e」后按下「enter」回车键。
3. 输入「i」。
4. 输入「0 * * * * DISPLAY=:0+空格+python3路径+空格+脚本所在的路径」，具体输入可参考下面此条命令。
「0 * * * * DISPLAY=:0 /usr/bin/python3 /Users/xxx/Documents/BJMF_Auto/BJMF_Auto_0.6.0.py」
5. 按下「esc」键后，输入「:wq」后按下「enter」回车键即可。

备注：
此命令的“翻译”是每天每隔一个小时执行一次python脚本，并且通过此crontab实现的每日自动打卡在新建Chrome进程之前会检查log文件中是否记录了今日的打卡数据，如果监测到已经打卡，那么就会直接退出，避免资源浪费。一切都是“后台静默”的方式，不会有任何的弹窗，你也不必担心在打卡过程中对电脑进行操作而中断了自动打卡。根据本人的体验，MacBook即使在锁屏时也可以实现自动打卡（盒盖了就不行了），所以基本上只要你一天在任意整点用会电脑都能顺利打上卡。
最后，如果你不再需要打卡了，可以通过「crontab -e」删除此条命令。

# 联系我｜Connect Me

**E-Mail: tshaveanidea@outlook.com**

**Personal Blog: [tssblog.club](http://tssblog.club)**

***Hope all of you have a nice day without the formalism.***
