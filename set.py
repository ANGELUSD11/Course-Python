my_set = set()

my_dictionary = {}
print(type(my_set))
print(type(my_dictionary))

my_dictionary = {"Angel", "Hernandez", 17}
print(type(my_dictionary))
my_dictionary = {"Angel": 17,
                 "ciudad": "Paipa",
                 "estatura": 180}
print(type(my_dictionary))

#si se modifica la sintaxis de un diccionario, se convierte en un set()

my_dictionary = set()
print(type(my_dictionary))

values = {"a", "b", 1}
print(len(values))

ages = ["a", "b", 2]
print(ages[0])

values.add("Angel")
print(values)

ages.append("Leo")
print(ages)

set_1 = set([1, 2, 3, 4])
print(type(set_1))