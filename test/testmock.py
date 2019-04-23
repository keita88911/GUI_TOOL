#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mock

class By(object):

    def add(self, a, b):
        return a + b + self.multiply(a,b)

    def multiply(self, a, b):
        pass

b  = By()

class MockDemo(object):
    def __init__(self):
        self.b  = b

    @mock.patch.object(b,'multiply')
    def test_add(self,mock_multiply):
        a = 3
        b = 5
        mock_multiply.return_value = 15
        if self.b.add(a,b) == 23:
            print "mock成功"
        else:
            print "mock失败"

if __name__ == '__main__':
    MockDemo().test_add()