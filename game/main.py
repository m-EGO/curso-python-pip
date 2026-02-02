import random


OPCIONES = ("piedra", "papel", "tijera")


def elegir_computadora() -> str:
    return random.choice(OPCIONES)


def decidir_ganador(jugador: str, computadora: str) -> str:
    if jugador == computadora:
        return "empate"

    reglas = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel",
    }
    if reglas[jugador] == computadora:
        return "jugador"
    return "computadora"


def pedir_jugada() -> str:
    while True:
        jugada = input("Elige piedra, papel o tijera (o 'salir'): ").strip().lower()
        if jugada == "salir":
            return jugada
        if jugada in OPCIONES:
            return jugada
        print("Entrada no válida. Intenta de nuevo.")


def jugar() -> None:
    victorias_jugador = 0
    victorias_computadora = 0
    empates = 0

    print("=== Piedra, Papel o Tijera ===")
    while True:
        jugador = pedir_jugada()
        if jugador == "salir":
            break

        computadora = elegir_computadora()
        resultado = decidir_ganador(jugador, computadora)

        print(f"Tú: {jugador} | Computadora: {computadora}")

        if resultado == "jugador":
            victorias_jugador += 1
            print("Ganaste esta ronda.")
        elif resultado == "computadora":
            victorias_computadora += 1
            print("La computadora ganó esta ronda.")
        else:
            empates += 1
            print("Empate.")

        print(
            f"Marcador -> Tú: {victorias_jugador} | "
            f"Computadora: {victorias_computadora} | Empates: {empates}\n"
        )

    print("\n¡Gracias por jugar!")
    print(
        f"Resultado final -> Tú: {victorias_jugador} | "
        f"Computadora: {victorias_computadora} | Empates: {empates}"
    )


if __name__ == "__main__":
    jugar()
