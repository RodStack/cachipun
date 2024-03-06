import random

choices = {
    1: "🪨",
    2: "🧻",
    3: "✂️"
}

print("Bienvenido al cachipun")

def main():
    while True:
        npc = generate_choice()
        print("Que quieres elegir?")
        print("1. 🪨")
        print("2. 🧻")
        print("3. ✂️")
        print("4. Dejar de jugar")
        selection = int(input("Seleccione una opción: "))
        if selection > 4:
            print("Error: elija una opción válida")
            continue
        elif selection == 4:
            break
        else:
            result = check_result(choices[selection], npc)
            print(result)

def generate_choice():
    number = random.randint(1, 3)
    return choices[number]

def check_result(player, npc):
    print()
    print(player, npc)
    if player == npc:
        print("Empate")
        main()
    elif player == "✂️" and npc == "🧻":
        return "Felicidades ganaste"
    elif player == "🧻" and npc == "🪨":
        return "Felicidades ganaste"
    elif player == "🪨" and npc == "✂️":
        return "Felicidades ganaste"
    else:
        return "Haz perdido"


if __name__ == "__main__":
    main()
