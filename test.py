temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
except:
    fahr = -1

cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)





print("Hello, this is ", end="")
print("dog")


def f(a, b):
    x = a * b
    if ("a", "b") in f(a, b):
        print(int(input("Please enter a number> ")))

    else:
        return x





print(f(input("Please enter a number> ")), input("Please enter another number >  "))
