def verificar_digito_control(codigo):
    suma = 0

     # Longitud sin contar el dígito de control
    longitud = len(codigo) - 1 
    
    # Recorremos los dígitos de derecha a izquierda, ignorando el último
    for i in range(longitud):

        # Tomar el dígito desde la derecha
        digito = int(codigo[longitud - 1 - i])
        
        # (i % 2 == 0) corresponde a las posiciones impares de derecha a izquierda
        # Posiciones impares
        if i % 2 == 0:  
            suma += digito * 3

        # Posiciones pares
        else:  
            suma += digito

    # Calcular el dígito de control esperado
    digito_control_calculado = (10 - (suma % 10)) 
    
    # El último dígito es el dígito de control
    digito_control_real = int(codigo[-1])  

    return digito_control_calculado == digito_control_real