'''### Attributs classe :
- capteurs : dico capteurs issu fichier de config : {adresse MAC, objet capteur...} --> permet de recuperer l'objet de type Capteur
- frequence : issue fichier de config 
- destinataire : issu fichier de config 

### Methodes classe :
- filtrerCapteur(self, adresse_mac_detectee, name): verif vs. scan, horodatage et renvoie "capteur" de type Capteur()
- tooSoon(self, capteur): verif horodatage'''

from datetime import datetime,timedelta
from capteur import Capteur
import json
### Class permettant de filtrer
class Filtre:
	###
	def __init__(self, configuration):
		### Capteurs
		self.__capteurs = { } #instanciation attribut liste capteurs à liste vide
		for key in configuration["capteurs"]: #iteration sur les cles du dico de capteurs
			liste = json.loads(configuration["capteurs"][key]) #conversion string en liste via json loads transforme string en liste, dico
			self.__capteurs[liste[0]] = Capteur(liste[0], liste[1])
		### Frequence
		frequence = configuration['data'].get("frequence") #methode get permet recuperer valeur ds dico
		#Ici configuration["data"].get("frequence") permet obtenir frequence parametree ds fichier config
		if frequence == None:
			self.__frequence = timedelta(seconds=60)
		else:
			self.__frequence = timedelta(seconds=int(frequence))
		### Destinataire
		self.__dest = configuration["data"]["dest"]

	def getAttributsFiltre(self):
		return self.__capteurs

	''' Fonction qui retourne 1 objet capteur stocke dans la configuration avec horodatage correct
		 Sert a savoir si on va envyoyer 1 mail'''
	def FiltrerCapteur(self, adresse_mac_detectee, name):
		### Verification si adresse_mac_detectee = adresse MAC d'un de nos capteurs
		capteur = self.__capteurs.get(str(adresse_mac_detectee)) #instanciation objet Capteur(), a partir attribut capteurs
		#rappel : attribut capteurs = dico{cle=adresse MAC : valeur=<objet Capteur()>}
		if capteur == None:
			return None #si adresse mac detectee != adresse Mac capteur, do nothing
		### 1ere detection
		if capteur.getHorodatage() == None: #1ere fois que capteur detecte
			### Set horodatage
			capteur.setHorodatageToNow() #parametrage horodatage a heure actuelle
			### return
			return capteur #renvoi du capteur
		### Deja découvert, compare horodatage
		if self.tooSoon(capteur) == True:
			return None
		### Set new horodatage et retourne l'objet
		capteur.setHorodatageToNow()
		return capteur

	### tooSoon : comparaison horodatage
	def tooSoon(self, capteur):
		if capteur.getHorodatage() + self.__frequence >= datetime.now():
			return True #si tps ecoule depuis dernier horodatage < frequence, do nothing
		return False

	'''Fonction qui prend en paramètre le dictionnaire issu du fichier de config et initialise les attributs de la classe Capteur
	def _init_from_configuration(self, configuration):
		### frequence
		frequence = configuration['data'].get("frequence") #methode get permet de recuperer la valeur ds un dico. 
		#Ici configuration["data"].get("frequence") permet obtenir frequence parametree ds fichier config
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

'''config_file = r"G:\PROJETS\CENTRALE ALERTE\Test DJ\settings_DJ.ini" 
#def de constante qui fige le chemin du fichier a lire
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
	# liste = configuration["capteurs"][key] #--> renvoie 1 liste au format string
	# print(configuration["capteurs"][key]) #--> valeur associee a la cle - dico[section][cle] renvoie la valeur associee a la cle de la section du dico
	#en l'occurence, configuration["capteurs"][key] renvoie ["4C:A5:6D:13:A7:1A", "Luigi Anselmi (Galaxy S5)"] puis ["aa::bb::cc::dd", "mon objet"], etc.
	#cela renvoie une liste, sur laquelle on peut faire liste[0] afin de recuperer l'adresse MAC
	print(liste[0]) #renvoie le 1er element de la liste precedemment renvoyee, soit l'adresse MAC
	capteurs[liste[0]] = Capteur(liste[0], liste[1]) #liste[0]=adresse mac, liste[1]=nom objet -- a chaque adresse mac trouvee, on instancie un objet de type Capteur()
	#la cle du dico ainsi constitue est l'adresse mac et la valeur correspondante est l'objet de type Capteur()
	#print(capteurs) #{'4C:A5:6D:13:A7:1A': <capteur.Capteur object at 0x014E45F0>, 'aa::bb::cc::dd': <capteur.Capteur object at 0x033679B0>}
	#print(capteurs.get("4C:A5:6D:13:A7:1A")) #<capteur.Capteur object at 0x014E45F0>
	#json.dumps convertit un dictionnaire en string
	############## In fine, on obtient un dico de capteurs, avec pour cle, l'adresse MAC et en valeur, un objet de type Capteur()'''







