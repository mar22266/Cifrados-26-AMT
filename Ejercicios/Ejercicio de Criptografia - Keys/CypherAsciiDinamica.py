# codigo genera cypher ascii con llave dinamica usando xor

import random


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


# Funcion de script pasado para aplicar xor a un bit
def AplicarXorABit(BitTexto, BitClave):
    ValorTexto = ord(BitTexto) - ord("0")
    ValorClave = ord(BitClave) - ord("0")
    if ValorTexto == ValorClave:
        Resultado = 0
    else:
        Resultado = 1
    BitResultado = chr(Resultado + ord("0"))
    return BitResultado


# Funcion para generar la llave dinamica del mismo tamaño que el texto
def GenerarLlaveDinamicaPorTexto(LongitudTexto):
    Llave = ""
    Contador = 0

    while Contador < LongitudTexto:
        # Generar un codigo ASCII aleatorio entre 33 y 126 para que sean visibles idea de chatgpt
        CodigoAscii = random.randint(33, 126)
        Caracter = chr(CodigoAscii)
        Llave = Llave + Caracter
        Contador = Contador + 1

    return Llave


# funcion que genera cypher con llave dinamica usando xor
def GenerarCypherConLlaveDinamica(TextoOriginal):
    TextoMinusculas = TextoOriginal.lower()
    LongitudTexto = len(TextoMinusculas)

    # Si esta vacio el texto no se genera nada
    if LongitudTexto == 0:
        return TextoMinusculas, "", "", "", "", ""

    # genera llave din mismo tamanio q texto
    LlaveDinamica = GenerarLlaveDinamicaPorTexto(LongitudTexto)

    CypherAscii = ""
    BinarioTexto = ""
    BinarioLlave = ""
    BinarioCypher = ""

    IndiceTexto = 0
    while IndiceTexto < LongitudTexto:
        # Caracter del texto
        CaracterTexto = TextoMinusculas[IndiceTexto]
        CodigoTexto = ord(CaracterTexto)
        BinarioTexto8 = ConvertirEnteroABinario8Bits(CodigoTexto)

        # Caracter de la llave dinamica
        CaracterLlave = LlaveDinamica[IndiceTexto]
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

        # binario resultado a entero ASCII
        CodigoCypher = ConvertirBinario8BitsAEntero(BinarioXor8)

        # entero a caracter ASCII
        CaracterCypher = chr(CodigoCypher)

        # cypher en ascii
        CypherAscii = CypherAscii + CaracterCypher

        # se arman cadenas binarias con sus espacios
        if BinarioTexto != "":
            BinarioTexto = BinarioTexto + " "
            BinarioLlave = BinarioLlave + " "
            BinarioCypher = BinarioCypher + " "

        BinarioTexto = BinarioTexto + BinarioTexto8
        BinarioLlave = BinarioLlave + BinarioLlave8
        BinarioCypher = BinarioCypher + BinarioXor8

        IndiceTexto = IndiceTexto + 1

    return (
        TextoMinusculas,
        LlaveDinamica,
        CypherAscii,
        BinarioTexto,
        BinarioLlave,
        BinarioCypher,
    )


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Genera cypher en ascii con llave dinamica K con XOR ===")
    print("La llave K se generara automaticamente con la misma longitud del texto.\n")
    TextoOriginal = input("Escribe el texto a cifrar: ")

    (
        TextoMinusculas,
        LlaveDinamica,
        CypherAscii,
        BinarioTexto,
        BinarioLlave,
        BinarioCypher,
    ) = GenerarCypherConLlaveDinamica(TextoOriginal)

    if TextoMinusculas == "" and LlaveDinamica == "":
        print("\nNo se ingreso texto. No se genero cypher.")
        return

    print("\nTexto original en minusculas:")
    print(TextoMinusculas)
    print("\nLlave dinamica generada em ASCII, misma longitud que el texto:")
    print(LlaveDinamica)
    print("\nTexto en binario ASCII (8 bits por caracter):")
    print(BinarioTexto)
    print("\nLlave dinamica en binario ASCII (8 bits por caracter):")
    print(BinarioLlave)
    print("\nCypher en binario (resultado de XOR bit a bit):")
    print(BinarioCypher)
    print("\nCypher en ASCII (resultado final):")
    print(CypherAscii)
    print("\nel cypher y la llave pueden contener simbolos o caracteres no legibles,")
    print("porque son resultados directos de XOR y de ASCII aleatorio.")


# Punto de entrada del programa
if __name__ == "__main__":
    Main()
