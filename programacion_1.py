#!/usr/bin/env python 
# -*- coding: utf-8 -*-

##################### Functions ############################

# Define y guarda la función n factorial
def n_factorial(number):
  assert number>=0,"El numero no puede ser menor a cero"
  n_factorial = number
  for i in range(1,number):
    n_factorial = n_factorial*(number-i)
  return n_factorial

# Define y guarda la función inversa de n factorial



# Define y calcula factor Forest Gump


############################################################

def main():

  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("Number", type=int, help="Debe ser un valor entero")
  args = parser.parse_args()

  print "El factorial del número elegido es: "+str(n_factorial(args.Number))
  #print "La inversa del factorial del número elegido es: " 1/n_factorial(args.Number))
  
if __name__ == "__main__":
  main()

