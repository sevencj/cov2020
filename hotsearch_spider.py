from selenium.webdriver import Chrome, ChromeOptions
import time


def get_hot_topic():
    url = 'https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1'
    # 隐藏浏览器配置
    option = ChromeOptions()
    option.add_argument('headless')
    option.add_argument("--no-sandbox")
    # 创建浏览器对象
    browser = Chrome(options=option)
    # 获取指定网页源码
    browser.get(url)
    # 模拟点击查看更多
    more = browser.find_element_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/div')
    more.click()
    time.sleep(1)
    # 获取热点内容
    hot_spots = browser.find_elements_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/a/div/span[2]')
    hot_spot_list = [i.text for i in hot_spots]
    # 关闭浏览器
    browser.close()
    # print(hot_spot_list)
    return hot_spot_list


if __name__ == '__main__':
    print(get_hot_topic())
