# genera llaves dinamicas con ascii

import random


# funcion tomada del ejercicio anterior de cripto para convertir a binario
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


# funcion tomada del eje de pasado convierte texto a binario ascii
def ConvertirTextoABinarioAscii(TextoAscii):
    ResultadoBinario = ""
    for Caracter in TextoAscii:
        CodigoAscii = ord(Caracter)
        Binario8Bits = ConvertirEnteroABinario8Bits(CodigoAscii)
        if ResultadoBinario != "":
            ResultadoBinario = ResultadoBinario + " "
        ResultadoBinario = ResultadoBinario + Binario8Bits
    return ResultadoBinario


# funcion para generar la llave dinamica
def GenerarLlaveDinamica(LongitudLlave):
    # String paara guardar llave
    Llave = ""

    Contador = 0
    while Contador < LongitudLlave:
        # Genera aleatorio entre 33 y 126 decision por chatgpt debido a que son solo se usan caracyeres visibles no tabs ni delete
        CodigoAscii = random.randint(33, 126)

        # se convierte cada codigo ascii a caracter
        Caracter = chr(CodigoAscii)

        # se le agrega el caracter a la llave
        Llave = Llave + Caracter
        Contador = Contador + 1

    return Llave


# funcion principal se pide texto y se muestra resultado
def Main():
    # Mensaje inicial para el usuario
    print("=== Genarador de llaves dinamicas con ASCII ===")
    print(
        "Se generara una llave aleatoria usando caracteres ASCII que sean visibles es decir imprimibles.\n"
    )
    TextoLongitud = input("Escribe la longitud de la llave en numero: ")

    # en caso el user ingrese algo no valido se usa valor por defecto que es 8 caracteres
    try:
        LongitudLlave = int(TextoLongitud)
    except ValueError:
        LongitudLlave = 8
        print("\nEntrada no valida. Se usara longitud por defecto de 8 caracteres.")

    if LongitudLlave <= 0:
        LongitudLlave = 8
        print(
            "\nLa longitud debe ser mayor que cero por eso se usara longitud de 8 caracteres."
        )

    LlaveGenerada = GenerarLlaveDinamica(LongitudLlave)
    LlaveEnBinario = ConvertirTextoABinarioAscii(LlaveGenerada)
    print("\nLlave dinamica generada (ASCII):")
    print(LlaveGenerada)
    print("\nLlave en binario ASCII (8 bits por caracter):")
    print(LlaveEnBinario)


# llamada a la funcion principal
if __name__ == "__main__":
    Main()
