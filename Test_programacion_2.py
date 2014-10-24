#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest
import programacion_2

class MyTest(unittest.TestCase):
  
# testEqual para función "divisores"
  def testEqual1(self):
    a = [1]
    self.assertEqual(list(programacion_2.divisores(2)),  list(a.extend([2])))



if __name__ == '__main__':
  unittest.main()
