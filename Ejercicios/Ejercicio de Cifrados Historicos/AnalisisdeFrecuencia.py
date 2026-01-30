# codigo que analiza la frec de los carc en min alfabeto a-z


# funcion que realiza el analisis de frecuencia en minusculas
def AnalisisFrecuencia(MensajeOriginal):
    MensajeMinusculas = MensajeOriginal.lower()

    # dicc que guarda las frecuencias de cada letra
    Frecuencias = {}
    TotalLetras = 0

    # se recorre cada caracter del mensaje en minusculas
    for Caracter in MensajeMinusculas:
        # solo letras de la a a la z y si no esta se inicializa en 0
        if Caracter >= "a" and Caracter <= "z":
            if Caracter not in Frecuencias:
                Frecuencias[Caracter] = 0

            # sino se aumenta su conteo
            Frecuencias[Caracter] = Frecuencias[Caracter] + 1

            # se aumenta el total de letras
            TotalLetras = TotalLetras + 1

    # tabla de frecuencias ayuda con chatgpt para formateo
    TablaFrecuencia = ""
    TablaFrecuencia = TablaFrecuencia + "CARACTER | CONTEO | PORCENTAJE\n"
    TablaFrecuencia = TablaFrecuencia + "-------- | ------ | ----------\n"

    # si no hay tabla se devuelve vacia
    if TotalLetras == 0:
        return MensajeMinusculas, TablaFrecuencia

    # ordenar letras por frec alfabeticamente
    LetrasOrdenadas = sorted(Frecuencias.items(), key=lambda Par: (-Par[1], Par[0]))

    # se recorren pero ordenadas x frec
    for Par in LetrasOrdenadas:
        Letra = Par[0]
        Conteo = Par[1]

        # calculo del porcentaje y formateo
        Porcentaje = (Conteo * 100.0) / TotalLetras
        TextoPorcentaje = "{:.2f}".format(Porcentaje)

        # se le agrega linea  a la tabla para formateo visual
        Linea = (
            Letra + "        | " + str(Conteo) + "      | " + TextoPorcentaje + "%\n"
        )

        TablaFrecuencia = TablaFrecuencia + Linea

    return MensajeMinusculas, TablaFrecuencia


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Analisis de frecuencia a a la z alfabeto ingles===")
    MensajeUsuario = input("Escribe el mensaje a analizar: ")
    MensajeMinusculas, TablaFrecuencia = AnalisisFrecuencia(MensajeUsuario)
    print("\nMensaje en minusculas texto analizado:")
    print(MensajeMinusculas)
    print("\nTabla de frecuencia de caracteres:")
    print(TablaFrecuencia)


# Punto de entrada del programa
if __name__ == "__main__":
    Main()
