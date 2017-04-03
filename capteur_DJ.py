### import
from datetime import datetime, timedelta
import re

### Classe represente 1 capteur et sa configuration
class Capteur:

	'''Un objet de type Capteur a 3 attributs : une adresse MAC, un nom et un dernier horodatage initialise a None par defaut'''
	def __init__(self, adresse_mac, nom_objet = "Capteur(unnamed)"):
		# adresse MAC
		self._MAC_address = adresse_mac
		# nom "user-friendly"
		self._object_name = nom_objet
		# dernier Datetime
		self._last_detect = None

	### Shortcut pour set le dernier horodatage à Now : seule action qu'on effectue sur la date
	def setHorodatageToNow(self):
		self._last_detect = datetime.now()
	
	### Recuperer l'horodatage
	def getHorodatage():
		return self._last_detect
	
	### Recuperer le nom de l'objet
	def getName():
		return self._object_name
		
	### Recuper l'adresse MAC
	def getAdresseMac
		return self._MAC_address

	### Verifier la validite de la MAC address
	def verifyAdresseMac(self):
		template_MAC = re.compile("[0-9A-F]{2}([-:])[0-9A-F]{2}(\\1[0-9A-F]{2}{4}$")
		



