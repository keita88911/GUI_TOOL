#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 15:04
# @Author  : lcc
# @Site    :
# @File    : Demo.py
# @Software: PyCharm
# @TestCase: 打开百度 搜索关键字selenium  并验证
from selenium.webdriver import Firefox
import unittest,time
import ddt
from selenium import  webdriver

import  traceback
from selenium.common.exceptions import NoSuchElementException

@ddt.ddt
class MyTestCase(unittest.TestCase):
    #我这里是开启谷歌浏览器，请注意
    def setUp(self):
        self.driver = Firefox()

    @ddt.data(
        ["1","selenium"],
        ["2", "python"]
    )

    @ddt.unpack
    def test_something(self,testdata,excpectdata):
        # try:

        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(10)
        print(testdata+"=============="+excpectdata)
        self.driver.find_element_by_id("kw").send_keys(testdata)
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        #断言
        print  "++++++++"+self.driver.title
        self.assertTrue(excpectdata in self.driver.title)
        # except NoSuchElementException,e:
        #    (u'没有找到该元素，请核查'+str(traceback.format_exc()))
        # else:
        #   (u"搜索失败")

    def tearDown(self):
        print "come in "
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()