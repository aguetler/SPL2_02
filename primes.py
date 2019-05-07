# primes.py
# erzeugen der Primzahlen von 1 bis 1000
# Achtung: 1 ist per Definition keine(!) Primzahl

# Beispiel
i = 10
if (i == 10):
	print ("ok.")
else:
	print ("nicht ok.")

for i in range (2,1001):
	isPrime = True
	for z in range (2, i):
		if (i % z == 0):
			isPrime = False
			break
	if (isPrime == True):
		print (i, end=", ")
	