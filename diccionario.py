#diccionario vacio

dictionary_empty = {}

print(f"diccionario vacio {dictionary_empty}")
print()

#diccionario homogenero
dictionary_ages = {"Juan": 32,
                   "Mateo": 21,
                   "Luisardo": 25
                   }
print(f"Diccionario de edades {dictionary_ages}")
print()

dictionary_dates = {"name": "Brenda",
                    "last_name": "Flores",
                    "age": 22
                    }
print(f"Diccionario de datos {dictionary_dates}")
print()

#diccionario que almacene listas y diccionarios
dictionary_list = {"a": {"a": 1},
                   "b": [0, 1, 2]}
print(f"Diccionario con lista y diccionario {dictionary_list}")
print()

#los diccionarios tambien pueden tener claves numericas

dictionary_number = {11: 1,
                     5: 2,
                     6: 3
                     }
print(f"Diccionario con claves numericas {dictionary_number}")
print()

#un diccionario no puede tener claves repetidas
#no es recomendable utilizar claves de distinto tipo en un mismo diccionario

dictionary_mix = {1: 23,
                  "Juan": 5,
                  -2: "hello"
                  }
print(f"diccionario con claves de distintos tipos de dato {dictionary_mix}")

#diccionario desde teclado
dictionary = {}
while True:
    key = int(input("Escriba un número distinto a 0: "))
    if key == 0:
        break
    value = input("Escribe tu nombre: ")
    dictionary[key] = value
    print(dictionary)
    break

#diccionario con clave
dictionary_pass = {}
while True:
    key = int(input("Escriba la clave numerica para continuar: "))
    if key != 17:
        print("Clave incorrecta")
        break
    else:
        value = input("Escriba su nombre: ")
        if value != "Angel":
            print("Acceso denegado")
            break
        else:
            dictionary_pass[key] = value
            print("Acceso concedido")
            print(dictionary_pass)
            break