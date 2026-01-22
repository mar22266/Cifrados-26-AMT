# convierte el texto en base64 a ascii en minusculas pasando por binario

import base64


# funcion tomada del archivo ascii bin
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


# convierte bin a entero, funcion igual a la de bin a base 64 achivo
def ConvertirBinario8BitsAEntero(TokenBinario):
    ValorEntero = 0

    for CaracterBit in TokenBinario:
        BitEntero = ord(CaracterBit) - ord("0")
        ValorEntero = (ValorEntero * 2) + BitEntero

    return ValorEntero


# Funcion convierte tex a minuscula de bin a ascii
def ConvertirTextoABinarioAscii(TextoAsciiMinusculas):
    # cadena para almacenar el resultado
    ResultadoBinario = ""

    # Se recorre cada caracter
    for Caracter in TextoAsciiMinusculas:
        CodigoAscii = ord(Caracter)
        Binario8Bits = ConvertirEnteroABinario8Bits(CodigoAscii)

        # se agrega espacio si no es del primer grupo
        if ResultadoBinario != "":
            ResultadoBinario = ResultadoBinario + " "

        # Agregar los 8 bits al resultado
        ResultadoBinario = ResultadoBinario + Binario8Bits

    return ResultadoBinario


# misma funcion tomada del archivo bin a ascii
def ConvertirBinarioAAscii(CadenaBinaria):
    TextoAscii = ""
    TokenBinario = ""

    for Caracter in CadenaBinaria:
        if Caracter == "0" or Caracter == "1":
            TokenBinario = TokenBinario + Caracter
        else:
            if TokenBinario != "":
                CodigoAscii = ConvertirBinario8BitsAEntero(TokenBinario)
                CaracterAscii = chr(CodigoAscii)
                TextoAscii = TextoAscii + CaracterAscii
                TokenBinario = ""

    if TokenBinario != "":
        CodigoAscii = ConvertirBinario8BitsAEntero(TokenBinario)
        CaracterAscii = chr(CodigoAscii)
        TextoAscii = TextoAscii + CaracterAscii

    TextoMinusculas = TextoAscii.lower()

    return TextoMinusculas


# Convierte base64 a ascii en minusculas pasando por binario
def ConvertirBase64AAscii(TextoBase64):

    # Limpiar espacios en los extremos
    TextoBase64Limpio = TextoBase64.strip()
    TextoBase64Bytes = TextoBase64Limpio.encode("utf-8")
    TextoDecodificadoBytes = base64.b64decode(TextoBase64Bytes)
    TextoDecodificado = TextoDecodificadoBytes.decode("utf-8")
    TextoMinusculas = TextoDecodificado.lower()

    # Se convierte el texto en minusculas a binario
    TextoEnBinario = ConvertirTextoABinarioAscii(TextoMinusculas)

    # se convierte ese binario de nuevo a ASCII
    TextoReconstruido = ConvertirBinarioAAscii(TextoEnBinario)

    return TextoMinusculas, TextoEnBinario, TextoReconstruido


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Conversor de BASE64 a ASCII ===")

    TextoBase64Usuario = input("Escribe el texto en BASE64: ")
    TextoMinusculas, TextoBinarioAscii, TextoReconstruido = ConvertirBase64AAscii(
        TextoBase64Usuario
    )

    print("\nTexto decodificado en minusculas (desde BASE64):")
    print(TextoMinusculas)
    print("\nTexto en binario ASCII (8 bits por caracter):")
    print(TextoBinarioAscii)
    print("\nTexto reconstruido desde el binario (en minusculas):")
    print(TextoReconstruido)


# llamada a la funcion principal
if __name__ == "__main__":
    Main()
