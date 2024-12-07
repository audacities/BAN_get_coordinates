import argparse
import pandas as pd
import requests

def get_gps_coordinates(address):
    """Récupère les coordonnées GPS via l'API Base Adresse Nationale"""
    base_url = "https://api-adresse.data.gouv.fr/search/"
    
    try:
        response = requests.get(base_url, params={"q": address, "limit": 1})
        data = response.json()
        
        if data['features']:
            longitude, latitude = data['features'][0]['geometry']['coordinates']
            return latitude, longitude
        
    except Exception as e:
        print(f"Erreur pour l'adresse {address}: {e}")
    
    return None, None

def process_addresses_csv(input_file, output_file, num_col, rue_col, cp_col, ville_col):
    """Traite un fichier CSV et ajoute les coordonnées GPS"""
    df = pd.read_csv(input_file, 
                     sep=None,  
                     engine='python', 
                     encoding='utf-8', 
                     encoding_errors='replace')
    
    # Afficher les noms de colonnes
    print("Colonnes disponibles :", list(df.columns))
    
    df['Latitude'] = None
    df['Longitude'] = None
    
    for index, row in df.iterrows():
        adresse = f"{row[num_col]} {row[rue_col]} {row[cp_col]} {row[ville_col]}"
        latitude, longitude = get_gps_coordinates(adresse)
        
        df.at[index, 'Latitude'] = latitude
        df.at[index, 'Longitude'] = longitude
    
    df.to_csv(output_file, index=False)
    print(f"Fichier traité sauvegardé : {output_file}")

def main():
    """Point d'entrée principal avec gestion des arguments CLI"""
    parser = argparse.ArgumentParser(description="Géolocalisation d'adresses à partir d'un CSV")
    parser.add_argument("input", help="Fichier CSV source")
    parser.add_argument("output", help="Fichier CSV de destination")
    parser.add_argument("--num", help="Colonne numéro")
    parser.add_argument("--rue", help="Colonne rue")
    parser.add_argument("--cp", help="Colonne code postal")
    parser.add_argument("--ville", help="Colonne ville")
    
    args = parser.parse_args()
    
    # Vérifier que toutes les colonnes sont spécifiées
    if not all([args.num, args.rue, args.cp, args.ville]):
        print("Vous devez spécifier tous les noms de colonnes.")
        print("Les colonnes disponibles sont affichées ci-dessus.")
        return
    
    process_addresses_csv(
        args.input, 
        args.output, 
        num_col=args.num,
        rue_col=args.rue, 
        cp_col=args.cp, 
        ville_col=args.ville
    )

if __name__ == "__main__":
    main()
