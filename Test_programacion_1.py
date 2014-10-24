#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest
import programacion_1

class MyTest(unittest.TestCase):
  
# testEqual para funciones "n_factorial", "sum_to_n" y "sum_to_inv_n"
  def testEqual1(self):
    self.assertEqual(programacion_1.n_factorial(0), 1)

  def testEqual2(self):
    self.assertEqual(programacion_1.sum_to_n(5), 15)

  def testEqual3(self):
    self.assertEqual(programacion_1.sum_to_inv_n(5), 1.0+(1.0/2)+(1.0/3)+(1.0/4)+(1.0/5))

# testIsNone para funciones n_factorial, sum_to_n y sum_to_inv_n
  def testIsNone1(self):
    self.assertIsNone(programacion_1.n_factorial(0))

  #def testIsNone2(self):
  #  self.assertIsNone(DRY_Gonzalo.surface_circle(-5))

  #def testIsNone3(self):
  #  self.assertIsNone(DRY_Gonzalo.Forest_Gump(-5))


if __name__ == '__main__':
  unittest.main()

