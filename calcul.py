#/bin/python3

from math import pi, sqrt, exp
import time

def printNbValues(nb):
    print("    Number of values:\t", nb, sep='')

def printStdDev(value, nb, arithmMean, stdDev):
    squareSum = (stdDev + pow(arithmMean, 2)) * nb
    tmpMean = (arithmMean * nb + value) / (nb + 1)
    newStdDev = ((squareSum + pow(value, 2)) / (nb + 1)) - pow(tmpMean, 2)
    print("    Standard deviation:\t", "%.2f" % newStdDev)
    return newStdDev

def printArithmMean(value, nb, arithmMean):
    newArithmMean = (arithmMean * nb + value) / (nb + 1)
    print("    Arithmetic mean:\t", "%.2f" % newArithmMean)
    return newArithmMean

def printQuadriMean(value, nb, arithmMean, stdDev):
    squareSum = (stdDev + pow(arithmMean, 2)) * (nb + 1)
    moyQuadra = sqrt((squareSum / (nb + 1)))
    print("    Root mean square:\t", "%.2f" % moyQuadra)
    return

def printHarmoMean(value, nb, harmoMean):
    sommeInv = nb / harmoMean
    newHarmoMean = (nb + 1) / (sommeInv + (1 / value))
    print("    Harmonic mean:\t", "%.2f" % newHarmoMean)
    return newHarmoMean