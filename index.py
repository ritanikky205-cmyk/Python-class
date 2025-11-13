name_class ="Hello Rita"

print(name_class)

name= "Rita"
age=23

print(f"my name is {name}\nI am {age} years old")

name= ["promise", "Rita", "Success", "Innocent"]
a, b, c, d = name

print(a)
print (b)
print (c)
print(d)

#month= ["jan", "Feb", "March"]
#x, y, z =month

#print(x)
#print(y)
#print(z)

print("my name is Rita\nI am 23 years old\nI am a web developer")

Name_Class_Group= "Rita"
print(f"my name is {Name_Class_Group}\nI am a web developer")

x= "Rita "
y= "is a good girl "
z= "always "

print(x+y+z)

x = "Rita"

def myfunc():
    print("my name is " + x)

myfunc()

def myfunc():
    global baller
    baller = "fantastic"

myfunc()

print("python is " + baller)

print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """I am a fan of football\nI love Chelsea football club\nmy blood bleeds blue."""
print(a)
a='''I am e tech enthuasist\nA web developer\nA coder.'''
print(a)

a = "Hello World"
print(a[8])

for x in "apple":
    print(x)

for y in "melon":
    print(y)

   # a = "Hello World"
   # print(len(a))

a = ['mango', 'apple', 'cashew']
print(len(a))


txt = "The best things in life are free!"
print("bee" in txt)

b = "Hello, World"
print(b[3:5])

#slicing from the start

name = "Hello, World"
print(name[:5])

name = "Rita, World"
print(name[5:])
print(name.upper())
print(name.lower())
print(name.strip())

print(name.replace("R", "Z"))

print(name.split(","))

#concatenation string

nan = 'Come '
vin = 'here '
can = 'now'
dao = nan + vin + can

print(dao)
nan = 'Come'
vin = 'here'
can = 'now'
dao = nan + " "+ vin +" "+ can

print(dao)

price = 30
print(f"I need {price:.3f} money")

#format spring outside print function

txt = f"I need {20} houses"
print(txt)

txt = f"I need {20 * 3} houses"
print(txt)

test = "We are so-called \"Vikings\" from the North."
print(test)


Rita = "I have taken my lunch"
x = Rita.capitalize()
print (x)

x = Rita.casefold()
print (x)

x = Rita.center(5)
print (x)

x = Rita.count("h")
print (x)

x = Rita.encode()
print (x)

x = Rita.endswith("h")
print (x)


x = txt.expandtabs()
print(x)

x = txt.find("n")
print(x)

x = txt.format("o")
print(x)

x = txt.format_map("p")
print(x)

x = txt.index("h")
print(x)

txt = "A1b3c5"
x = txt.isalnum()
print(x)

txt = "12345"
x = txt.isalpha()
print(x)

txt = "go,python"
x = txt.isascii()
print(x)

x = txt.isdecimal()
print(x)

x = txt.isdigit()
print(x)

x = txt.isidentifier()
print(x)

x = txt.islower()
print(x)

x = txt.isnumeric()
print(x)

x = txt.isprintable()
print(x)

x = txt.isspace()
print(x)

x = txt.istitle()
print(x)

x = txt.isupper()
print(x)

mytuple = ("john", "peter","vicky")
x = "#".join(mytuple)
print(x)

txt = "banana" 
x = txt.ljust(20)
print(x, "is my favorite fruit.")

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

x = txt.lstrip()
print(x)

txt = "Hello Sam!"
x = str.maketrans("S", "p")
print(txt.translate(x))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

x = txt.replace("bananas", "apples")
print(x)

x = txt.rfind("all")
print(x)

x = txt.rindex("bananas")
print(x)

x = txt.rjust(20)
print(x, "is my favorite fruit")

txt = "apple, banana, cherry"
x = txt.rsplit(",")
print("x")

x = txt.rpartition("banana")
print(x)

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "Thank you for the music\nwelcome to the jungle"
x = txt.splitlines()
print(x)

x = txt.startswith("Thank")
print(x)

txt = "    banana    "
x = txt.strip()
print("of all fruits", x,"is my favorite")

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

txt = "Welcome to my World"
x = txt.title()
print(x)

mydict = {83: 80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello my friends"
x = txt.upper()
print(x)

txt = "50"
x = txt.zfill(10)
print(x)