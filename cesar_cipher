def cesar_cipher(texto, desplazamiento):
    # Inicializa una cadena vacía para almacenar el texto cifrado
    texto_cifrado = ""
    # Itera sobre cada carácter en el texto proporcionado
    for char in texto:
        # Verifica si el carácter es una letra del alfabeto
        if char.isalpha():
            # Si el carácter es una letra mayúscula
            if char.isupper():
                # Aplica el cifrado César para letras mayúsculas
                texto_cifrado += chr((ord(char) - 65 + desplazamiento) % 26 + 65)
            # Si el carácter es una letra minúscula
            elif char.islower():
                # Aplica el cifrado César para letras minúsculas
                texto_cifrado += chr((ord(char) - 97 + desplazamiento) % 26 + 97)
        else:
            # Si el carácter no es una letra del alfabeto, simplemente lo agrega al texto cifrado
            texto_cifrado += char
    # Retorna el texto cifrado
    return texto_cifrado

# Texto de ejemplo a cifrar
texto = "Hola mundo"
# Valor de desplazamiento para el cifrado César
desplazamiento = 3
# Llama a la función cesar_cipher para cifrar el texto con el desplazamiento dado
texto_cifrado = cesar_cipher(texto, desplazamiento)
# Imprime el texto cifrado
print("Texto cifrado:", texto_cifrado)
