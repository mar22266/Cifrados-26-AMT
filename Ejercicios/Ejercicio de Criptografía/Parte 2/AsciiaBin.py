# Codigo conbertir texto a binario ASCII en minusculas


# cinvertir ascii a bin 8 bits usando divisiones y modulos
def ConvertirEnteroABinario8Bits(CodigoAscii):
    Binario8Bits = ""
    # se empieza desde el bit mas siginificativo
    Potencia = 7
    while Potencia >= 0:
        # Se calcula el valor de la potencia de 2
        ValorBit = 2**Potencia

        # Se agarra el valor del bit usando division entera si ascii es mayor o igual al valor de este bit entonces el bit es 1
        Bit = CodigoAscii // ValorBit

        # bit es 1 se resta ese valor al codigo para seguir
        if Bit == 1:
            CodigoAscii = CodigoAscii - ValorBit
            Binario8Bits = Binario8Bits + "1"
        else:
            Binario8Bits = Binario8Bits + "0"

        # se pasa al siguiente bit
        Potencia = Potencia - 1

    return Binario8Bits


# convierte texto a minusculas y luego se crea cadena para binario
def ConvertirTextoABinario(TextoOriginal):
    TextoMinusculas = TextoOriginal.lower()

    ResultadoBinario = ""

    # recorrer cada caracter y convierte asccii a bin
    for Caracter in TextoMinusculas:
        CodigoAscii = ord(Caracter)
        Binario8Bits = ConvertirEnteroABinario8Bits(CodigoAscii)
        if ResultadoBinario != "":
            ResultadoBinario = ResultadoBinario + " "

        # Agregar los 8 bits al resultado
        ResultadoBinario = ResultadoBinario + Binario8Bits

    return TextoMinusculas, ResultadoBinario


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Conversor ASCII A BINARIO en minusculas ===")
    TextoUsuario = input("Escribe una palabra o frase: ")

    TextoMinusculas, TextoEnBinario = ConvertirTextoABinario(TextoUsuario)

    print("\nTexto en minusculas:")
    print(TextoMinusculas)

    print("\nTexto en binario ASCII, 8 bits por caracter:")
    print(TextoEnBinario)


# llamada a la funcion principal
if __name__ == "__main__":
    Main()
