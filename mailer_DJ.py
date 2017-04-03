'''1 - We start by only importing only the classes we need, this also saves us from
having to use the full module name later.'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''4 - For sending the mail, we have to convert the object to a string, and then
use the same prodecure as above to send using the SMTP server..'''
import smtplib

### Import
from filtre_DJ import Filtre
from loader_DJ import Loader

### Affectation du fichier de config a la variable filename
filename = "settings_DJ.ini"

### On instancie 1 objet de type Loader() afin de pouvoir appeler la methode loadConfig(filename) dessus par la suite
loader = Loader()

### La variable configuration contient le dictionnaire genere a partir du fichier de config(=filename) via la fct loadConfig
configuration = loader.loadConfig(filename) 

class Mailer:

	def __init__(self, configuration):
		
		#mail expediteur
		self._mail_expediteur = "centrale.alerte.grp.1@gmail.com"
		
		#mail destinataire
		destinataire = configuration["data"].get("dest")
		if destinataire == None:
			exit()
		self._mail_destinataire = destinataire
		
		#mdp compte mail expediteur
		self._mdp_expediteur = "raspberry"
		
		
	
	def sendMail(self, capteur):
		if capteur == None:
			return None
	
		### Message
		message = MIMEMultipart()
		message['From'] = self._mail_expediteur
		message['To'] = self._mail_destinataire
		message['Subject'] = "Test Domitille"
		body = "L'objet {} a bougé".format(capteur[1])
		message.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(self._mail_expediteur, self._mdp_expediteur)
		text = message.as_string()
		server.sendmail(self._mail_expediteur, self._mail_destinataire, text)
		server.quit()
		

v = ["4C:A5:6D:13:A7:1A", "Luigi Anselmi (Galaxy S5)"]
w = Mailer(configuration)
w.sendMail(v)
		

	
