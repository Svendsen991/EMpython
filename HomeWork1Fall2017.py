# -*- coding: utf-8 -*-

import numpy as np

import functions as func
import prefix


# Opgave 2

a = (1/2) * prefix.m_milli() ## ½mm
b = (6.12 / 2) * prefix.m_milli() ## 6.12 / 2 mm

mu_c = 1
sigma_c = 5.797 * 10**7

epsilon_r = 2
mu_r = 1
sigma_ins = 9.81 * 10**(-5)

freq = 1 * prefix.G_giga()

# a)

R_s = func.TL_find_Rs_freqMucSigmac(freq, mu_c, sigma_c)
R_p = func.TL_find_Rprime_RsAB(R_s, a, b)
G_p = func.TL_find_Gprime_sigmaAB(sigma_ins, a, b)
L_p = func.TL_find_Lprime_muAB(mu_r, a, b)
C_p = func.TL_find_Cprime_epsilonAB(epsilon_r, a, b)
omega = func.findOmega_Freq(freq)

Z_0 = func.TL_find_Z0_RpGpLpCpOmega(R_p, G_p, L_p, C_p, omega)

print("Rs: ", R_s, "Rp: ", R_p, "Gp: ", G_p, "Lp: ", L_p, "Cp: ", C_p, "Z0: ", Z_0)


# b)

gamma = func.TL_find_smallGamma_RpGpLpCp(R_p, G_p, L_p, C_p, omega)
alpha = np.real(gamma)
beta = np.imag(gamma)

print("Beta: ", beta)

# c)

print("Alpha: ", alpha)