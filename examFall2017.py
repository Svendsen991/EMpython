# -*- coding: utf-8 -*-

import numpy as np

import functions as func
import prefix


# Spørgsmål 1
# [R'] = OHM / meter Ulaby s. 76

# Spørgsmål 2
# S = E × H 
# [S] = W / m^2 Ulaby s. 365

# Spørgsmål 3
# [J] = A / m^2 !OBS! Current density (volume) Ulaby appendix A

# Spørgsmål 4
# [B] = T Ulaby appendix A


# Spørgsmål 5
V_min = 0.5 # [V]
V_max = 5.5 # [V]

SWR = func.TL_find_SWR_VminVmax(V_min, V_max)
print("Spørgsmål 5: SWR: ", SWR)

# Spørgsmål 6
absGAMMA = func.TL_find_absGAMMA_SWR(SWR)
print("Spørgsmål 6: absGAMMA: ", absGAMMA)

# Spørgsmål 7
z_L1 = func.TL_find_zL_GAMMA(absGAMMA)
z_L2 = func.TL_find_zL_GAMMA(-absGAMMA)
Z_0 = 75 # Ved ikke hvad Z_0 er, men det kunne være 50 OHM
Z_L1 = Z_0 * z_L1
Z_L2 = Z_0 * z_L2
print("Spørgsmål 7: Z_L1: ", Z_L1, "Z_L2: ", Z_L2)

# Spørgsmål 8
# Inductive

# Spørgsmål 9
# lambda / 2

# Spørgsmål 10
# VSWR = 1

# Spørgsmål 11
# lambda / 8

# Spørgsmål 
# Spørgsmål 
# Spørgsmål 
# Spørgsmål 
# Spørgsmål 
# Spørgsmål 
