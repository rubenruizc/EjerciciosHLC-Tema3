def recorrido(cadena: str):

    cadena = cadena.replace(" ", "")  
    resta = 0
    diferenciaPisos = 0
    
    for i in range(len(cadena) - 1):  
        resta = int(cadena[i]) - int(cadena[i + 1])
        diferenciaPisos += abs(resta)

    return diferenciaPisos