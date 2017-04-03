### Import
from alerteur_v3 import AlerteurDiscoverer
from loader import Loader
from web_loader import WebLoader

### Affectation du fichier de config a la variable filename
filename = "settings.ini"

### On instancie 1 objet de type Loader() afin de pouvoir appeler la methode loadConfig(filename) dessus par la suite
loader = Loader()

### La variable configuration contient le dictionnaire genere a partir du fichier de config(=filename) via la fct loadConfig
configuration = loader.loadConfig(filename)

### !!!
### Avec WebLoader, mettre le server en running préalablement
"""
webloader = WebLoader()
configuration = webloader.LoadConfigFromServer('http://localhost:5000/configuration')
"""

### 1 alerteur
alerteur = AlerteurDiscoverer(configuration)

### scanne
alerteur.scanne()













