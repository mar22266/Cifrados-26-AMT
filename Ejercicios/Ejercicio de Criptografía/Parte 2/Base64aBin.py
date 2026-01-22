# codigo convertir texto a base64 y luego a binario ASCII

import base64


# funcion base del archivo Ascii a bin
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


# convierte texto a minusculas, luego a bytes utf-8 se codifica en base64
def ConvertirTextoBase64ABinario(TextoOriginal):
    TextoMinusculas = TextoOriginal.lower()
    TextoEnBytes = TextoMinusculas.encode("utf-8")
    TextoBase64Bytes = base64.b64encode(TextoEnBytes)

    # Convertir base64 a texto
    TextoBase64 = TextoBase64Bytes.decode("utf-8")

    # string acumula resultado
    ResultadoBinario = ""

    # Recorre caracter y obtiene ascii, convierte a binario 8 bits y agrega al resultado
    for Caracter in TextoBase64:
        CodigoAscii = ord(Caracter)
        Binario8Bits = ConvertirEnteroABinario8Bits(CodigoAscii)

        if ResultadoBinario != "":
            ResultadoBinario = ResultadoBinario + " "

        ResultadoBinario = ResultadoBinario + Binario8Bits

    return TextoMinusculas, TextoBase64, ResultadoBinario


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Conversor Base64 A Binario en minusculas ===")
    TextoUsuario = input("Escribe una palabra o frase: ")

    TextoMinusculas, TextoBase64, TextoBinario = ConvertirTextoBase64ABinario(
        TextoUsuario
    )

    print("\nTexto en minusculas:")
    print(TextoMinusculas)
    print("\nTexto codificado en BASE64:")
    print(TextoBase64)
    print("\nTexto BASE64 en binario (ASCII, 8 bits por caracter):")
    print(TextoBinario)


# llamada a la funcion principal
if __name__ == "__main__":
    Main()
