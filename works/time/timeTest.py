# -*- coding: utf-8 -*-
# 테스트 2020-05-24

import time


def sleep_test(cnt):
    current = cnt
    while current > 0:
        print(current)
        time.sleep(1)
        current = current - 1


count = 10
sleep_test(count)
