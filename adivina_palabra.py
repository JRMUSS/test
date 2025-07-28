import random
import string

def elegir_palabra_por_categoria(categorias):
    print("\nCategorías disponibles:")
    for i, categoria in enumerate(categorias.keys(), start=1):
        print(f"{i}. {categoria}")
    
    while True:
        opcion = input("\nElige una categoría ingresando su número: ").strip()
        if opcion.isdigit():
            indice = int(opcion) - 1
            if 0 <= indice < len(categorias):
                categoria = list(categorias.keys())[indice]
                return random.choice(categorias[categoria]).upper(), categoria
        print("Opción inválida. Intenta nuevamente.")

def mostrar_estado(estado, vidas, letras_incorrectas):
    print("\nPalabra:", ' '.join(estado))
    print(f"Vidas restantes: {vidas}")
    print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")

def validar_letra(letra, usadas):
    letra = letra.upper()
    if len(letra) != 1:
        print("Por favor ingresa solo UNA letra.")
        return None
    if letra not in string.ascii_uppercase:
        print("Eso no es una letra válida.")
        return None
    if letra in usadas:
        print("Ya ingresaste esa letra. Intenta con otra.")
        return None
    return letra

def jugar_una_partida(categorias):
    palabra, categoria = elegir_palabra_por_categoria(categorias)
    vidas = 6
    estado = ['_' for _ in palabra]
    letras_adivinadas = set()
    letras_incorrectas = []

    print(f"\nCategoría elegida: {categoria}")

    while vidas > 0 and '_' in estado:
        mostrar_estado(estado, vidas, letras_incorrectas)
        entrada = input("Ingresa una letra (o '!' para rendirte): ").strip()

        if entrada == '!':
            print("Has decidido rendirte. ¡Partida terminada!")
            return False  # para no seguir jugando si se rinde

        letra = validar_letra(entrada, letras_adivinadas.union(set(letras_incorrectas)))
        if not letra:
            continue

        if letra in palabra:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            letras_adivinadas.add(letra)
            for i, l in enumerate(palabra):
                if l == letra:
                    estado[i] = letra
        else:
            print(f"La letra '{letra}' NO está en la palabra.")
            vidas -= 1
            letras_incorrectas.append(letra)

    if '_' not in estado:
        print(f"\n¡Felicidades! ¡Adivinaste la palabra: {palabra}!")
    else:
        print(f"\nHas perdido. La palabra era: {palabra}.")

    return True  # para seguir jugando

def main():
    categorias = {
        'Países': ['uruguay', 'argentina', 'brasil', 'canada', 'japon'],
        'Animales': ['elefante', 'jirafa', 'perro', 'gato', 'delfin'],
        'Colores': ['rojo', 'azul', 'verde', 'amarillo', 'violeta'],
        'Personajes históricos': ['napoleon', 'einstein', 'cleopatra', 'bolivar', 'mandela']
    }

    print("=== ¡Bienvenido al juego 'Adivina la palabra' con categorías! ===")

    while True:
        seguir = jugar_una_partida(categorias)
        if not seguir:
            break
        otra = input("\n¿Deseas jugar otra vez? (S/N): ").strip().upper()
        if otra != 'S':
            print("¡Gracias por jugar! Hasta la próxima.")
            break

if __name__ == '__main__':
    main()