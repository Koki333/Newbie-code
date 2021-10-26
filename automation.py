def truthy_falsey():
    name = ''
    while not name:
        name = input("Enter your name: > ")
    numofguests = int(input(f"How many guests will you have, {name}? > "))
    if numofguests > 0:
        print(f"Okay, {name}. {numofguests}, that's not bad. Be sure to have enough room for all of your guests.")

    print("Done")

def for_loop():
    print('My name is')
    for n in range(5):
        print("Jimmy five times: (" + str(n) + ")")

def gauss():
    result = 0
    for n in range(0, 101):
        result = result + n
    print(result)

def gauss_while():
    n = 0
    i = 0
    while i < 100:
        i = i + 1
        n = n + i
        print(n)
