# -*- coding: utf-8 -*-
# 테스트 2020-05-24

import time


def sleep_test(cnt):
    dot_mark = "*" * cnt
    current = cnt

    while current >= 0:
        print("\r %d  " % ((float(current) / cnt) * 100), end=dot_mark)
        time.sleep(1)
        current = current - 1
        dot_mark = "*" * current


count = 10
sleep_test(count)
