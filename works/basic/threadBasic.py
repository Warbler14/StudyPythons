# -*- coding: utf-8 -*-

import time
import threading


def long_task():
    for x in range(5):
        time.sleep(1)
        print('working:%s\n' % x)


print('start')

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('End')
