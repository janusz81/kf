import random
#import sys
#sys.stdout.reconfigure(encoding='utf-8')

class Regula:
	def __init__(self,znak,pol,ang):
		self.znak=znak
		self.pol=pol
		self.ang=ang
	def __str__(self):
		return "%s - %s - %s"%(self.znak,self.pol,self.ang)

def zadanie(reguly,co,naco):
	print("Zamiana %s na %s"%(co,naco))
	los=random.sample(reguly,5)
	pytanie=[getattr(l,co) for l in los]
	odpowiedz=[getattr(l,naco) for l in los]
	odpowiedz=" ".join(odpowiedz)
	print("Zamień: %s"%(" ".join(pytanie)))
	odp=input().strip()
	if odp.lower().replace(" ","")==odpowiedz.lower().replace(" ",""):
		print("OK\n")
		return 1
	else:
		print("Prawidłowa: %s\n"%(odpowiedz))
		return 0

sciezka="literowanie.dat"
reguly=[]
with open(sciezka,"r",encoding="utf-8") as plik:
	for linia in plik:
		(znak,pol,ang)=linia.replace("\n","").split(";")
		regula=Regula(znak,pol,ang)
		reguly.append(regula)

liczba_zadan=5
liczba_poprawnych=0
for i in range(liczba_zadan):
	co,naco=random.sample(["znak","pol","ang"],2)
	liczba_poprawnych+=zadanie(reguly,co,naco)
print("Poprawnie %d z %s zadań."%(liczba_poprawnych,liczba_zadan))