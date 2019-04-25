#/bin/python3

from math import pi, sqrt, exp
import time

def printNbValues(nb):
    print("    Number of values:\t", nb, sep='')

def printStdDev(value, nb, stdDev):

    return stdDev

def printArithmMean(value, nb, arithmMean):
    newArithmMean = (arithmMean * nb + value) / (nb + 1)
    print("    Arithmetic mean:\t", "%.2f" % newArithmMean)
    return newArithmMean

def printHarmoMean(value, nb, harmoMean):
    sommeInv = nb / harmoMean
    newHarmoMean = (nb + 1) / (sommeInv + (1 / value))
    print("    Harmonic mean:\t", "%.2f" % newHarmoMean)
    return newHarmoMean