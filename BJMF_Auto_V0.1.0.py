from selenium import webdriver
import time,datetime


print('| *****       开始打卡      ***** |')

# 创建无窗口的chrome浏览器
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
wd = webdriver.Chrome(options=chrome_options)

# 模拟登录
wd.get('http://banjimofang.com/student')
element_username = wd.find_element_by_name('username')
element_username.send_keys('123456789') # 修改引号内的内容，填写为班级魔方的账号
element_password = wd.find_element_by_name('password')
element_password.send_keys('123456789') # 修改引号内的内容，填写为班级魔方的密码
element_submit = wd.find_elements_by_id('submit')
element_submit[0].click()

# 跳转至每日健康报告并模拟提交每日健康报告
wd.get('http://banjimofang.com/student/course/14912')
wd.get('http://banjimofang.com/student/course/14912/profiles?ids=28,29')
wd.get('http://banjimofang.com/student/course/14912/profiles/29')
time.sleep(2)
element_submit_report = wd.find_elements_by_xpath('//*[@id="profileform"]/div[9]/button')
element_submit_report[0].click()

# 获取打卡成功截图文件名
now_date = ''
now_time = time.strftime("%H%M%S")
now_date = str(datetime.date.today().year)  + \
           str(datetime.date.today().month).zfill(2) + \
           str(datetime.date.today().day).zfill(2)
screenshot_file_name = 'ScreenShot' + '_' + now_date + '_' + now_time + '.png'
screenshot_file_pre_dir_path = '/Users/ts/Desktop/BanJiMoFang_ScreenShot/' # 修改引号内的内容为保存截图的路径，改默认路径不可用。
screenshot_file_path = screenshot_file_pre_dir_path + screenshot_file_name

# 退出chrome浏览器并保存截图
print('| *****     打卡已经完成     ***** |')
time.sleep(0.5)
print('| *****        结束        ***** |')
time.sleep(3)
wd.get_screenshot_as_file(screenshot_file_path)
wd.quit()
