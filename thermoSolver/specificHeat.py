from .Objects import element
import math


def cp(CompoundName, Temp):

    if (CompoundName == 'Air'):
        a1 = element.compound['Nitrogen']['SpecificHeatCp']['a']
        b1 = element.compound['Nitrogen']['SpecificHeatCp']['b']
        c1 = element.compound['Nitrogen']['SpecificHeatCp']['c']
        d1 = element.compound['Nitrogen']['SpecificHeatCp']['d']

        a2 = element.compound['Oxygen']['SpecificHeatCp']['a']
        b2 = element.compound['Oxygen']['SpecificHeatCp']['b']
        c2 = element.compound['Oxygen']['SpecificHeatCp']['c']
        d2 = element.compound['Oxygen']['SpecificHeatCp']['d']

        a = 0.71*a1 + 0.29*a2
        b = 0.71*b1 + 0.29*b2
        c = 0.71*c1 + 0.29*c2
        d = 0.71*d1 + 0.29*d2

        lower_temp = element.compound['Nitrogen']['SpecificHeatCp']['range'][0]
        higher_temp = element.compound['Nitrogen']['SpecificHeatCp']['range'][1]

    else:
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
