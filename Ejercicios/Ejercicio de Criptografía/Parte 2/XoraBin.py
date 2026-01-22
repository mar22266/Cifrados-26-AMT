# codigo que aplcia xor a una cadena binaria


# limpia la cadana binaria de espacios u otros caracteres
def LimpiarCadenaBinaria(CadenaOriginal):
    CadenaLimpia = ""
    for Caracter in CadenaOriginal:
        if Caracter == "0" or Caracter == "1":
            CadenaLimpia = CadenaLimpia + Caracter

    return CadenaLimpia


# se agrupa en 8
def AgruparEnOctetos(CadenaBinariaLimpia):
    ResultadoAgrupado = ""
    ContadorBits = 0

    # Se recorre cada bit
    for Bit in CadenaBinariaLimpia:
        # verificacion si agregar espacio
        if ContadorBits > 0 and (ContadorBits % 8) == 0:
            ResultadoAgrupado = ResultadoAgrupado + " "

        # se agrega bit actual
        ResultadoAgrupado = ResultadoAgrupado + Bit

        # Incrementa conta
        ContadorBits = ContadorBits + 1

    return ResultadoAgrupado


# se aoplica xor a un bit
def AplicarXorABit(BitTexto, BitClave):
    # Se convierte carac a numericos
    ValorTexto = ord(BitTexto) - ord("0")
    ValorClave = ord(BitClave) - ord("0")

    # XOR logico
    if ValorTexto == ValorClave:
        Resultado = 0
    else:
        Resultado = 1

    # se convierte a 0 1
    BitResultado = chr(Resultado + ord("0"))

    return BitResultado


# se aplica xor a la cadena binaria con la clave
def AplicarXorACadenaBinaria(CadenaBinariaLimpia, CadenaClaveLimpia):

    ResultadoXorLimpio = ""

    LongitudTexto = len(CadenaBinariaLimpia)
    LongitudClave = len(CadenaClaveLimpia)

    # si no hay clave no hay xor
    if LongitudClave == 0:
        return ""

    # Se recorre cada bit del texto
    Posicion = 0
    while Posicion < LongitudTexto:
        BitTexto = CadenaBinariaLimpia[Posicion]

        # Calcula pos del bit y se usa mod para dar vueltas en la claveq
        PosicionClave = Posicion % LongitudClave
        BitClave = CadenaClaveLimpia[PosicionClave]

        BitXor = AplicarXorABit(BitTexto, BitClave)
        ResultadoXorLimpio = ResultadoXorLimpio + BitXor
        Posicion = Posicion + 1

    return ResultadoXorLimpio


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Aplicar XOR a una cadena binaria ===")
    print("Ingresa el texto en binario")
    print("Ingresa clave que se va a repetir hasta completar el texto")

    CadenaBinariaOriginal = input("Escribe la cadena binaria del texto: ")
    CadenaClaveOriginal = input("Escribe la cadena binaria de la clave: ")
    CadenaBinariaLimpia = LimpiarCadenaBinaria(CadenaBinariaOriginal)
    CadenaClaveLimpia = LimpiarCadenaBinaria(CadenaClaveOriginal)

    CadenaResultadoLimpia = AplicarXorACadenaBinaria(
        CadenaBinariaLimpia, CadenaClaveLimpia
    )

    CadenaBinariaAgrupada = AgruparEnOctetos(CadenaBinariaLimpia)
    CadenaResultadoAgrupada = AgruparEnOctetos(CadenaResultadoLimpia)

    print("\nTexto binario limpio (agrupado en 8 bits):")
    print(CadenaBinariaAgrupada)
    print("\nClave binaria limpia:")
    print(CadenaClaveLimpia)
    print("\nResultado de aplicar XOR (agrupado en 8 bits):")
    print(CadenaResultadoAgrupada)


# llamada a la funcion principal
if __name__ == "__main__":
    Main()
