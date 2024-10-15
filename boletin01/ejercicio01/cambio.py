
def change (texto,num):
    letras =  (
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'
    )

    textoCifrado = ""

    for letra in texto:
        indice = letras.index(letra)
        if(indice == 26):
            indice = 0
        textoCifrado += letras[indice + num]


    return textoCifrado