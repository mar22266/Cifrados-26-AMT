# codigo para cifrar y descifrar usando el cifrado Cesar


# se normaliza el desplazamiento al rango 0 a 25 es decir se usa diccionario ingles
def NormalizarDesplazamiento(Desplazamiento):
    DesplazamientoNormalizado = Desplazamiento % 26
    return DesplazamientoNormalizado


# Se cifra un solo caracter usando el desplazamiento dado
def CifrarCaracterCesar(Caracter, DesplazamientoNormalizado):
    CodigoAscii = ord(Caracter)

    # a a la z en ascii
    CodigoA = ord("a")
    CodigoZ = ord("z")

    # si no es letra se devuelve igual
    if CodigoAscii < CodigoA or CodigoAscii > CodigoZ:
        return Caracter

    # pos de la leyta
    Posicion = CodigoAscii - CodigoA

    # desplazamiento aplicar
    PosicionCifrada = (Posicion + DesplazamientoNormalizado) % 26

    # se aplica el cifrado y s eobtiene
    CodigoCifrado = CodigoA + PosicionCifrada

    CaracterCifrado = chr(CodigoCifrado)
    return CaracterCifrado


# Funcion que descifra un solo caracter usando el desplazamiento dado
def DescifrarCaracterCesar(Caracter, DesplazamientoNormalizado):
    CodigoAscii = ord(Caracter)

    CodigoA = ord("a")
    CodigoZ = ord("z")

    if CodigoAscii < CodigoA or CodigoAscii > CodigoZ:
        return Caracter

    # pos de la letra
    Posicion = CodigoAscii - CodigoA

    # se hace el desplazamiento inverso
    PosicionDescifrada = (Posicion - DesplazamientoNormalizado) % 26

    # se obtiene el codigo descifrado
    CodigoDescifrado = CodigoA + PosicionDescifrada
    CaracterDescifrado = chr(CodigoDescifrado)
    return CaracterDescifrado


# Se cifra el mensaje completo usando cifrado Cesar
def CifrarCesar(MensajeOriginal, Desplazamiento):

    MensajeMinusculas = MensajeOriginal.lower()

    # Se normaliza el desplazamiento
    DesplazamientoNormalizado = NormalizarDesplazamiento(Desplazamiento)

    # string para guardar el mensaje cifrado
    MensajeCifrado = ""

    # recorrer el mensaje caracter por caracter
    Indice = 0
    Longitud = len(MensajeMinusculas)
    while Indice < Longitud:
        Caracter = MensajeMinusculas[Indice]

        # se cifra el caracter si es letra y se va construyendo el mensaje cifrado
        CaracterCifrado = CifrarCaracterCesar(Caracter, DesplazamientoNormalizado)
        MensajeCifrado = MensajeCifrado + CaracterCifrado
        Indice = Indice + 1

    return MensajeCifrado


# procesos para descifrar el mensaje cifrado usando cifrado Cesar
def DescifrarCesar(MensajeCifrado, Desplazamiento):
    MensajeMinusculas = MensajeCifrado.lower()
    DesplazamientoNormalizado = NormalizarDesplazamiento(Desplazamiento)
    MensajeDescifrado = ""
    Indice = 0
    Longitud = len(MensajeMinusculas)

    # se recorre el mensaje caracter por caracter aplicando proceso inverso
    while Indice < Longitud:
        Caracter = MensajeMinusculas[Indice]
        CaracterDescifrado = DescifrarCaracterCesar(Caracter, DesplazamientoNormalizado)
        MensajeDescifrado = MensajeDescifrado + CaracterDescifrado
        Indice = Indice + 1

    return MensajeDescifrado


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Cifrado Cesar ASCII en abecedario ingles ===")
    print(
        "Se ignorara mayusculas todo se pasa a minusculas y los caracteres que no sean letras se dejan sin cambio\n"
    )

    MensajeUsuario = input("Escribe el mensaje: ")
    TextoDesplazamiento = input("Escribe el desplazamiento entero puede ser negativo: ")

    try:
        Desplazamiento = int(TextoDesplazamiento)
    except ValueError:
        Desplazamiento = 3
        print("\nDesplazamiento no valido. Se usara desplazamiento por defecto = 3.")

    MensajeCifrado = CifrarCesar(MensajeUsuario, Desplazamiento)
    MensajeDescifrado = DescifrarCesar(MensajeCifrado, Desplazamiento)

    print("\nMensaje original en minusculas:")
    print(MensajeUsuario.lower())
    print("\nMensaje CIFRADO (Cesar):")
    print(MensajeCifrado)
    print("\nMensaje DESCIFRADO (usando el mismo desplazamiento):")
    print(MensajeDescifrado)


# Punto de entrada del programa
if __name__ == "__main__":
    Main()
