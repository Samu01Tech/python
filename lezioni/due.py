lista = ["apple", "banana", "cherry"]

print(lista)
print(lista[0])
print(lista[-1])

print(len(lista))

if "apple" in lista:
    print("apple esiste")

# lista += ["mango"]
lista.append("mango")

print(lista)

lista.insert(1, "strawberry")

print(lista)

lista.remove("banana")

print(lista)

lista.pop()

print(lista)

lista.pop(0)

print(lista)

for i in range(len(lista)):
    print("Elemento" + str(i) + ":" + lista[i])

for element in lista:
    print(element)

lettere = ["c", "a", "e", "b", "d"]
lettere.sort()

print(lettere)

lettere.reverse()

print(lettere)
