# -*- coding: utf-8 -*-
import testMod1
from testMod1 import *
import testMod2
import os
from works.basic.system import sysImport

print('--- testMod1 ---')
print(testMod1.__name__)

print(testMod1.add(22, 7))
print(add(22, 7))
print(testMod1.sub(22, 7))
print(sub(22, 7))

print('--- testMod2 ---')
math = testMod2.Math()
print(math.solv(2))
print(testMod2.add(testMod2.PI, 1.0))

print('--- file check ---')
print(__file__)
print(os.path.relpath(__file__))
print(os.path.abspath(__file__))
print(os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)))

print('--- module import ---')
sysImport.path_append_on_cwd('/module')
import testMod3
print(testMod3.sqrt(3))
