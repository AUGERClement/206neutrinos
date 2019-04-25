#/bin/python3

from math import pi, sqrt, exp
import time

def printNbValues(nb):
    print("\tNumber of values:\t", nb, sep='')

def printStdDev(value, nb, stdDev):
    return stdDev

def printArithmMean(value, nb, arithmMean):
    newArithmMean = (arithmMean * nb + value) / (nb + 1)
    print("\tArithmetic mean:\t", "%.2f" % newArithmMean)
    return newArithmMean

#206 : moy n + 1 = (moyenne n * n + nouvel elem) / n + 1
