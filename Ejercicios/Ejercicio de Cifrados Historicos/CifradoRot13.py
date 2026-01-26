# codigo para cifrar usando el cifrado ROT13 sin duplicar codigo

from CifradoCesar import CifrarCesar


# funcion para ROT 13
def rot13(Mensaje):
    DesplazamientoRot13 = 13
    MensajeRot13 = CifrarCesar(Mensaje, DesplazamientoRot13)
    return MensajeRot13


# funcion principal se pide texto y se muestra resultado
def Main():
    print("=== Cifrado ROT13 ===")
    print("Se reutiliza la funcion CifrarCesar con desplazamiento fijo de 13.\n")
    MensajeUsuario = input("Escribe el mensaje: ")
    MensajeRot13 = rot13(MensajeUsuario)
    MensajeDobleRot13 = rot13(MensajeRot13)
    print("\nMensaje original en minusculas:")
    print(MensajeUsuario.lower())
    print("\nMensaje transformado con ROT13:")
    print(MensajeRot13)
    print("\nSi se aplica  ROT13 otra vez, se regresa al original:")
    print(MensajeDobleRot13)


# Punto de entrada del programa
if __name__ == "__main__":
    Main()
