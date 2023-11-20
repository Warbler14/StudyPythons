# -*- coding: utf-8 -*-

import time


def sleep_test(cnt, secs):
    current = cnt
    while current > 0:
        print(current)
        time.sleep(secs)
        current = current - 1


count = 10
secs = 2
sleep_test(count, secs)
