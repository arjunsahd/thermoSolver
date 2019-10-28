from . import specificHeat

def calcOut(T_guess, CompoundOut, MFlowListOut):
    out = 0
    for i in range(0,len(CompoundOut)):
        out += MFlowListOut[i]*specificHeat.cp(CompoundOut[i], T_guess)
    return out

def calcIn(TempAirIn, CompoundIn, MFlowListIn):
    out = 0
    for i in range(0,len(CompoundIn)):
        out += MFlowListIn[i]*specificHeat.cp(CompoundIn[i], TempAirIn)*(TempAirIn - 298)
    return out

def TAdiabatic(TempAirIn, LowerHeatingValue, T_guess, CompoundIn, CompoundOut, MFlowListOut, MFlowListIn ):

    T_guess_new = T_guess
    delta_T = 100

    while delta_T > 10:

        T_guess = T_guess_new
        Out = calcOut(T_guess, CompoundOut, MFlowListOut)
        In = calcIn(TempAirIn, CompoundIn, MFlowListIn)
        T_guess_new = (In + LowerHeatingValue)/Out + 298
        delta_T = abs(T_guess_new - T_guess)

    return T_guess_new

