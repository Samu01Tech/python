def main():
    print("Hello, World!") # Hello, World!

    a = 10
    b = 20

    print(a + b) # 30

    print("Hello, " + "World!") # Hello, World!

    testo1 = f"Hello, {a}!"
    print(testo1) # Hello, 10!

    if(a > b):
        print("a is greater than b")
    elif (a == b):
        print("a is equal to b")
    else:
        print("a is not greater than b")
    
    print(a > b) # False

    c = 10

    print(a == c) # True



if __name__ == "__main__":
    main()