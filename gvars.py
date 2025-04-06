import numpy as np


def init(ig = -9.8, idt = 0.1, iyBound = [0,0], iBounceCoef = 1, iSimLength = 10):
    global g           # gravity coefficient, rn its inputable, will turn into the gravitational constant with true interobject force updates
    global dt          # time step size
    global ybound      # [lowest, tallest] point. Tallest currently not implimented
    global bounce_coef # amount of velocity lost at a bounce with ground TODO: make this more inline with forces
    global simLength   # total amount time running (assumed to be seconds)


    g    = ig
    dt   = idt
    ybound = iyBound
    bounce_coef = iBounceCoef
    simLength = iSimLength