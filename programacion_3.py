#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Number", type=int, help="Debe ser un valor entero positivo")
args = parser.parse_args()

assert args.Number>0,"El numero no puede ser igual ni menor a cero"

import programacion_2
if sum(programacion_2.divisores(args.Number)) - list.pop(programacion_2.divisores(args.Number)) == args.Number:
  print "El número ingresado es perfecto"
else:
  print "El número ingresado NO es perfecto"

