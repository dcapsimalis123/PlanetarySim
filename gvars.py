import numpy as np


def init(ig = -9.8, idt = 0.1, iyBound = [0,0], iBounceCoef = 1, iSimLength = 10):
    global g
    global dt
    global ybound
    global bounce_coef
    global simLength


    g    = ig
    dt   = idt
    ybound = iyBound
    bounce_coef = iBounceCoef
    simLength = iSimLength