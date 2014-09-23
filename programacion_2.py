#!/usr/bin/env python 
# -*- coding: utf-8 -*-

def divisores(number):
  divisors = []
  for i in range(1,number+1):
    if number % i == 0: divisors.append(i)
  return divisors


#main()  
def main():
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("Number", type=int, help="Debe ser un valor entero positivo")
  args = parser.parse_args()

  assert args.Number>0,"El numero no puede ser igual ni menor a cero"
  
  print "Los divisores del número elegido son: "+str(divisores(args.Number))


if __name__ == "__main__":
  main()
