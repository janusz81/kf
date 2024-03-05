import random
import sys
#sys.stdout.reconfigure(encoding='utf-8')

class Pytanie:
	def __init__(self,pytanie,odpowiedz):
		self.pytanie=pytanie
		self.odpowiedz=odpowiedz
	def __str__(self):
		return "%s: %s"%(self.pytanie,self.odpowiedz)

class Pytania:
	def __init__(self):
		self.pytania=[]
		self.polecenie=None
	def readfromfile(self,filepath):
		with open(filepath,"r",encoding="utf-8") as plik:
			for linia in plik:
				if linia.startswith("#"):continue
				(pyt,odp)=linia.replace("\n","").split(";")
				pytanie=Pytanie(pyt,odp)
				if self.polecenie is None:self.polecenie="Podaj %s %s"%(pytanie.odpowiedz,pytanie.pytanie)
				else:self.pytania.append(pytanie)
		if len(self.pytania)==0:
			print("nie udało się wczytać definicji")
			return None
		else:return self
	def zadanie(self):
		los=random.choice(self.pytania)
		print("%s"%(los.pytanie))
		odp=input().strip()
		if odp.lower().replace(" ","")==los.odpowiedz.lower().replace(" ",""):
			print("OK\n")
			return 1
		else:
			print("Prawidłowa: %s\n"%(los.odpowiedz))
			return 0

if __name__=="__main__":
	if len(sys.argv)!=3:
		print("Parametry: nazwa pliku z definicją i ilość zadań")
		sys.exit(-1)
	pytania=Pytania()
	ret=pytania.readfromfile(sys.argv[1])
	if ret==None:sys.exit(-1)
	liczba_zadan=int(sys.argv[2])
	liczba_poprawnych=0
	print(pytania.polecenie)
	for i in range(liczba_zadan):
		liczba_poprawnych+=pytania.zadanie()
	print("Poprawnie %d z %s zadań."%(liczba_poprawnych,liczba_zadan))