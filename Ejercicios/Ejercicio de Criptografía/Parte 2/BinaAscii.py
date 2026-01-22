# convierte de binario a asii


# convierte bin a entero, funcion igual a la de bin a base 64 achivo
def ConvertirBinario8BitsAEntero(TokenBinario):
    ValorEntero = 0

    for CaracterBit in TokenBinario:
        BitEntero = ord(CaracterBit) - ord("0")
        ValorEntero = (ValorEntero * 2) + BitEntero

    return ValorEntero


def ConvertirBinarioAAscii(CadenaBinaria):
    TextoAscii = ""

    # temporal para armando grupos de bits
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
    return TextoMinusculas


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Conversor de Binario a ASCII ===")
    print("Ingresa los bits en grupos de 8, separados por espacios.")

    CadenaBinariaUsuario = input("Escribe la cadena binaria: ")
    TextoResultado = ConvertirBinarioAAscii(CadenaBinariaUsuario)

    print("\nTexto reconstruido en minusculas desde el binario:")
    print(TextoResultado)


# llamada a la funcion principal
if __name__ == "__main__":
    Main()
