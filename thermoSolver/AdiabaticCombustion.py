from . import specificHeat

def calcOut(T_guess, CompoundOut, MFlowListOut):
    out = 0
    for i in range(0,len(CompoundOut)):
        out += MFlowListOut[i]*specificHeat.cp(CompoundOut[i], T_guess)
    return out

def calcIn(TempAirIn, CompoundIn, MFlowListIn):
    out = 0
    for i in range(0,len(CompoundIn)):
        out += MFlowListIn[i]*specificHeat.cp(CompoundIn[i], TempAirIn)
    return out

def TAdiabatic(TempAirIn, LowerHeatingValue, T_guess, CompoundIn, CompoundOut, MFlowListOut, MFlowListIn ):

    T_guess_new = T_guess
    delta_T = 10000

    while delta_T > 10:
        T_guess = T_guess_new
        Out = calcOut(T_guess, CompoundOut, MFlowListOut)
        In = calcIn(TempAirIn, CompoundIn, MFlowListIn)
        In = In + LowerHeatingValue

        print(In)
        print(Out)

        T_guess_new = (In*(TempAirIn - 298))/Out + 298
        delta_T = abs(T_guess_new - T_guess)
        print(T_guess_new)

    return T_guess_new
