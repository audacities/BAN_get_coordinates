# Script de Géolocalisation d'Adresses Postales Françaises
A partir d'un fichier csv contenant des adresses, ajoute 'latitude' et 'longitude' dans deux nouvelles colonnes en utilisant les données de la Base d'Adresse Nationale.

## Prérequis

- Python 3.8 ou supérieur
- pip

## Installation

1. Clonez le dépôt :
```bash
git clone [URL_DU_DEPOT]
cd [NOM_DU_DEPOT]
```

2. Créez un environnement virtuel (optionnel mais recommandé) :
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# ou 
env\Scripts\activate     # Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python script.py input.csv output.csv --num NumeroColonne --rue RueColonne --cp CPColonne --ville VilleColonne
```

### Exemple

```bash
python script.py adresses.csv adresses_geolocalisees.csv --num Numero --rue Adresse --cp CodePostal --ville Ville
```

### Paramètres

- `input.csv` : Fichier source
- `output.csv` : Fichier de destination
- `--num` : Colonne du numéro
- `--rue` : Colonne de la rue
- `--cp` : Colonne du code postal
- `--ville` : Colonne de la ville

## Dépendances

- pandas
- requests

## Limitations

- Nécessite une connexion internet
- Utilisations multiples de l'API Base Adresse Nationale soumises à des limitations

## Crédits

Géolocalisation réalisée avec l'API Base Adresse Nationale (BAN) 
© Données géographiques issues de la Base Adresse Nationale, 
mise à disposition par la DINUM, licence Ouverte ETALAB 2.0
Site web : https://adresse.data.gouv.fr/