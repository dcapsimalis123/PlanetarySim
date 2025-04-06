import numpy as np


# simple 2D distance calculator
def dist_calc(pos1, pos2):
    temp = pos1 - pos2
    return np.sqrt(temp[0]**2+temp[1]**2)

# returns a unit vector between two points
def unit_vector(pos1, pos2):
    temp = pos1 - pos2
    return temp/dist_calc(pos1, pos2)

def init(ig = -9.8, idt = 0.1, iyBound = [0,0], iBounceCoef = 1, iSimLength = 10, iG = 1):
    global g           # gravity coefficient, rn its inputable, will turn into the gravitational constant with true interobject force updates
    global dt          # time step size
    global ybound      # [lowest, tallest] point. Tallest currently not implimented
    global bounce_coef # amount of velocity lost at a bounce with ground TODO: make this more inline with forces
    global simLength   # total amount time running (assumed to be seconds)
    global G   

    g    = ig
    G    = iG
    dt   = idt
    ybound = iyBound
    bounce_coef = iBounceCoef
    simLength = iSimLength