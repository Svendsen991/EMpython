# -*- coding: utf-8 -*-

import numpy as np

import functions as func
import printJSON 

## 

mu_zero = printJSON.getMu_0()
epsilon_zero = printJSON.getEpsilon_0()

printJSON.constants()
printJSON.meterials()


print("BetaHat: ", func.find_betaHatVec_EfieldHfield([1,-1,1], [1,2,1]))


GAMMA = (-1/3) * 1.j
SWR = func.find_SWR_GAMMA(GAMMA)

print("SWR: ", SWR)

Z_L = func.find_ZL_GAMMAZ0(0.13, 75, pol=True, deg=True, angle=30)
print("Z_L: ", Z_L)
