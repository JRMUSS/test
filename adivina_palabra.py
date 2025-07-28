import random
import string

def elegir_palabra_por_categoria(categorias):
    """Permite al jugador elegir una categoría y selecciona una palabra al azar."""
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

def inicializar_juego(palabra):
    """Prepara el estado inicial del juego."""
    vidas = 6
    letras_adivinadas = set()
    letras_incorrectas = []
    estado = ['_' for _ in palabra]
    return vidas, letras_adivinadas, letras_incorrectas, estado

def mostrar_estado(estado, vidas, letras_incorrectas):
    """Imprime en pantalla el progreso del jugador."""
    print("\nPalabra: ", ' '.join(estado))
    print(f"Vidas restantes: {vidas}")
    print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")

def validar_letra(letra, usadas):
    """Valida que la entrada sea una letra no usada previamente."""
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
    vidas, adivinadas, incorrectas, estado = inicializar_juego(palabra)

    print(f"\nCategoría elegida: {categoria}")
    print(f"La palabra tiene {len(palabra)} letras.")

    while vidas > 0 and '_' in estado:
        mostrar_estado(estado, vidas, incorrectas)
        entrada = input("Ingresa una letra (o '!' para rendirte): ").strip()

        if entrada == '!':
            print("Has decidido rendirte. ¡Partida terminada!")
            print("Rendirse también es parte del juego. ¡Ánimo!")
            break

        letra = validar_letra(entrada, adivinadas.union(set(incorrectas)))
        if not letra:
            continue

        if letra in palabra:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            adivinadas.add(letra)
            nueva_estado = []
            for posicion in range(len(palabra)):
                if palabra[posicion] == letra:
                    nueva_estado.append(letra)
                else:
                    nueva_estado.append(estado[posicion])
            estado = nueva_estado
        else:
            print(f"La letra '{letra}' NO está en la palabra.")
            vidas -= 1
            incorrectas.append(letra)

    if '_' not in estado:
        print(f"\n¡Felicidades! ¡Adivinaste la palabra: {palabra}!")
    elif vidas == 0:
        print(f"\nHas perdido. La palabra era: {palabra}.")
        print("¡No te preocupes! Podés volver a intentarlo.")
    return

def main():
    categorias = {
        'Países': ['uruguay', 'argentina', 'brasil', 'canada', 'japon'],
        'Animales': ['elefante', 'jirafa', 'perro', 'gato', 'delfin'],
        'Colores': ['rojo', 'azul', 'verde', 'amarillo', 'violeta'],
        'Personajes históricos': ['napoleon', 'einstein', 'cleopatra', 'aristoteles', 'mandela']
    }

    print("===🔮🕹️✨✍🏼 ¡Bienvenido al juego 'Adivina la palabra' con categorías!✍🏼✨🕹️🔮 ===")

    while True:
        jugar_una_partida(categorias)
        otra = input("\n¿Deseas jugar otra vez? (S/N): ").strip().upper()
        if otra != 'S':
            print("¡Gracias por jugar! Hasta la próxima.")
            break

if __name__ == '__main__':
    main()

