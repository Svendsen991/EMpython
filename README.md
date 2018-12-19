# EMpython - documentation not finished 
This python lib can be used freely but it's build for solving problems in course 31035 "Anvendt elektromagnetisme" DTU


## 31035 Anvendt elektromagnetisme

### Literature
  
  - Fundamentals of Applied Electromagnetics, Fawwaz T. Ulaby, Umberto Ravaioli. Referred as **Ulaby** 

  - [Class pictures link 1](https://www.dropbox.com/sh/mmwt50c62wx66n8/AAAk9syV4ZdBt49FdrQ1KfLya?dl=0)
  
  - [Class pictures link 2](https://drive.google.com/open?id=1poexgWhZUBpiSHl2aM6Wob38YJCyake8)


**Install python 3 and pip**
 > sudo apt install python3 python3-pip

**Install numpy**
 > pip3 install numpy

</br>

***

1. ## printJSON.py

    Print material table and constant table from Ulaby appendix B and FUNDAMENTAL PHYSICAL CONSTANTS
  
  - #### constants()

    > Prints constant table
  
  - #### meterials()

    > Prints material table

  - #### getMu_0()

    > Returns mu zero

  - #### getEpsilon_0()

    > Returns epsilon zero
  
  - #### getSpeedOfLight()

    > Returns speed of light

</br>

2. ## prefix.py

    Returns magnitude for easy convertion to meter.
    
    - E_exa()
    - P_peta()
    - T_tera()
    - G_giga()
    - M_mega()
    - k_kilo()
    - m_milli()
    - mu_micro()
    - n_nano()
    - p_pico()
    - f_femto()
    - a_atto()

</br>


3. ## functions.py

    Helpful functions 
  
  - ### Transmision line

    1. #### Find characteristic impedance Z_0 with R', G', L', C' and omega. Ulaby s. 89
    
        - General case

          > TL_find_Z0_RpGpLpCpOmega(Rp, Gp, Lp, Cp, omega)

    2. #### Find u_p Phase velocity with omega and beta. Ulaby s. 89

        - General case

          > TL_find_Up_OmegaBeta(omega, beta)

    3. #### Find Propagation constant (gamma = alpha + j*beta) with R', G', L', C' and omega. Ulaby s. 89

        - General case

          > TL_find_smallGamma_RpGpLpCp(Rp, Gp, Lp, Cp, omega)
    
    4. #### Find beta with omega and epsilon. Ulaby s. 89 and omega. Ulaby s. 89

        - Lossless case

          > TL_find_beta_omegaEpsilon(omega, epsilon_r)

    5. #### Find u_p Phase velocity with epsilon. Ulaby s. 89

        - Lossless case

          > TL_find_Up_epsilon(epsilon_r)
    
    6. #### Find characteristic impedance Z_0 with L' and C'. Ulaby s. 89

        - Lossless case

          > TL_find_Z0_LpCp(Lp, Cp)

    7. #### Find characteristic impedance Z_0 with epsilon, a (inner radius) and b (outer radius). Ulaby s. 89

        - Lossless coaxial

          > TL_find_Z0_epsilonAB(epsilon_r, a, b)
    
    8. #### Find R's with frequency, mu of conductor and sigma of conductor. Ulaby s. 76

        - General case

          > TL_find_Rs_freqMucSigmac(freq, mu_c, sigma_c)
    
    9. #### Find R' with R's, a and b. Ulaby s. 76

        - General coaxial case

          > TL_find_Rprime_RsAB(Rs, a, b)
    
    10. #### Find L' with mu (insulator), a and b. Ulaby s. 76

        - General coaxial case

          > TL_find_Lprime_muAB(mu_r, a, b)
    
    11. #### Find G' with sigma (insulator), a and b. Ulaby s. 76

        - General coaxial case

          > TL_find_Gprime_sigmaAB(sigma, a, b)
    
    12. #### Find C' with epsilon (insulator), a and b. Ulaby s. 76

        - General coaxial case

          > TL_find_Cprime_epsilonAB(epsilon_r, a, b)
    
    13. #### Find standing wave ratio (SWR) with reflection coefficient. Ulaby s. 94

        - General case
          
          > TL_find_SWR_GAMMA(GAMMA)

    13. #### Find standing wave ratio (SWR) with  with V_min and V_max. Ulaby s. 94

        - General case
          
          > TL_find_SWR_VminVmax(V_min, V_max)

    14. #### Find reflection coefficient (GAMMA) abs value with only SWR. Ulaby s. 94

        - General case
          
          > TL_find_absGAMMA_SWR(SWR)

    15. #### Find normalized load impedance (z_L) with GAMMA. Ulaby s. 90

        - General case
          
          > TL_find_zL_GAMMA(GAMMA)

    16. #### Find characteristic impedance with short- and opencircuit impedance. Ulaby s. 103

        - Lossless case
          
          > TL_find_Z0_ZscZoc(Zsc, Zoc)
    
    17. #### Find beta with length of TL and short- and opencircuit impedance. Ulaby s. 103.

        - Lossless case
          
          > TL_find_beta_lenZscZoc(lenght, Zsc, Zoc)

  - ### Plane-wave propagation

    1. #### Find betahat vector with E_field and H_field. Ulaby s. 369

        - Plane-wave case !!**Only returns beta hat vector**!!
          
          > find_betaHatVec_EfieldHfield(E_field, H_field)
    
    2. #### Find reflection coefficient (big Gamma) with Z_L and Z_0. Ulaby s. 90

        - Plane-wave case
          
          > find_GAMMA_ZLZ0(Z_L, Z_0)   
        
    
    3. #### Find Z_L with reflection coefficient and Z_0. Ulaby s. 90 If GAMMA is on polar form, pol needs to be True and GAMMA is magnitude and angle is angle. deg needs to be True if angle is in degrees.

        - Plane-wave case
          
          > find_ZL_GAMMAZ0(GAMMA, Z_0, pol=False, deg=False, angle=0)

  - ### Wave reflection and transmission

    1. #### Find reflection coefficient (GAMMA) with complex intrinsic impandance. Ulaby s. 379

        - Normal incidence

          > WRT_find_GAMMA_eta1eta2(eta1, eta2)

    2. #### Find reflection coefficient (GAMMA) with intrinsic impandance. Ulaby s. 379

        - Normal incidence

          > WRT_find_GAMMA_eta1eta2(eta1, eta2)
    
    3. #### Find complex intrinsic impandance with mu_r, epsilon_r, sigma and omega. Ulaby s. 379

        - Normal incidence !OBS! not tested

          > WRT_find_eta_c_murEprSig(mu_r, epsilon_r, sigma, omega)

    4. #### Find transmitting angle with n1, n2 (index of refraction) and incident angle. If deg=False radians is used. Ulaby s. 385

        - Snell's law 

          > def WRT_find_Tangle_n1n2Angle(n1, n2, angle)

  - ### Wave polarization

    1. #### Find E wave polarization with E0 vector. Vector can also be complex.  Lection 12 (9, 10, 11)

        - Plane wave

          >POL_find_polarization(E0_vector)


  - #### getPolarization(E_0real, E_0imag)

    ##### Input
      > E_0real and E_0imag are real vectors

      > Should also work with H_0real and H_0imag as well
      
    ##### Output
      > Returns polarization

      > Else returns bool False
  
  - #### getRightOrLeftPolE_field(E_0real, E_0imag, betaVec)

     ##### Input
      > E_0real, E_0imag and betaVec are real vectors

      > Only works with Electric field
      
    ##### Output
      > Returns left or right polarization

      > Else returns error message
  
  - #### getRightOrLeftPolH_field(H_0real, H_0imag, betaVec)

     ##### Input
      > H_0real, H_0imag and betaVec are real vectors

      > Only works with Magnetic field
      
    ##### Output
      > Returns left or right polarization

      > Else returns error message
  

