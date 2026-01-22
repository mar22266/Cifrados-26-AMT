# codigo convertir Binario a base64

import base64


# cinvierte bits a un entero
def ConvertirBinario8BitsAEntero(TokenBinario):
    ValorEntero = 0

    # Se recorre de izquierda a drecha cada bit del token de 8 bits
    for CaracterBit in TokenBinario:
        BitEntero = ord(CaracterBit) - ord("0")
        # Se desplaza el valor actual un bit a la izquierda multiplicar por 2 y sumamos el bit actual
        ValorEntero = (ValorEntero * 2) + BitEntero

    return ValorEntero


# cadena de bits recibe
def ConvertirBinarioABase64(CadenaBinaria):
    # Se reconstruye el texto ASCII a partir del binario
    TextoAscii = ""

    # temporal para ir armando cada grupo de 8 bits
    TokenBinario = ""

    # Recorrer caracter
    for Caracter in CadenaBinaria:
        # Si es un bit valido se agrega
        if Caracter == "0" or Caracter == "1":
            TokenBinario = TokenBinario + Caracter
        else:
            # si se tiene un separador y hays bits acumulados, se convierte ese grupo de bits a un caracter ASCII
            if TokenBinario != "":
                # Convertir el grupo de bits a entero
                CodigoAscii = ConvertirBinario8BitsAEntero(TokenBinario)

                # numero entero a caracter ASCII
                CaracterAscii = chr(CodigoAscii)
                TextoAscii = TextoAscii + CaracterAscii
                TokenBinario = ""

    # si quedo un token pendiente se procesa
    if TokenBinario != "":
        CodigoAscii = ConvertirBinario8BitsAEntero(TokenBinario)
        CaracterAscii = chr(CodigoAscii)
        TextoAscii = TextoAscii + CaracterAscii

    TextoMinusculas = TextoAscii.lower()
    TextoBytes = TextoMinusculas.encode("utf-8")
    TextoBase64Bytes = base64.b64encode(TextoBytes)
    TextoBase64 = TextoBase64Bytes.decode("utf-8")

    return TextoMinusculas, TextoBase64


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Conversor de Binario a BASE64 ===")
    print("Ingresa los bits en grupos de 8, separados por espacios.")

    CadenaBinariaUsuario = input("Escribe la cadena binaria: ")
    TextoMinusculas, TextoBase64 = ConvertirBinarioABase64(CadenaBinariaUsuario)

    print("\nTexto reconstruido en minusculas:")
    print(TextoMinusculas)
    print("\nTexto en BASE64:")
    print(TextoBase64)


# llamada a la funcion principal
if __name__ == "__main__":
    Main()
