import random
import string

def generate_password(length=12, include_symbols=True, include_numbers=True):
    characters = string.ascii_letters  # Incluye letras mayúsculas y minúsculas
    if include_numbers:
        characters += string.digits  # Incluye dígitos (0-9)
    if include_symbols:
        characters += string.punctuation  # Incluye caracteres especiales (!, @, #, etc.)
    
    # Genera la contraseña aleatoria
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Entrada del usuario para personalizar la contraseña
length = int(input("Ingresa la longitud de la contraseña (recomendado: 12): "))
include_symbols = input("¿Incluir símbolos? (S/N): ").lower() == 's'
include_numbers = input("¿Incluir números? (S/N): ").lower() == 's'

# Generar la contraseña y mostrarla
password = generate_password(length, include_symbols, include_numbers)
print(f"Contraseña segura generada: {password}")
