# codigo convertir texto a base64 y luego a binario ASCII

import base64


# convierte texto a minusculas, luego a bytes utf-8 se codifica en base64 da resultado bytes
# luego se convierte el base64 a texto y se crea cadena para binario
def ConvertirTextoBase64ABinario(TextoOriginal):
    TextoMinusculas = TextoOriginal.lower()
    TextoEnBytes = TextoMinusculas.encode("utf-8")
    TextoBase64Bytes = base64.b64encode(TextoEnBytes)
    TextoBase64 = TextoBase64Bytes.decode("utf-8")
    ResultadoBinario = ""

    # Recorrer cada caracter ibtiene el ascii, convierte ascii a binario de 8 bits y agrega espacio si no es el primero y agrega el bin al resultado
    for Caracter in TextoBase64:
        CodigoAscii = ord(Caracter)
        Binario8Bits = format(CodigoAscii, "08b")
        if ResultadoBinario != "":
            ResultadoBinario += " "
        ResultadoBinario += Binario8Bits

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
