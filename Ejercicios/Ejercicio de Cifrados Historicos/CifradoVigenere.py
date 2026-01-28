# codigo para cifrar y descifrar usando el cifrado Vigenere


# funcion reutilizada de otro script
def NormalizarDesplazamiento(Desplazamiento):
    DesplazamientoNormalizado = Desplazamiento % 26
    return DesplazamientoNormalizado


# de igual funcion reutilizada de otro script
def CifrarCaracterCesar(Caracter, DesplazamientoNormalizado):
    CodigoAscii = ord(Caracter)
    CodigoA = ord("a")
    CodigoZ = ord("z")
    if CodigoAscii < CodigoA or CodigoAscii > CodigoZ:
        return Caracter
    Posicion = CodigoAscii - CodigoA
    PosicionCifrada = (Posicion + DesplazamientoNormalizado) % 26
    CodigoCifrado = CodigoA + PosicionCifrada
    CaracterCifrado = chr(CodigoCifrado)

    return CaracterCifrado


# funcion reutilizada de otro script
def DescifrarCaracterCesar(Caracter, DesplazamientoNormalizado):
    CodigoAscii = ord(Caracter)
    CodigoA = ord("a")
    CodigoZ = ord("z")
    if CodigoAscii < CodigoA or CodigoAscii > CodigoZ:
        return Caracter
    Posicion = CodigoAscii - CodigoA
    PosicionDescifrada = (Posicion - DesplazamientoNormalizado) % 26
    CodigoDescifrado = CodigoA + PosicionDescifrada
    CaracterDescifrado = chr(CodigoDescifrado)

    return CaracterDescifrado


# funcion para limpiar la clave alfabetica
def LimpiarClaveAlfabetica(ClaveOriginal):
    ClaveMinusculas = ClaveOriginal.lower()
    ClaveLimpia = ""
    Indice = 0
    Longitud = len(ClaveMinusculas)

    while Indice < Longitud:
        Caracter = ClaveMinusculas[Indice]
        if Caracter >= "a" and Caracter <= "z":
            ClaveLimpia = ClaveLimpia + Caracter
        Indice = Indice + 1

    return ClaveLimpia


# funcion que cifra el sms x vigenere usa clave alfabetica que se repite
# se uso chatgpt para ayudar a escribir esta funcion
def CifrarVigenere(MensajeOriginal, ClaveOriginal):
    MensajeMinusculas = MensajeOriginal.lower()
    ClaveLimpia = LimpiarClaveAlfabetica(ClaveOriginal)

    # no clave no se cifra nada
    if ClaveLimpia == "":
        return MensajeMinusculas

    MensajeCifrado = ""
    LongitudMensaje = len(MensajeMinusculas)
    LongitudClave = len(ClaveLimpia)
    IndiceMensaje = 0
    IndiceClave = 0

    # se recorre todo el mensaje cifrando letra a letra
    while IndiceMensaje < LongitudMensaje:
        CaracterMensaje = MensajeMinusculas[IndiceMensaje]

        # no es a a la z se copia igual y no avanza clave
        if CaracterMensaje < "a" or CaracterMensaje > "z":
            MensajeCifrado = MensajeCifrado + CaracterMensaje
        else:
            CaracterClave = ClaveLimpia[IndiceClave]

            # El desplazamiento es la posicion de la letra de la clave
            Desplazamiento = ord(CaracterClave) - ord("a")
            DesplazamientoNormalizado = NormalizarDesplazamiento(Desplazamiento)

            # se cifra este caracter del mensaje con ese desplazamiento
            CaracterCifrado = CifrarCaracterCesar(
                CaracterMensaje, DesplazamientoNormalizado
            )

            MensajeCifrado = MensajeCifrado + CaracterCifrado

            # se avanaza la clave solo al procesar letras
            IndiceClave = IndiceClave + 1
            if IndiceClave == LongitudClave:
                IndiceClave = 0

        IndiceMensaje = IndiceMensaje + 1

    return MensajeCifrado


# funcion inversa que decifra el sms x vigenere usa clave alfabetica que se repite
# se uso chatgpt para ayudar a escribir esta funcion
def DescifrarVigenere(MensajeCifrado, ClaveOriginal):
    MensajeMinusculas = MensajeCifrado.lower()
    ClaveLimpia = LimpiarClaveAlfabetica(ClaveOriginal)

    if ClaveLimpia == "":
        return MensajeMinusculas
    MensajeDescifrado = ""
    LongitudMensaje = len(MensajeMinusculas)
    LongitudClave = len(ClaveLimpia)
    IndiceMensaje = 0
    IndiceClave = 0

    # se recorre todo el mensaje descifrando letra a letra usa misma logica que cifrar solo que inversa
    while IndiceMensaje < LongitudMensaje:
        CaracterMensaje = MensajeMinusculas[IndiceMensaje]

        if CaracterMensaje < "a" or CaracterMensaje > "z":
            MensajeDescifrado = MensajeDescifrado + CaracterMensaje
        else:
            CaracterClave = ClaveLimpia[IndiceClave]
            Desplazamiento = ord(CaracterClave) - ord("a")
            DesplazamientoNormalizado = NormalizarDesplazamiento(Desplazamiento)
            CaracterDescifrado = DescifrarCaracterCesar(
                CaracterMensaje, DesplazamientoNormalizado
            )
            MensajeDescifrado = MensajeDescifrado + CaracterDescifrado
            IndiceClave = IndiceClave + 1
            if IndiceClave == LongitudClave:
                IndiceClave = 0
        IndiceMensaje = IndiceMensaje + 1

    return MensajeDescifrado


# funcion principal se pide texto y se muestra resultado
def Main():
    # Mensaje inicial
    print("=== Cifrado Vigenere con clave alfabetica ===")
    print("Solo se cifran letras a-z.")
    print("La clave se limpia para usar solo letras a-z\n")

    MensajeUsuario = input("Escribe el mensaje: ")
    ClaveUsuario = input("Escribe la clave alfabetica: ")
    MensajeCifrado = CifrarVigenere(MensajeUsuario, ClaveUsuario)
    MensajeDescifrado = DescifrarVigenere(MensajeCifrado, ClaveUsuario)
    print("\nMensaje original en minusculas:")
    print(MensajeUsuario.lower())

    print("\nClave limpia en minusculas solo letras a-z:")
    print(LimpiarClaveAlfabetica(ClaveUsuario))

    print("\nMensaje cifrado Vigenere:")
    print(MensajeCifrado)

    print("\nMensaje descifrado usando la misma clave:")
    print(MensajeDescifrado)


# Punto de entrada del programa
if __name__ == "__main__":
    Main()
