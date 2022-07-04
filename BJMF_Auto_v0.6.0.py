from selenium import webdriver
import time,datetime,sys


# Information / 需要填写的个人信息
qq_acount = '123456789' # 绑定的qq账号
qq_password = '123456789' # 绑定的qq密码
log_file_directory = '/Users/xxx/Documents/PycharmProjects/BJMF_Auto/BJMF_Auto.log' # 用于记录打卡数据的记录文件，你可以通过新建一个txt文本文件，并将其后缀名修改为.log获得一个空的log文件，请根据自己的log文件修改路径位置。
BJMF_covid19_URL = 'http://banjimofang.com/student/course/12345/profiles/29' # 通过网页登陆班级魔方，并将「防疫专项-健康日报」的URL复制到此处。
location = '|26.63999,111.41659' # 用于定位的地理位置信息。格式为：|纬度,经度,例如:'|26.63999,111.41659'。如果你不清楚，可以查看历史填写的数据。
sheet_location = '湖南省长沙市' # 对应表格-「现在居住地 精确到省、市」选项
travel_log_QR_code_screenshot_file = '/Users/xxx/Downloads/screenshot.PNG' # 行程码截图文件路径。
results_screenshot_directory = '/Users/xxx/Documents/PycharmProjects/BJMF_Auto/BJMF_Screenshot/' # 用于储存打卡结果的截图文件存放路径（文件夹），如果你不确定今天的打卡情况，可以检查这个文件夹里的浏览器打卡截图。
chrome_driver_directory = '/usr/local/bin/chromedriver' # chromedriver的默认安装位置，如果你是macOS，默认安装chromedriver后，此处不必修改。


# try to ignore alert function
def try_to_ignore_alert(wd):
    try:
        wd.switch_to.alert.accept()
    except:
        time.sleep(1)
    try:
        wd.switch_to.alert.accept()
    except:
        time.sleep(1)
    try:
        wd.switch_to.alert.accept()
    except:
        time.sleep(1)
    try:
        wd.switch_to.alert.accept()
    except:
        time.sleep(1)
    try:
        wd.switch_to.alert.accept()
    except:
        time.sleep(1)


# 获取当前日期与时间
now_time = time.strftime("%H%M%S")
now_date = str(datetime.date.today().year)  + \
           str(datetime.date.today().month).zfill(2) + \
           str(datetime.date.today().day).zfill(2)


# 检查今天是否已经完成打卡
with open(log_file_directory) as logfile:
    logfile_content = logfile.read()
if now_date in logfile_content:
    print("今天已打卡")
    sys.exit()
print('开始打卡')



# 创建一个无窗口的chrome浏览器进程
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
wd = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_directory)



# 模拟使用qq登录班级魔方
wd.get('http://banjimofang.com/student')
element_submit = wd.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div/div[2]/a')
element_submit.click()
time.sleep(2)
wd.switch_to.frame(0)
wd.find_element_by_xpath(".//*[@id='switcher_plogin']").click()
element_qq_account = wd.find_element_by_id('u')
time.sleep(1)
element_qq_account.send_keys(qq_acount)
time.sleep(1)
element_qq_password = wd.find_element_by_id('p')
time.sleep(1)
element_qq_password.send_keys(qq_password)
time.sleep(1)
element_qq_login = wd.find_element_by_id('login_button')
element_qq_login.click()
time.sleep(3)



# 跳转至每日健康报告&处理警告窗口
wd.get(BJMF_covid19_URL)
wd.switch_to.alert.accept()
time.sleep(2) #等待加载
try_to_ignore_alert(wd)


# 填写表单元素
element_01 = wd.find_elements_by_xpath('//*[@id="profileform"]/div[1]/div/input')[0]
element_01.send_keys(sheet_location)
element_02 = wd.find_element_by_xpath('//*[@id="profileform"]/div[2]/div/label[2]')
element_02.click()
element_03 = wd.find_element_by_xpath('//*[@id="profileform"]/div[3]/div/label[2]')
element_03.click()
element_04 = wd.find_element_by_xpath('//*[@id="profileform"]/div[4]/div/label[2]')
element_04.click()
element_05 = wd.find_element_by_xpath('//*[@id="profileform"]/div[5]/div/label[2]')
element_05.click()
element_06 = wd.find_element_by_xpath('//*[@id="profileform"]/div[6]/div/label[2]')
element_06.click()
element_07 = wd.find_element_by_xpath('//*[@id="profileform"]/div[7]/div/label[2]')
element_07.click()

# 填写定位信息 / Remove unchangeable element attribute - auto_locate_by_wechat_function
try:
    element_auto_locate = wd.find_elements_by_xpath('//*[@id="profileform"]/div[8]/div/input')[0]
    wd.execute_script("arguments[0].removeAttribute('readonly')",element_auto_locate)
    element_auto_locate.send_keys(location)
except:
    pass

# 上传截图文件 / upload file
element_upload = wd.find_element_by_xpath('//*[@id="bjmfuploader_form_up_i"]')
element_upload.send_keys(travel_log_QR_code_screenshot_file)
time.sleep(10)



# 提交 / submit sheet
element_submit_report = wd.find_element_by_xpath('//*[@id="profileform"]/div[11]/button')
element_submit_report.click()



# 生成打卡截图并记录log文件
screenshot_file_pre_dir_path = results_screenshot_directory # 修改引号内的内容为保存截图的路径，改默认路径不可用。
screenshot_file_name = 'ScreenShot' + '_' + now_date + '_' + now_time + '.png'
screenshot_file_path = screenshot_file_pre_dir_path + screenshot_file_name

with open(log_file_directory,'a') as new_logfile:
    new_logfile.write('\n' + now_date + '_' + now_time )



# 退出chrome浏览器并保存截图
time.sleep(2)
try_to_ignore_alert(wd)
wd.get_screenshot_as_file(screenshot_file_path)



print('打卡成功')
wd.quit()