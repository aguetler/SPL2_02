# primes.py
# erzeugen der Primzahlen von 1 bis 1000
# Achtung: 1 ist per Definition keine(!) Primzahl

zahlen = 0
for i in range (2,1001):
	isPrime = True
	for z in range (2, i):
		if (i % z == 0):
			isPrime = False
			break
	if (isPrime == True):
		zahlen += 1
		print (i, end=", ")	

print("Anzahl Primzahlen von 1 bis 1000:", zahlen)