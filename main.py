import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建Chrome WebDriver对象
driver = webdriver.Chrome()

url = 'https://activity.ourteacher.com.cn/'
user_name = '15879675827'
pass_word = 'Dt19971201'


# 打开Google网站


def parser_course(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    li_list = soup.find_all('li')
    data_list = []
    for li in li_list:
        span_list = li.find_all('span')
        data = (span_list[0].text.strip(), span_list[1].get('class')[0])
        data_list.append(data)
    return data_list


def start_study(flag_text):
    print(flag_text)
    driver.implicitly_wait(1)
    driver.find_element(By.LINK_TEXT, flag_text).click()
    driver.implicitly_wait(1)
    title = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[4]/div[2]/div/div[1]/span").text
    if '【选课】' in title:
        num = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[4]/div[2]/div/div[3]/div/div/span').text
        course_list = driver.find_element(By.ID, 'courseList')
        # 只选择第一个课程
        choseClass = course_list.find_elements(By.NAME, 'choseClass')
        for i in range(int(num)):
            choseClass[i].click()
            time.sleep(1)
        # 点击确认
        driver.find_element(By.ID, 'btnSelectCourse').click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, 'sure').click()
        driver.refresh()
        time.sleep(3)
    else:
        driver.find_element(By.LINK_TEXT, "立即学习").click()
        print(f'{flag_text}开始学习，开始时间：{time.strftime("%y-%m-%d %H:%M:%S")}')
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)
        learn_time = driver.find_element(By.ID, 'learnTime').text.split('/')[1][:-1]
        # print(learn_time)
        run_text = ''
        while True:
            try:
                var = driver.find_element(By.ID, 'learnTime').text
                if run_text != var:
                    run_text = var
                else:
                    driver.refresh()
                    driver.implicitly_wait(3)
            except Exception:
                driver.refresh()
                driver.implicitly_wait(3)
            # if time.time() - start_time > int(learn_time) * 60 + 60:
            #     print('超时')
            #     driver.refresh()
            try:
                if '可以进入下一环节学习' in driver.find_element(By.ID, 'lock').text:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[-1])
                    driver.refresh()
                    driver.implicitly_wait(2)
                    break
            except:
                pass
            try:
                # 随堂小测试
                div = driver.find_element(By.ID, 'ValidationPage')
                if '测试' in div.find_element(By.CLASS_NAME, 'modal-title').text:
                    div.find_element(By.ID, 'strA').click()
                    time.sleep(1)
                    div.find_element(By.ID, 'submit').click()
            except Exception as e:
                pass
            time.sleep(20)


driver.get(url)
driver.find_element(By.ID, 'aw-login-user-name').send_keys(user_name)
driver.find_element(By.ID, 'aw-login-user-password').send_keys(pass_word)
driver.find_element(By.ID, 'login_submit').click()

# print(driver.title)
# 等待搜索结果加载完成
driver.implicitly_wait(10)
if driver.title == '奥鹏教师教育网':
    driver.find_element(By.LINK_TEXT, '去学习').click()
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(10)
    while True:
        html = driver.find_element(By.XPATH, '//*[@id="LeftNav"]/div/div[2]/ul').get_attribute('outerHTML')
        d = parser_course(html)
        flag = False
        # print(d)
        for course in d:
            if course[1] == 'a-bg-tip-orange':
                start_study(course[0])

input('exit')
# 关闭浏览器
driver.quit()
