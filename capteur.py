### import
from datetime import datetime,timedelta

### Class représent 1 capteur et sa configuration ( pas 1 capteur réel )
class Capteur:
	### init
	def __init__(self, adresse_mac, nom_objet="Capteur(unnamed)"):
		### MAC
		### Check validité avec 1 class permettrais d'éviter de surcharger de la daube
		###	Voire d'avertir l'utilisater avec 1 mail
		###		Bonne idée : ligne et tout
		self._adresse_MAC = adresse_mac

		### Nom "user friendly"
		self._nom_objet = nom_objet

		### Dernier date time
		self._timestamp = None

	### Short cut pour set le timestamp at now : seul action que l'on effectue sur la date
	def SetHorodatageToNow(self):
		self._timestamp = datetime.now()

	### Permet de retourner l'horodatage
	def GetHorodatage(self):
		return self._timestamp

	### adresse mac
	def GetAdresseMAC(self):
		return self._adresse_MAC

	###
	def GetName(self):
		return self._nom_objet









