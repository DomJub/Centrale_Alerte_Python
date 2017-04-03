### Import
from filtre_DJ import Filtre
from loader_DJ import Loader


### Affectation du fichier de config a la variable filename
filename = "settings_DJ.ini"

### On instancie 1 objet de type Loader() afin de pouvoir appeler la methode loadConfig(filename) dessus par la suite
loader = Loader()

### La variable configuration contient le dictionnaire genere a partir du fichier de config(=filename) via la fct loadConfig
configuration = loader.loadConfig(filename) 
#{'data': {'dest': 'centrale.alerte.grp.1@gmail.com', 'frequence': '40'}, 
#'capteurs': {'mac1': '["4C:A5:6D:13:A7:1A", "Luigi Anselmi (Galaxy S5)"]', 'mac3': '["aa::bb::cc::dd", "mon objet_1"]', 'mac4': '["ee::ff::gg::hh", "mon objet_2"]'}}
v = Filtre(configuration)
print(v.getAttributsFiltre())
#{'4C:A5:6D:13:A7:1A': <capteur.Capteur object at 0x0326EE10>, 'aa::bb::cc::dd': <capteur.Capteur object at 0x0326EED0>, 'ee::ff::gg::hh': <capteur.Capteur object at 0x0327DDD0>}













