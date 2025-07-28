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

def jugar_una_partida(categorias):
    palabra, categoria = elegir_palabra_por_categoria(categorias)
    vidas = 6
    estado = ['_' for _ in palabra]
    letras_adivinadas = set()
    letras_incorrectas = []

    print(f"\nCategoría elegida: {categoria}")

    while vidas > 0 and '_' in estado:
        print("\nPalabra:", ' '.join(estado))
        print("Vidas restantes:", vidas)
        print("Letras incorrectas:", ', '.join(letras_incorrectas))
        letra = input("Ingresa una letra: ").strip().upper()

        if len(letra) != 1 or letra not in string.ascii_uppercase:
            print("Por favor, ingresa solo una letra válida.")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("Ya ingresaste esa letra.")
            continue

        if letra in palabra:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            letras_adivinadas.add(letra)
            for i, l in enumerate(palabra):
                if l == letra:
                    estado[i] = letra
        else:
            print(f"La letra '{letra}' no está en la palabra.")
            vidas -= 1
            letras_incorrectas.append(letra)

    if '_' not in estado:
        print(f"\n¡Felicidades! Adivinaste la palabra: {palabra}")
    else:
        print(f"\nPerdiste. La palabra era: {palabra}")

if __name__ == "__main__":
    categorias = {
        'Países': ['uruguay', 'argentina', 'brasil', 'canada', 'japon'],
        'Animales': ['elefante', 'jirafa', 'perro', 'gato', 'delfin'],
        'Colores': ['rojo', 'azul', 'verde', 'amarillo', 'violeta'],
        'Personajes históricos': ['napoleon', 'einstein', 'cleopatra', 'bolivar', 'mandela']
    }
    jugar_una_partida(categorias)