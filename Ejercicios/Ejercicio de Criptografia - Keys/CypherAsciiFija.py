# codigo genera cypher ascii con llave fija usando xor


# funcion de archivo pasados para convertir entero a binario de 8 bits
def ConvertirEnteroABinario8Bits(CodigoAscii):
    Binario8Bits = ""
    Potencia = 7
    while Potencia >= 0:
        ValorBit = 2**Potencia
        Bit = CodigoAscii // ValorBit
        if Bit == 1:
            CodigoAscii = CodigoAscii - ValorBit
            Binario8Bits = Binario8Bits + "1"
        else:
            Binario8Bits = Binario8Bits + "0"
        Potencia = Potencia - 1

    return Binario8Bits


# funcion de script pasado para convertir binario de 8 bits a entero
def ConvertirBinario8BitsAEntero(TokenBinario):
    ValorEntero = 0
    for CaracterBit in TokenBinario:
        BitEntero = ord(CaracterBit) - ord("0")
        ValorEntero = (ValorEntero * 2) + BitEntero
    return ValorEntero


# funcion de script pasado para aplicar xor a un bit
def AplicarXorABit(BitTexto, BitClave):
    ValorTexto = ord(BitTexto) - ord("0")
    ValorClave = ord(BitClave) - ord("0")

    if ValorTexto == ValorClave:
        Resultado = 0
    else:
        Resultado = 1

    BitResultado = chr(Resultado + ord("0"))
    return BitResultado


# funcion de scripts para convertir texto ascii a binario ascii
def ConvertirTextoABinarioAscii(TextoAscii):
    ResultadoBinario = ""
    Indice = 0
    Longitud = len(TextoAscii)
    while Indice < Longitud:
        Caracter = TextoAscii[Indice]
        CodigoAscii = ord(Caracter)
        Binario8Bits = ConvertirEnteroABinario8Bits(CodigoAscii)
        if ResultadoBinario != "":
            ResultadoBinario = ResultadoBinario + " "

        ResultadoBinario = ResultadoBinario + Binario8Bits
        Indice = Indice + 1

    return ResultadoBinario


# esta genera la llave fija y genera cypher ascii con xor
def GenerarCypherConLlaveFija(TextoOriginal, LlaveTexto):
    TextoMinusculas = TextoOriginal.lower()
    LlaveMinusculas = LlaveTexto.lower()

    # si no hay llave no se genera cypher
    if len(LlaveMinusculas) == 0:
        return TextoMinusculas, LlaveMinusculas, "", "", "", ""

    # String para guardar cypher ascii
    CypherAscii = ""

    # bin del text llave repetida y cypher
    BinarioTexto = ""
    BinarioLlaveRepetida = ""
    BinarioCypher = ""
    LongitudTexto = len(TextoMinusculas)
    LongitudLlave = len(LlaveMinusculas)
    IndiceTexto = 0
    # Se recorre cada caracter del texto
    while IndiceTexto < LongitudTexto:
        CaracterTexto = TextoMinusculas[IndiceTexto]
        CodigoTexto = ord(CaracterTexto)
        BinarioTexto8 = ConvertirEnteroABinario8Bits(CodigoTexto)

        # Caracter de la llave repetida en caso sea mas largo el texto que la llave
        IndiceLlave = IndiceTexto % LongitudLlave
        CaracterLlave = LlaveMinusculas[IndiceLlave]
        CodigoLlave = ord(CaracterLlave)
        BinarioLlave8 = ConvertirEnteroABinario8Bits(CodigoLlave)

        # se aplica xor bit a bit
        BinarioXor8 = ""
        PosicionBit = 0
        while PosicionBit < 8:
            BitTexto = BinarioTexto8[PosicionBit]
            BitLlave = BinarioLlave8[PosicionBit]
            BitXor = AplicarXorABit(BitTexto, BitLlave)
            BinarioXor8 = BinarioXor8 + BitXor
            PosicionBit = PosicionBit + 1

        # Se convierte el binario xor de 8 bits a entero
        CodigoCypher = ConvertirBinario8BitsAEntero(BinarioXor8)

        # se convierte el entero a caracter ascii
        CaracterCypher = chr(CodigoCypher)

        # se arma cypher en ascii
        CypherAscii = CypherAscii + CaracterCypher

        # se arman cadenas binarias con sus espacios
        if BinarioTexto != "":
            BinarioTexto = BinarioTexto + " "
            BinarioLlaveRepetida = BinarioLlaveRepetida + " "
            BinarioCypher = BinarioCypher + " "

        BinarioTexto = BinarioTexto + BinarioTexto8
        BinarioLlaveRepetida = BinarioLlaveRepetida + BinarioLlave8
        BinarioCypher = BinarioCypher + BinarioXor8
        IndiceTexto = IndiceTexto + 1

    return (
        TextoMinusculas,
        LlaveMinusculas,
        CypherAscii,
        BinarioTexto,
        BinarioLlaveRepetida,
        BinarioCypher,
    )


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Genera cypher en ascii con llave fija K con XOR")
    TextoOriginal = input("Escribe el texto a cifrar: ")
    LlaveTexto = input("Escribe la llave K tamaño fijo: ")

    (
        TextoMinusculas,
        LlaveMinusculas,
        CypherAscii,
        BinarioTexto,
        BinarioLlaveRepetida,
        BinarioCypher,
    ) = GenerarCypherConLlaveFija(TextoOriginal, LlaveTexto)

    if LlaveMinusculas == "":
        print("\nLa llave no puede ser vacia. No se genero cypher.")
        return

    print("\nTexto original en minusculas:")
    print(TextoMinusculas)

    print("\nLlave K en minusculas (tamaño fijo):")
    print(LlaveMinusculas)

    print("\nTexto en binario ASCII (8 bits por caracter):")
    print(BinarioTexto)

    print(
        "\nLlave K puede ser repetida depende de longitud de texto de entrada y tamanio de llave en binario ASCII (alineada con el texto):"
    )
    print(BinarioLlaveRepetida)

    print("\nCypher en binario (resultado de XOR bit a bit):")
    print(BinarioCypher)

    print("\nCypher en ASCII (resultado final):")
    print(CypherAscii)

    print("\ncypher puede tener simbolos o caracteres que no son legibles,")
    print("porque es el resultado directo del XOR a nivel ASCII.")


# Punto de entrada del programa
if __name__ == "__main__":
    Main()
