### Import
import os
import signal
import subprocess
import time
import sys

from filtre import Filtre
from mailer_v2 import Mailer

### Class
class AlerteurDiscoverer():
	### Init
	def __init__(self, configuration):
		self._filtre = Filtre(configuration) #on recupere le dico de capteurs du fichier settings
		self._mailer = Mailer(configuration) 
		
	### Scanne
	def scan(self, duration=5):
		while True:
			self.find_devices(duration)

	def find_devices(self, duration=5):
		### Lance le subprocess shell Linux permettant de scanner
		proc = subprocess.Popen(['/usr/bin/hcitool', 'lescan'], stdout=subprocess.PIPE) #To run a process and read all of its output, set the stdout value to PIPE and call communicate().
		time.sleep(duration) #laisse un temps ou ca dort entre le processus et le kill ==> ie le scan dure 5 secondes avt d'etre kille
		os.kill(proc.pid, signal.SIGINT) #on kill le process apres 5 s
		proc.stdout.readline().decode("UTF-8") #on lit l'output du scan et on va iterer sur chq ligne de l'output
		#print(proc.stdout.readline().decode("UTF-8"))

		for lines in proc.stdout.readlines():
			values = lines.decode("UTF-8").split(" ")
			print("*" + values[0] + ":" + values[1][:-1] + "*")

			### device discovered
			self.device_discovered(values[0], values[1][:-1]) #le [:-1] slice le dernier caractere de ce qui est retourne, on passe en parametre l'adresse MAC et le nom du device
			# values[0] renvoie l'adresse MAC, valeues[1][:-1] renvoie le nom de l'objet
			### pr chq device scanne on appelle la fct device_discovered qui fait appel a la fct FiltrerCapteur

	### Fonction appeller pour chaque device découvert
	def device_discovered(self, address, name):
		### Pour check
		print("%s - %s" % (address, name))

		### Check si on le mail
		capteur_retourne = self._filtre.FiltrerCapteur(address, name)

		### Fonction return -1 si appartient pas, si doit pas mailer
		if capteur_retourne == None:
			### Do nothing
			return
		else:
			### Faire le mail et l'envoyer
			self._mailer.SendMail(capteur_retourner)








