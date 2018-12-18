# EMpython - documentation not finished 
This python lib can be used freely but it's build for solving problems in course 31035 "Anvendt elektromagnetisme" DTU


## 31035 Anvendt elektromagnetisme


**Install python 3 and pip**
 > sudo apt install python3 python3-pip

**Install numpy**
 > pip3 install numpy

</br>
***

1. **printJSON.py**

    > Print material table and constant table from Ulaby appendix B and FUNDAMENTAL PHYSICAL CONSTANTS
  
  - **constants()**

    Prints constant table
  
  - **meterials()**

    Prints material table

  - **getMu_0()**

    Returns mu zero

  - **getEpsilon_0()**

    Returns epsilon zero

***
</br>


2. **functions.py**

    > Helpful functions 

  - getPolarization(E_0real, E_0imag)

    **Input**
      > E_0real and E_0imag are real vectors

      > Should also work with H_0real and H_0imag as well
      
    **Output** 
      > Returns polarization

      > Else returns bool False
  
  - getRightOrLeftPolE_field(E_0real, E_0imag, betaVec)

     **Input**
      > E_0real, E_0imag and betaVec are real vectors

      > Only works with Electric field
      
    **Output** 
      > Returns left or right polarization

      > Else returns error message
  
  - getRightOrLeftPolH_field(H_0real, H_0imag, betaVec)

     **Input**
      > H_0real, H_0imag and betaVec are real vectors

      > Only works with Magnetic field
      
    **Output** 
      > Returns left or right polarization

      > Else returns error message
  

