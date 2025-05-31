def CuentaDigitos(num,dig):
    if isinstance(num and dig,int) and dig<10 and dig>=0:
            return CuentaDigitos_Aux(abs(num),dig)
    else:
        return "Error"
def CuentaDigitos_Aux(num, dig):
    if num == 0:
        return 0
    elif num%10>dig:
        return 1+CuentaDigitos_Aux(num//10, dig)    
    else:
        return CuentaDigitos_Aux(num//10, dig)
