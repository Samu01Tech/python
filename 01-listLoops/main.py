def mySort(n):
  return abs(n - 50)

def main():
    lista = ["apple", "banana", "cherry"]

    if "apple" in lista:
        print("Yes, 'apple' is in the fruits list")

    lista += ["orange"]
    lista.append("mango")

    print(lista)

    lista.insert(1, "strawberry")

    print(lista)

    lista.remove("banana")
    lista.pop()

    print(lista)

    for element in lista:
        print(element)

    for i in range(len(lista)):
        print("Elemento" + str(i) + ":" + lista[i])


    lettere = ["c", "a", "e", "b", "d"]
    lettere.sort()

    print(lettere)

    lettere.reverse()

    print(lettere)

    numeri = [100, 50, 65, 82, 23]
    numeri.sort()

    print(numeri)

    numeri = [100, 50, 65, 82, 23]
    numeri.sort(key = mySort)

    print(numeri)

if __name__ == "__main__":
    main()