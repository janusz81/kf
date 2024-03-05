import random
import sys
#sys.stdout.reconfigure(encoding='utf-8')

class Regula:
	def __init__(self,znak,pol,ang):
		self.znak=znak
		self.pol=pol
		self.ang=ang
	def __str__(self):
		return "%s - %s - %s"%(self.znak,self.pol,self.ang)

class Reguly:
	def __init__(self):
		self.reguly=[]
	def readfromfile(self,filepath):
		with open(filepath,"r",encoding="utf-8") as plik:
			for linia in plik:
				if linia.startswith("#"):continue
				(znak,pol,ang)=linia.replace("\n","").split(";")
				regula=Regula(znak,pol,ang)
				self.reguly.append(regula)
		if len(self.reguly)==0:
			print("nie udało się wczytać definicji")
			return None
		else:return self
	def zadanie(self,co,naco):
		print("Zamiana %s na %s"%(co,naco))
		los=random.sample(self.reguly,5)
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

if __name__=="__main__":
	if len(sys.argv)!=3:
		print("Parametry: nazwa pliku z definicją i ilość zadań")
		sys.exit(-1)
	reguly=Reguly()
	print(sys.argv[1])
	ret=reguly.readfromfile(sys.argv[1])
	if ret==None:sys.exit(-1)
	liczba_zadan=int(sys.argv[2])
	liczba_poprawnych=0
	for i in range(liczba_zadan):
		co,naco=random.sample(["znak","pol","ang"],2)
		liczba_poprawnych+=reguly.zadanie(co,naco)
	print("Poprawnie %d z %s zadań."%(liczba_poprawnych,liczba_zadan))