config_file = r"G:\PROJETS\CENTRALE ALERTE\Test DJ\settings_DJ.ini" 
'''def de constante qui fige le chemin du fichier a lire'''
import configparser
import json
from capteur import Capteur

config = configparser.ConfigParser() #fct configparser.ConfigParser() declare un objet 
config.read(config_file) #on applique la methode read de l'objet config a notre fichier de config

configuration = {section:dict(config.items(section)) for section in config.sections()}
capteurs = {}
for key in configuration["capteurs"]: #on itere sur les cles du dico de capteurs, ie mac 1, mac 2, mac 3, etc.
	### check
	liste = json.loads(configuration["capteurs"][key]) #json.loads hyper imptt pr que la liste ne soit pas au format string, sinon liste[0] renvoie "[" ald renvoyer adresse mac
	# liste = configuration["capteurs"][key] --> renvoie 1 liste au format string
	#print(configuration["capteurs"][key]) #--> valeur associee a la cle - dico[section][cle] renvoie la valeur associee a la cle de la section du dico
	# en l'occurence, configuration["capteurs"][key] renvoie ["4C:A5:6D:13:A7:1A", "Luigi Anselmi (Galaxy S5)"] a 1ere iteration, ["aa::bb::cc::dd", "mon objet"] a 2e iter., etc.
	# cela renvoie une liste
	print(liste[0]) #renvoie le 1er element de la liste precedemment renvoyee, soit l'adresse MAC
	capteurs[liste[0]] = Capteur(liste[0], liste[1]) #liste[0]=adresse mac, liste[1]=nom objet -- a chaque adresse mac trouvee, on instancie un objet de type Capteur()
	#la cle du dico ainsi constitue est l'adresse mac et la valeur correspondante est l'objet de type Capteur()
	print(capteurs) #{'4C:A5:6D:13:A7:1A': <capteur.Capteur object at 0x014E45F0>, 'aa::bb::cc::dd': <capteur.Capteur object at 0x033679B0>}
	print(capteurs.get("4C:A5:6D:13:A7:1A"))
	#json.dumps convertit un dictionnaire en string
	# In fine, on obtient un dico de capteurs, avec pour cle, l'adresse MAC et en valeur, un objet de type Capteur()



'''### Class permettant de filtrer
class Filtre:
	###
	def __init__(self, configuration):
		### On instancie l'attribut liste de capteurs à une liste vide
		self.__capteurs = { }

		### fonction qui parse et qui parametre les attributs frequence, destinataire et capteurs en fonction du dictionnaire issu fichier de config.
		self._init_from_configuration(configuration)

	### Fonction qui retourne 1 capteur stocke dans la configuration avec horodatage correct
	### Sert a savoir si on va envyoyer 1 mail
	def FiltrerDevice(self, adresse_mac_detectee, name):
		### Check ours
		capteur = self.__capteurs.get(str(adresse_mac_detectee)) #
		if capteur == None:
			return None

		### 1ere detection
		if capteur.getHorodatage() == None:
			### Set horodatage
			capteur.setHorodatageToNow()

			### return
			return capteur

		### Deja découvert, compare horodatage
		if self.isFresh(capteur) == True:
			return None

		### Set new horodatage et retn l'objet
		capteur.setHorodatageToNow()

		return capteur

	### Is fresh : comparaison horodatage
	def isFresh(self, capteur):
		### Juste check : pas 60 seconde écoulée ( 15h10 + 10 : 15h20 , frequence de 5 : 
		if capteur.GetHorodatage() + self.__frequence >= datetime.now():
			return True
		return False

	Fonction qui prend en paramètre le dictionnaire issu du fichier de config
	def _init_from_configuration(self, configuration):
		### frequence
		frequence = configuration["data"].get("frequence") #methode get permet de recuperer la valeur ds un dico. Ici configuration["data"].get("frequence") permet obtenir frequence parametree ds fichier config
		if frequence == None:
			self.__frequence = timedelta(seconds=60)
		else:
			self.__frequence = timedelta(seconds=int(frequence))

		### dest
		self.__dest = configuration["data"]["dest"]

		### capteurs
		for key in configuration["capteurs"]: #on itère sur les cles du dico de capteurs
			### check
			liste = json.loads(configuration["capteurs"][key])
			self.__capteurs[liste[0]] = Capteur(liste[0], liste[1])
			#json.dumps convertit un dictionnaire en string'''









