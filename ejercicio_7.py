string = input("Introduce una frase para invertirla: ")
string_reversed = ""

for variable in string:
    string_reversed = variable + string_reversed

print(f"string invertido: {string_reversed}")
