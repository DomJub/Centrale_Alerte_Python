'''But = transformer le fichier de configuration ds lequel on a notamment la liste des adresses MAC et le nom de nos capteurs en dictionnaire exploitable
1- Fct generale loadConfig(filename) qui se base sur 2 fct : _load_config(filename) & _config_to_dict(config)
2 - Fct _load_config(filename) --> créé objet config de type ConfigParser()
3 - Fct _config_to_dict(config) --> retourne un dictionnaire'''
### import
import configparser

### class permettant de loader
class Loader:
	### init
	def __init__(self):
		### nothing
		pass

	### Load
	'''fonction qui prend en argument un nom de fichier (variable indiquant emplacement fichier) correspondant a fichier de configuration et renvoie un dictionnaire'''
	def loadConfig(self, filename):
		### Check
		if filename == None:
			return None
		### load
		config = self._load_config(filename)
		### to dict
		dictionnary = self._config_to_dict(config)
		return dictionnary


	### Load config
	'''fonction qui prend en argument un nom de fichier (variable indiquant emplacement fichier) et renvoie un objet de type ConfigParser()'''
	def _load_config(self, filename):
		config = configparser.ConfigParser()
		config.read(filename) #on lit l'objet config qu'on vient d'instancier a la ligne du dessus
		return config

	### Config to dict
	''' fonction qui prend en argument un objet de type ConfigParser() retourne par la fct _load_config. Convertit un fichier de configuration en dictionnaire de dictionnaire.'''
	def _config_to_dict(self, config):
		dict_result = {section:dict(config.items(section)) for section in config.sections()} #la section est la cle du 1er dico, et le 2e dico doit contenir les couples cles/valeur propres a cette section
		return dict_result
		'''result = {}
								for section in config.sections():
									result[section] = {}
									for key, val in config.items(section):
										result[section][key] = val
								return result'''







