import random
import MakeSpaceTower
# import hypar
# Import the classes we'll need.

from aecSpace.aecColor import aecColor
from aecSpace.aecPoint import aecPoint
from aecSpace.aecSpace import aecSpace
from aecSpace.aecSpacer import aecSpacer
from aecSpace.aecSpaceGroup import aecSpaceGroup
from aecSpace.aecSpaceDrawOCC import aecSpaceDrawOCC
import itertools
import space_cfm_calc
import math


spaces = [{'area': 5957.857142857145, 'l': [6787.5, 23531.785714285717, 97373.0], 'end': [6787.5, 17573.928571428572, 97373.0], 'cfm': 16320.0, 'width': 914.4, 'height': 1041.3999999999999},{'area': 5957.857142857145, 'l': [6787.5, 23531.785714285717, 97373.0], 'end': [6787.5, 17573.928571428572, 97373.0], 'cfm': 16320.0, 'width': 914.4, 'height': 1041.3999999999999}]
ductSpecs = [{'weight': 5957.857142857145, 'area': [6787.5, 23531.785714285717, 97373.0], 'end': [6787.5, 17573.928571428572, 97373.0], 'cfm': 16320.0, 'width': 914.4, 'height': 1041.3999999999999},{'weight': 5957.857142857145, 'area': [6787.5, 23531.785714285717, 97373.0], 'end': [6787.5, 17573.928571428572, 97373.0], 'cfm': 16320.0, 'width': 914.4, 'height': 1041.3999999999999}]


def air(spaces, ductSpecs):
    duct = []
    totalair = 0
    totalarea = 0
    area = []
    for x in spaces:
        duct.append(x.get("cfm"))
        area.append(x.get("area"))
    ductpounds = []
    for x in ductSpecs:
        weight = x.get("weight")*0.00328084
        width = x.get("width")*0.00328084
        height = x.get("height")*0.00328084
        widtharea = 2*(weight*width)
        heightarea = 2*(weight*height)
        ductpounds.append(widtharea+heightarea*1.1)
    print("Duct Poundage (lbs.): ",str(math.ceil(sum(ductpounds))))
    print("Duct Cost ($): ", str(math.ceil(sum(ductpounds)*3)))
    totalair = sum(duct)
    totalarea = sum(area)
    print("Total Air (CFM): ",str(math.ceil(totalair)))
    shaftdim = math.sqrt(totalair/2000)
    print("Shaft Size (ftxft): ", str(round(shaftdim, 2)),"x",str(round(shaftdim,2)))
    print("Total Floor Area (sq. ft.): ",str(round(math.ceil(totalarea),2)))
    bldgcfmsqft = totalair/totalarea
    print("Bldg CFM/Sq. Ft: ",str(round(bldgcfmsqft,2)))
    return (totalair,totalarea,bldgcfmsqft)

    #chiller
def chiller(supplyair):
    chillerton=supplyair/400
    print("Chiller Size (tons): ",str(round(chillerton, 2)))
    print("Chiller Cost ($): ", str(round(chillerton*660,0)))
    return chillerton

def boiler(area):
    boilerhp=area/1000
    print("Boiler HP:", boilerhp)
    print("Boiler Cost ($):", str(boilerhp*375))
    return boilerhp


if __name__ == "__main__":
    air(spaces, ductSpecs)
    area = 15000
    boiler(area)
    totalair = 32640
    chiller(totalair)
