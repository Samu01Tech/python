def main():
    # dictionaries
    stuff = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    # ordered, mutable, no duplicates

    print(stuff.items())
    print(stuff.keys())
    print(stuff.values())

    for key in stuff:
        print(key + ":" + str(stuff[key]))

    if "name" in stuff:
        print("Yes, 'name' is one of the keys in the stuff dictionary")

    if "John" in stuff.values():
        print("Yes, 'John' is one of the values in the stuff dictionary")

    # sets
    # unordered, mutable, no duplicates
    mySet = {"apple", "banana", "cherry"}

    for x in mySet:
        print(x)
    
    mySet.add("apple")

    print(mySet)

    mySet.update(["orange", "mango", "grapes"])

    print(mySet)

    mySet.remove("banana")

    print(mySet)

    

if __name__ == "__main__":
    main()