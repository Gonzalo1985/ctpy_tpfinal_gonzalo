#!/usr/bin/env python 
# -*- coding: utf-8 -*-


def divisores(number):
  from decimal import Decimal
  for i in range(1,number+1):
    division = Decimal(number)/Decimal(i)
    if division == int(division):
      print i
    else:
      print "no es divisor"
  return division
  
def main():
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("Number", type=int, help="Debe ser un valor entero positivo")
  args = parser.parse_args()

  assert args.Number>=0,"El numero no puede ser menor a cero"
  
  divisores(args.Number)

if __name__ == "__main__":
  main()
