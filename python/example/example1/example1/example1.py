import random #import random to code

print("Hello, World!!") #print

num1 = 5 #int
num2 = 2.66148 #float
print("num1: ",num1)
print("type of num1: ",type(num1))
print("num2: ",num2)
print("type of num2: ",type(num2))

#can
print("num1 + num2:", num1 + num2) #plus
""" can't
x = 5
y = "John"
print(x + y)
"""

print("num1 - num2:", num1 - num2) #
print("num1 * num2:", num1 * num2) #
print("num1 / num2:", num1 / num2) #
print("num1 % num2:", num1 % num2) #
print("num1 ** num1:", num1 ** num1) #
print("num1 // num2:", num1 // num2) #

sum0 = num2
print("sum0:", sum0)
sum0 += num1 #sum0 = sum0 + num1
print("sum0 += num1:", sum0)
sum0 -= num1 #sum0 = sum0 - num1
print("sum0 -= num1:", sum0)
sum0 *= num1 #sum0 = sum0 * num1
print("sum0 *= num1:", sum0)
sum0 /= num1 #sum0 = sum0 / num1
print("sum0 /= num1:", sum0)
sum0 %= num1 #sum0 = sum0 % num1
print("sum0 %= num1:", sum0)
sum0 **= num1 #sum0 = sum0 ** num1
print("sum0 **= num1:", sum0)
sum0 //= num1 #sum0 = sum0 // num1
print("sum0 //= num1:", sum0)

#string
"""
    "" and '' is the same as,
"""
name1 = "John"
name2 = 'Sally'
print("name1: " + name1)
print("type of name1: ",type(name1))
print("name1: " + name1)
print("type of name1: ",type(name1))
#string is sequence of letters

#can print(str + str)
# or
#can print(str,any,...)
# or
#can print(f"str {any}") -- the fastest

print("name1[0]: ",name1[0]) #some letters in name1
"""
    name1[index]
    in name1 have:
        index 0: J
        index 1: o
        index 2: h
        index 3: n
"""

#All letters
for c in name1:
    print(c)

#len() -> Text length
print(len(name1))
for i in range(len(name1)):
    print(i,":",name1[i])

txt = "The best things in life are free!"
print('has "free" in txt?: ',"free" in txt) #Check if there is free in txt -> bool
print('has not "free" in txt?: ',"free" not in txt)

print(txt[0:2]) #get text period index 0-2 -> 0:T,1:h
print(txt[:8]) #get text period index end of 8 -> 0:T,1:h,...7:b
print(txt[8:]) #get text period index start with 8 -> 8: ,9:t,...

price = 59
print(f"The price is {price:.2f} dollars") #is print price in float 2 decimals

str0 = str(3) #make any to string

int0 = int(str0) #make string to int
int0 = int(3) #make int to int
int0 = int(3.8) #make float to int
#int0 = int("3.1") can't

float0 = float(str0) #make string to float
float0 = float(3) #make int to float
float0 = float(3.0) #make float to float

print("num1: " + str(num1)) 
print("type of num1: ")
print(type(num1)) #get type

print("num2: " + str(num2))
print("type of num2: ")
print(type(num2))

print("name1: " + str(name1))
print("type of name1: " )
print(type(name1))

print("name2: " + str(name2))
print("type of name2: " )
print(type(name2))

print("3 to string: " + str(str0))
print("type of str0: " )
print(type(str0))

print('"3" to int: ' + str(int0))
print("type of int0: " )
print(type(int0))

print('"3" to float: ' + str(float0))
print("type of float0: " )
print(type(float0))

#can
myvar = " "
my_var = " "
_my_var = " "
myVar = " "
MYVAR = " "
myvar2 = " "

""" can't
2myvar = "John"
my-var = "John"
my var = "John"
"""

o0,b0,c0 = "Orange", "Banana", "Cherry"
print(o0)
print(b0)
print(c0)

o1 = b1 = c1 = "Orange"
print(o1)
print(b1)
print(c1)

#tuple
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)
print(b)
print(c)

xf1 = "awesome"

#create function
def f1() -> (): # -> make it say that func return what, it this -> () is return not thing it is void func
    xf1 = "fantastic" #fx1 in f1() is changing
    print("Python is " + xf1)

f1()
#fx1 out f1() is not changing
print("Python is " + xf1)

#global in func
xf2 = "KUY"

def f2() -> ():
    global xf2 #make xf2 can changed
    xf2 = "Good"

f2() #xf2 changed to "Good"

print("Python is " + xf2)

def addStr(x):
    print(x + "Refsnes")
addStr("Emil")
addStr("Tobias")
addStr("Linus")

def kidF(*kids): #add * to make func know kids is tuple
  print("The youngest child is " + kids[2])

kidF("Emil", "Tobias", "Linus")

def getNamein(**kid): #add ** to make func know kid is dict
    print("His name is " + kid["name"])
getNamein(name = "Goten",age = -1)

def wow(x = "KUY"):
    print("you is " + x)
wow("cute")
wow()

def MFive(x):
    return x * 5
print(MFive(1))
print(MFive(2))

c = 1j #complex(จำนวนเชิงซ้อน)
print("c:", c)
print("type of c: ", type(c))
Z = 3 + c
print("Z:",Z)
print("Z real num:",Z.real)
print("Z complex num:",Z.imag)
# x = complex(1j)

lists0 = [1,'GG',1.515,3j] #list
print("lists0:", lists0)
print("type of lists0: ", type(lists0))
# x = list(("apple", "banana", "cherry"))
print("has 1 in lists0?: ", 1 in lists0)
print("hasn't 1 in lists0?: ", 1 not in lists0)

for x in lists0:
  print(x)

tuple0 = ("EZ",51,15.152,0.5j) #tuple
print("tuple0:", tuple0)
print("type of tuple0: ", type(tuple0))
# x = tuple(("apple", "banana", "cherry"))

ran0 = range(6) #range
#for loop
for i in ran0: #make i = 0 -> 6
    print("i:",i)

dicts0 = {"name" : "John", "age" : 36} #dict
print("dicts0:", dicts0)
print("type of dicts0: ", type(dicts0))
# x = dict(name="John", age=36)

t = True #bool
f = False
print("t:", t)
print("type of t: ", type(t))
print("f:", f)
print("type of f: ", type(f))
# x = bool(1) -> True, x = bool(0) -> False
print("t == t: ", t == t)
print("f == f: ", f == f)
print("t == f: ", t == f)
print("t != t: ", t != t)
print("f != f: ", f != f)
print("t != f: ", t != f)
print("5 > 6: ", 5 > 6)
print("5 < 6: ", 5 < 6)
print("5 >= 6: ", 5 >= 6)
print("5 <= 6: ", 5 <= 6)
print("5 > 3 and 5 < 10: ", 5 > 3 and 5 < 10)
print("5 > 3 or 5 < 10: ", 5 > 3 or 5 < 10)
print("not(5 > 3 and 5 < 10): ", not(5 > 3 and 5 < 10))

print("random 1-10: ",random.randrange(1, 10)) #random int in range 1 - 10

what = """ Bro WTF
WOW asafsf a
fa sg sdg dfh dh
 hfgj j gfjhjgfh
 jjgfhjg """
print(f"What?: {what}")

print("6 & 3: ",6 & 3) #AND
print("6 | 3: ",6 | 3) #OR
print("6 ^ 3: ",6 ^ 3) #XOR
print("~3: ",~3) #NOT
print("3 << 2: ",3 << 2) #Zero fill left shift
print("8 >> 2: ",8 >> 2) #Signed right shift

#if - else
def checkNum0(x,y):
    if x < y:
        print("x is lesser than y")
    elif x == y:
        print("x and y are equal")
    else: 
        print("x is greater than y")
    
def checkNum1(x,y):
    if x > y:
        pass
    else:
        print("x is not greater than y")

checkNum0(33,200)
checkNum0(61,21)
checkNum0(1,1)
checkNum1(100,45)
checkNum1(14,1032)

i = 0
while i < 100:
    i += 1
    if i % 20 == 0:
        continue
    if  i == 88:
        break
    
    print(i)

class Tvector2D:
    x : int | float
    y : int | float
    
point0 = Tvector2D()
point0.x = 0
point0.y = 1
print("point0 x: ",point0.x)
print("point0 y: ",point0.y)

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
  
  def Hello(self):
      print("Hello my name is " + self.name)

plr1 = Person("John", 36)

print("plr1 name: ",plr1.name)
print("plr1 age: ",plr1.age)
plr1.Hello()
