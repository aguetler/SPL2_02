# variable.py

a=10
b=20
c=30

print (a+b+c)
print ("Summe = ", a+b+c)

print ("Multiplikation", a*b)

print ("Division", a/b)
print ("Division", c/a)
print ("Division", int(c/a))

print ("Potenz", a**b)

text = "Hallo Welt"
print (text)
print (text * 99)

print ("-" * 20)
print ("Hallo Welt")
print ("-" * 20)

# name = input("Wer bist du?")
name = "Alexander"
print ("Hallo", name * 99)

for i in ("Franz", "Karl", "Klaus"):
	print(i)
	
for i in (-4, 12, 19, 7, 0, -281, 192):
	print (i, end=" ")
	
for i in range (1, 100):
	print (i, end=".")
	
while (True):
	i *= 2
	print (i, end=".")
	
	




