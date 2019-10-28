from .Objects import element
import math


def cp(CompoundName, Temp):

    a = element.compound[CompoundName]['SpecificHeatCp']['a']
    b = element.compound[CompoundName]['SpecificHeatCp']['b']
    c = element.compound[CompoundName]['SpecificHeatCp']['c']
    d = element.compound[CompoundName]['SpecificHeatCp']['d']

    lower_temp = element.compound[CompoundName]['SpecificHeatCp']['range'][0]
    higher_temp = element.compound[CompoundName]['SpecificHeatCp']['range'][1]

    if lower_temp <= Temp <= higher_temp:
        return a + b*Temp + c*math.pow(Temp, 2) + d*math.pow(Temp, 3)
    else:
        return -1
