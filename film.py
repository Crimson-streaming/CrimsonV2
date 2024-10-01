import json

# Fonction pour traiter le nom du film (remplacer les tirets par des espaces)
def format_title(title):
    return title.replace('-', ' ').strip()

# Lire le fichier txt et transformer le contenu en JSON
def txt_to_json(txt_file, json_file):
    data = []
    
    with open(txt_file, 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                # Diviser à la première occurrence de ':'
                title, url = line.split(':', 1)
                film_data = {
                    "title": format_title(title),
                    "url": url.strip()
                }
                data.append(film_data)

    # Écrire les données dans un fichier JSON
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        json.dump(data, jsonf, indent=4)

# Chemin du fichier .txt et du fichier .json
txt_file = 'films.txt'  # Nom de votre fichier .txt
json_file = 'films.json'  # Nom du fichier de sortie .json

# Exécuter la fonction
txt_to_json(txt_file, json_file)

print(f"Les données ont été converties et sauvegardées dans {json_file}")
