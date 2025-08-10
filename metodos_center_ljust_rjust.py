string = "menu"

print("metodos con espacios: ")

print(string.center(20))
print(string.ljust(20))
print(string.rjust(20))

print("\nmetodos con caracter")
print(string.center(20, "*"))
print(string.ljust(20, "*"))
print(string.rjust(20, "*"))

print("\nvariable modificada: ")

string = string.center(10, "*")
print(string)
