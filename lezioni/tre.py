def sum(a, b):
    return a + b

mySet = {"apple", "banana", "cherry"}

for x in mySet:
    print(x)
print("-----")
mySet.add("mango")

for x in mySet:
    print(x)

mySet.remove("apple")

print(mySet)

stuff = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

print(stuff.items())
print(stuff.keys())
print(stuff.values())


