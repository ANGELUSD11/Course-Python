frase = input("Escriba una frase: ")
palabra = input("Escriba una palabra que quiera eliminar de la frase: ")
substring = ""
indice = frase.find(palabra)
substring = frase[0 : indice] + frase[indice + len(palabra) + 1 : ]

print(f"Cadena resultante: {substring}")
