from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import unittest
# binary = FirefoxBinary(r"C:\Users\11237\AppData\Local\Mozilla Firefox\firefox.exe")
# browser = webdriver.Firefox(firefox_binary=binary)
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 汤姆听说有一个很酷的在线待办事项应用
        #他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        #他注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请他输入一个代办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        #他在文本框中输入了“Buy peacock feathers"(购买孔雀羽毛)
        #汤姆的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #他按回车后页面更新了
        #代办事项表格中显示了"1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        import time
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])

        #页面又显示了一个文本框，可以输入其他的代办事项
        #他又输入了"Use peacock feathers to make a fly"(使用孔雀羽毛做假蝇)
        #汤姆做事很有条理
        time.sleep(1)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #页面再次更新，他的清单中显示了这两个待办事项
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #汤姆想知道这个网站是否会记住他的清单
        #他看到网站为他生成了一个唯一的URL
        #而且页面中有一些文字解说这个功能
        self.fail('Finish the test!')
        #他访问哪个URL，发现他的代办事项列表还在

        #他很满意，去睡觉了
if __name__ == '__main__':
    unittest.main(warnings='ignore')