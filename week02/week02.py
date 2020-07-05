from selenium import webdriver
import time

try:
    brower=webdriver.Chrome()
    brower.get("https://shimo.im")
    time.sleep(3)
    #未向服务器发起请求，仅前段切换
    #brower.switch_to.frame(brower.find_element_by_tag_name('iframe'))
    btm1=brower.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    btm1.click()

    brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('15274906860')
    brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('Xiangwan01')
    time.sleep(3)
    brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    cookies=brower.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    brower.close()
