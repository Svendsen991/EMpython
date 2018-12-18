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