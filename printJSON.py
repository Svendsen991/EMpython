# -*- coding: utf-8 -*-
##
##  Author:     Emil Svendsen
##  Date:       18/12-2018
##  Last edit:  18/12-2018

import json

def constants():
    with open("materials.json", "r") as material_file:
        data = json.load(material_file)
    for i in data['Constants']:
        print(i, ":\n\tSymbol:", data['Constants'][i]['Symbol'], "\n\tValue:", data['Constants'][i]['Value'], "\n\tSI unit:", data['Constants'][i]['SI unit'])

def meterials():
    with open("materials.json", "r") as material_file:
        data = json.load(material_file)
    for i in data['material']:
        print(i, ":\n\tμ_0:", data['material'][i]['permeability'], "\n\tε_0:", data['material'][i]['permittivity'])

def getMu_0():
    with open("materials.json", "r") as material_file:
        data = json.load(material_file)
    return data['GetMu0AndEpsilon0']['Mu_0']

def getEpsilon_0():
    with open("materials.json", "r") as material_file:
        data = json.load(material_file)
    return data['GetMu0AndEpsilon0']['Epsilon_0']
    