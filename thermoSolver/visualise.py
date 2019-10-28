from chempy import balance_stoichiometry
from chempy import Substance

def equation(cmpin, cmpout):

    Set_in = set(cmpin)
    Set_out = set(cmpout)

    reac, prod = balance_stoichiometry(Set_in, Set_out)

    for i in range(len(cmpin)):
        if reac[cmpin[i]] != 1:
            print(reac[cmpin[i]], end ='')

        out = Substance.from_formula(cmpin[i])
        print(out.unicode_name, end='')
        if i!=len(cmpin) - 1:
            print(' + ', end = ''),

    print(' ----> ', end ='')

    for i in range(len(cmpout)):
        if prod[cmpout[i]] != 1:
            print(prod[cmpout[i]], end ='')
        out = Substance.from_formula(cmpout[i])
        print(out.unicode_name, end='')
        if i!=len(cmpout) - 1:
            print(' + ', end = ''),
