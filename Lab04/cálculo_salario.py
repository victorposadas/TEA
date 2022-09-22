# Tendencia e Innovación en Tencología Agrícola (TEA)
# Función utilizada para calcular el pago de horas trabajadas, incluye horas extras.

def calcularpago(Horas, Tarifa):
    MAX_HORAS = 40
    if ((Horas) > MAX_HORAS):
        horas_extras = (Horas) - MAX_HORAS
    else:
        horas_extras = 0
    cálculo = (Horas) * (Tarifa)+ (horas_extras * ((Tarifa)/2))
    return cálculo
# Código Principal

try:
    Horas = float(input(" Ingrese número de horas: "))
    Tarifa = float(input(" Ingrese tarifa: "))
    Pago = calcularpago ( Horas, Tarifa)
    print (Pago)
except:
    print( "Error, valor ingresado no es válido")
