# This is a sample Python script.
import nt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
val = "global"
def learning_27_05_2024():
    #print
    print("Hello, World!")

    #variables learning
    x = 5
    y = "John"
    print(x)
    print(y)

    #variables guidelines learning
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"

    #multiple variable intialization
    x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)

    #single value to multiple variable intilization
    x = y = z = "Orange"
    print(x)
    print(y)
    print(z)

    #list to vaiables
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)

    #diffrent rpint statement
    x = "Python"
    y = "is"
    z = "awesome"
    print(x, y, z)

    x = "Python "
    y = "is "
    z = "awesome"
    print(x + y + z)

    x = 5
    y = 10
    print(x + y)

    x = 5
    y = "John"
    print(x, y)

    #global
    global globe
    globe = 10
    # This is a single line comment.
    #datatype

    x = 5
    print(type(x))

    x = "Hello World"
    print(type(x))
    #str
    x = 20
    print(type(x))
    #int
    x = 20.5
    print(type(x))
    #float
    x = 1j
    print(type(x))
    #complex
    x = ["apple", "banana", "cherry"]
    print(type(x))
    #list
    x = ("apple", "banana", "cherry")
    print(type(x))
    #tuple
    x = range(6)
    print(type(x))
    #range
    x = {"name": "John", "age": 36}
    print(type(x))
    #dict
    x = {"apple", "banana", "cherry"}
    print(type(x))
    #set
    x = frozenset({"apple", "banana", "cherry"})
    print(type(x))
    #frozenset
    x = True
    print(type(x))
    #bool
    x = b"Hello"
    print(type(x))
    #bytes
    x = bytearray(5)
    print(type(x))
    #bytearray
    x = memoryview(bytes(5))
    print(type(x))
    #memoryview
    x = None
    print(type(x))
    #None

    #int usage
    x = 1
    y = 35656222554887711
    z = -3255522

    print(type(x))
    print(type(y))
    print(type(z))

    #float usage
    x = 1.10
    y = 1.0
    z = -35.59

    print(type(x))
    print(type(y))
    print(type(z))

    #exponential
    x = 35e3
    y = 12E4
    z = -87.7e100

    print(type(x))
    print(type(y))
    print(type(z))

    #complex
    x = 3 + 5j
    y = 5j
    z = -5j

    print(type(x))
    print(type(y))
    print(type(z))

    #type conversion
    x = 1  # int
    y = 2.8  # float
    z = 1j  # complex

    # convert from int to float:
    a = float(x)

    # convert from float to int:
    b = int(y)

    # convert from int to complex:
    c = complex(x)

    print(a)
    print(b)
    print(c)

    print(type(a))
    print(type(b))
    print(type(c))

    #work on random numbers
    print(random.randrange(1, 10))

    #casting
    x = int(1)  # x will be 1
    y = int(2.8)  # y will be 2
    z = int("3")  # z will be 3

    print(x, y, z)

    x = float(1)  # x will be 1.0
    y = float(2.8)  # y will be 2.8
    z = float("3")  # z will be 3.0
    w = float("4.2")  # w will be 4.2

    print(x, y, z)

    x = str("s1")  # x will be 's1'
    y = str(2)  # y will be '2'
    z = str(3.0)  # z will be '3.0'

    print(x, y, z)

    #quotes
    print("It's alright")
    print("He is called 'Johnny'")
    print('He is called "Johnny"')

    #multiline string

    a = """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua."""
    print(a)

    #string
    a = "Hello, World!"
    print(a[1])

    #iterate of string
    for i in a :
        print(i)
    print(len(a))

    txt = "The best things in life are free!"
    if "free" in txt:
        print("Yes, 'free' is present.")
    if "expensive" not in txt:
        print("No, 'expensive' is NOT present.")

    #string slicing
    b = "Mohith Shivu   "
    print(b[2:5])
    print(b[:])
    print(b[2:])
    print(b[:2])
    print(b[-5:-2])
    print(b.upper())
    print(b.lower())
    print(b.capitalize())
    print(b.strip())
    print(b.replace("S", "s"))
    print(b.split(" "))

    #format string
    a = 3
    print(f"the valuse of a is {a}")
    print(f"the valuse of a is {a:.2f}")
    txt = f"The price is {20 * 59} dollars"
    print(txt)

    txt = "We are the so-called \"Vikings\" from the north."
    print(txt)

    #String opertaions
    txt = "Company123"

    x = txt.isascii()

    print(x)
    txt = "banana"

    x = txt.center(20)

    print(x)
    txt = "My name is Ståle"

    x = txt.encode()

    print(x)
    txt = "For only {price:.2f} dollars!"
    print(txt.format(price=49))

    #boolean
    print(10 > 9)
    print(10 == 9)
    print(10 < 9)

    x = "Hello"
    y = 15

    print(bool(x))
    print(bool(y))

    bool(False)
    bool(None)
    bool(0)
    bool("")
    bool(())
    bool([])
    bool({})

    #power
    print(2**8)

    #list
    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    print(thislist)

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])

    thislist = ["apple", "banana", "cherry"]
    thistuple = ("kiwi", "orange")
    thislist.extend(thistuple)
    print(thislist)

    thislist = ["apple", "banana", "cherry"]
    thislist.pop(1)
    print(thislist)

    thislist = ["apple", "banana", "cherry"]
    del thislist[0]
    print(thislist)

    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)

    #list comprehension
    thislist = ["apple", "banana", "cherry"]
    [print(x) for x in thislist]

    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    newlist = [x for x in fruits if "a" in x]

    print(newlist)

    newlist = [x if x != "banana" else "orange" for x in fruits]

    thislist = [100, 50, 65, 82, 23]
    thislist.sort(reverse=True)
    print(thislist)

    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)

    #tuple
    thistuple = ("apple", "banana", "cherry")
    print(thistuple)

    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)

    print(x)

    thistuple = ("apple", "banana", "cherry")
    y = ("orange",)
    thistuple += y

    print(thistuple)

    #unpack tuples
    fruits = ("apple", "banana", "cherry")

    (green, yellow, red) = fruits

    print(green)
    print(yellow)
    print(red)

    #astric
    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

    (green, yellow, *red) = fruits

    print(green)
    print(yellow)
    print(red)

    """
    this is multi line comments
    """

learning_27_05_2024()
print(val)
print(globe)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
