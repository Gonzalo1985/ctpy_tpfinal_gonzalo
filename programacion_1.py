#!/usr/bin/env python 
# -*- coding: utf-8 -*-

##################### Functions ############################

# Define y guarda la función n factorial
def n_factorial(number):
  assert number>=0,"El numero no puede ser menor a cero para calcular factorial"
  n_factorial = number
  for i in range(1,number):
    n_factorial = n_factorial*(number-i)
  return n_factorial

# Define y guarda la función inversa de n factorial
def n_factorial_inv(number):
  from decimal import Decimal
  assert number>0,"El numero no puede ser menor ni igual a cero para calcular función inversa de n factorial"
  n_factorial_inv = Decimal(1)/Decimal(n_factorial(number))
  return n_factorial_inv

# Define y guarda la función sumatoria de i hasta n
def sum_to_n(number):
  assert number>=0,"El numero no puede ser menor a cero para calcular la sumatoria hasta n"
  sum_to_n = 0
  for i in range(1,number+1):
    sum_to_n = sum_to_n + i
  return sum_to_n


############################################################

def main():

  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("Number", type=int, help="Debe ser un valor entero")
  args = parser.parse_args()

  print "La sumatoria hasta n es: "+str(sum_to_n(args.Number))
  print "El factorial del número elegido es: "+str(n_factorial(args.Number))
  print "La inversa del factorial del número elegido es: "+str(n_factorial_inv(args.Number))


if __name__ == "__main__":
  main()

