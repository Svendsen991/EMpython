# -*- coding: utf-8 -*-

import numpy as np

import functions as func
import printJSON
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
z_L2 = func.TL_find_zL_GAMMA(-1 * absGAMMA)
Z_0 = 50 # Ved ikke hvad Z_0 er, men det kunne være 50 OHM
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

# Spørgsmål 12
# Billede nr. 1

# Spørgsmål 13
# -1 Ulaby s. 378

# Spørgsmål 14
n1 = 1.5
n2 = 2.1
n3 = 1.5
angle1 = 41.2
angle2 = func.WRT_find_Tangle_n1n2Angle(n1, n2, angle1)
angle3 = func.WRT_find_Tangle_n1n2Angle(n2, n3, angle2)
print("Spørgsmål 14: angle2: ", angle2, "angle3: ", angle3)

# Spørgsmål 15
# Måske both Ulaby s. 400

# Spørgsmål 16
# tau = 1 + GAMMA Ulaby s. 400

# Spørgsmål 17
# 1/r^2 Ulaby s. 204

# Spørgsmål 18
# q1 = -
# q2 = +
# q3 = -
# q4 = +

# Spørgsmål 19
# Billede 2 Ulaby s. 271

# Spørgsmål 20
# F = q(E + v cross B) Ulaby s. 295. 

# Spørgsmål 21
freq = 11 * prefix.G_giga()
# Air 
mu_r = 1
epsilon_r = 1

lamb = func.findLambdaWaveLenght(freq, mu_r, epsilon_r)
length = 3 * prefix.m_milli()
print(length / lamb)

print(1 * prefix.n_nano() * freq * 2 * np.pi)
# Regn det sidste på smith chart
# Zin = 11.3 OMH 36.2 grader


# Spørgsmål 22 
Zsc = 3.01 * 1.j
Zoc = -1.44 * 1.j * prefix.k_kilo()

Z_0 = func.TL_find_Z0_ZscZoc(Zsc, Zoc)
print("Spørgsmål 22: Z_0", Z_0)


# Spørgsmål 23
freq = 10 * prefix.M_mega()
length = 15 * prefix.c_centi()

omega = func.findOmega_Freq(freq)
beta = func.TL_find_beta_lenZscZoc(length, Zsc, Zoc)

print("Spørgsmål 23: Up: ", func.TL_find_Up_OmegaBeta(omega, beta))

# Spørgsmål 24
E0 = [1 + 1.j, 3 + 3.j, 2 + 2.j]
E0real = [1, 3, 2]
E0imag = [1, 3, 2]

print("Spørgsmål 24: ", func.getPolarization(E0real, E0imag))
print("Spørgsmål 24: ", func.POL_find_polarization(E0))

# Spørgsmål 25
lamb = 580 * prefix.n_nano()

beta = func.findBeta_lambda(lamb)
print("Spørgsmål 25: ", beta)

# Spørgsmål 26

## Air
mu_r = 1
epsilon_r = 1

Efield = np.multiply(E0, 1)
eta = func.WP_find_eta_murEpr(mu_r, epsilon_r)

S = func.POW_find_powerDensity_EfieldEta(Efield, eta)
print("Spørgsmål 26: ", S)

# Spørgsmål 27
freq = 1 * prefix.G_giga()
omega = func.findOmega_Freq(freq)
# glass
mu_r_g = 1
epsilon_r_g = 5.3
sigma_g = 0
# Water
mu_r_w = 1
epsilon_r_w = 80
sigma_w = 4

eta_g = func.WRT_find_eta_c_murEprSig(mu_r_g, epsilon_r_g, sigma_g, omega)
eta_w = func.WRT_find_eta_c_murEprSig(mu_r_w, epsilon_r_w, sigma_w, omega)

GAMMA = func.WRT_find_GAMMA_eta1eta2(eta_g, eta_w)

print("Spørgsmål 27: ", GAMMA)

# Spørgsmål 28
R = func.WRT_find_R_GAMMA(GAMMA)
T = func.WRT_find_T_R(R)
print("Spørgsmål 28: ", T)

# Spørgsmål 29
# Air
mu_r = 1
epsilon_r = 1
eta_a = func.WP_find_eta_murEpr(mu_r, epsilon_r)
# Not air but lossless
mu_r_2 = 1
epsilon_r_2 = 10.2
eta2 = func.WP_find_eta_murEpr(mu_r_2, epsilon_r_2)

angle_i = 60 # degrees

GAMMA_TE = func.WRT_find_GAMMAperpen_eta1eta2Angle(eta_a, eta2, angle_i)
R = func.WRT_find_R_GAMMA(GAMMA_TE)
print("Spørgsmål 29: ", R)

# Spørgsmål 30
GAMMA_TM = func.WRT_find_GAMMAparallel_eta1eta2Angle(eta_a, eta2, angle_i)
R = func.WRT_find_R_GAMMA(GAMMA_TM)
T = func.WRT_find_T_R(R)
print("Spørgsmål 30: ", T)

# Spørgsmål 31
# None lektion 19 tavle 8 
# Der findes ingen brewster angle for TE når mu1 = mu2.
# Derfor vil der altid være reflektion fra TE

# Spørgsmål 41

waveLength = 208 * prefix.n_nano()

# Glass
n_g = 2.5
Up = func.WRT_find_Up_n(n_g)
freq = func.TL_find_freq_lambdaUp(waveLength, Up)
print("Spørgsmål 41: Frequency: ", freq)


# Spørgsmål 42
E0real = [1,0,0]
E0imag = [-2,+1,0]
major, minor, AR = func.findMajorAndMinorSemiAxis(E0real, E0imag)

print("Spørgsmål 42: Major: ", major, "minor: ", minor, "AR: ", AR)

# Spørgsmål 43

betaVec1 = [0,12.1,0]
print("BetaVec1: ",func.getRightOrLeftPolE_field(E0real, E0imag, betaVec1))

betaVec2 = [0,0,-30.2]
print("BetaVec2: ",func.getRightOrLeftPolE_field(E0real, E0imag, betaVec2))

betaVec3 = [-4.81,2 * (-4.81), 0]
print("BetaVec3: ",func.getRightOrLeftPolE_field(E0real, E0imag, betaVec3))

betaVec4 = [0,0,8.12]
print("BetaVec4: ",func.getRightOrLeftPolE_field(E0real, E0imag, betaVec4))

# Svar nummer 4 er det eneste der er right-hand polorized  
# Derfor nummer 4
