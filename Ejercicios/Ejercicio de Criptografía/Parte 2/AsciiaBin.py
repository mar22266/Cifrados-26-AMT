# Codigo conbertir texto a binario ASCII en minusculas


# convierte textoa minusculas y luego se crea cadena para binario
def ConvertirTextoABinario(TextoOriginal):
    TextoMinusculas = TextoOriginal.lower()
    ResultadoBinario = ""

    # Recorrer caracter x caracter y obtiene ascii, convierte a binario y agrega un espacio si no es el primero y luego se agrega al resultado
    for Caracter in TextoMinusculas:
        CodigoAscii = ord(Caracter)
        Binario8Bits = format(CodigoAscii, "08b")
        if ResultadoBinario != "":
            ResultadoBinario += " "
        ResultadoBinario += Binario8Bits

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
