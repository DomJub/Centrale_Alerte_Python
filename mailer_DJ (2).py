### import
import smtplib

# Import les modules email
### HTML send as mail ... check si fonctionne
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

### template le mail
from datetime import datetime,timedelta

### 
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

### class qui va servir à envoyer 1 mail ici
class Mailer:
	### init
	def __init__(self, configuration):
		### Peut verifier la validité de l'adresse mail
		### Import à vrai dire
		self._mail_expediteur = "centrale.alerte.grp.1@gmail.com"
		destinataire = configuration["data"].get("dest")
		if destinataire == None:
		### Destinataire
		
			### Ne feras rien anyway
			exit()
		
		self._mail_destinataire = destinataire

		### enleve si utilise mail que l'on fait nous pour l'utilisateur
		self._mdp_expediteur = "raspberry"

		###
		self._template_filename = "message.html"

		### env
		self._env = Environment()
		self._env.loader = FileSystemLoader('templates')

	### Action principale
	def SendMail(self, capteur):
		### Check
		if capteur == None:
			return None
		
		### Others check

		### Message
		message = MIMEMultipart()

		### Set le header
		message['From'] = self._mail_expediteur
		message['To'] = self._mail_destinataire
		message['Subject'] = "Un capteur est en train d'être voler !!!"

		### Contenue du message
		content = self.FormateMail(capteur)

		#raise RuntimeError(content)

		### Attache le document text au message
		message.add_header('Content-Type','text/html')
		message.attach(MIMEText(content, "html"))

		### Utilise gmail pour émettre le mail
		### Peut etre 1 mail à nous en fait
		
		#mailserver = smtplib.SMTP('smtp.gmail.com', 587)#465 not working
		mailserver = smtplib.SMTP('smtp.gmail.com', 587)

		### STMP protocole
		mailserver.ehlo()
		mailserver.starttls()

		### Ce login dans gmail
		mailserver.login(self._mail_expediteur, self._mdp_expediteur)
		
		### Emettre le mail
		mailserver.sendmail(self._mail_expediteur, self._mail_destinataire, message.as_string())

		### quitter
		mailserver.quit()

	### Encapsule le building pour pas surcharger l'autre fonction
	def FormateMail(self, capteur):
		### Build from template
		template = self._env.get_template(self._template_filename)
		
		content = template.render(
			title="Un capteur vient de bouger", 
			capteur=capteur)

		### return
		return content











