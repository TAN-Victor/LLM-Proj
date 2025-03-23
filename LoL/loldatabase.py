import json
import os

# Dossier contenant les fichiers JSON des champions
input_folder = "champion"  # À modifier selon ton chemin
output_file = "lol.json"

# Initialisation du dictionnaire qui contiendra tous les champions
lol_database = {}

# Touches dans l'ordre Q, W, E, R
spell_keys = ["Q", "W", "E", "R"]

# Parcourir tous les fichiers dans le dossier
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        filepath = os.path.join(input_folder, filename)
        
        # Charger le fichier JSON
        with open(filepath, 'r', encoding='utf-8') as f:
            champion_data = json.load(f)
            
            # Extraire les données du champion (elles sont dans "data")
            champ_key = list(champion_data["data"].keys())[0]
            champ = champion_data["data"][champ_key]
            # Supprimer les espaces dans le nom du champion pour les IDs
            champ_name = champ["name"].replace(" ", "")
            
            # Créer la structure demandée
            champion_info = {
                "name": champ["name"],
                "title": champ["title"],
                "lore": champ["lore"],
                "base_stats": {
                    "hp": champ["stats"]["hp"],
                    "defense": champ["stats"]["armor"],
                    "magic_resist": champ["stats"]["spellblock"],
                    "movespeed": champ["stats"]["movespeed"],
                    "attack": champ["stats"]["attackdamage"],
                    "range": champ["stats"]["attackrange"]
                },
                "spells": [
                    {
                        "name": spell["name"],
                        "id": f"{champ_name}_{spell_keys[i]}",
                        "description": spell["description"],
                        "cost": spell["costBurn"],
                        "cooldown": spell["cooldownBurn"]
                    }
                    for i, spell in enumerate(champ["spells"])
                ],
                "passive": {
                    "name": champ["passive"]["name"],
                    "id": f"{champ_name}_Passive",
                    "description": champ["passive"]["description"],
                    "cost": "0",  # Pas de coût pour le passif
                    "cooldown": "0"  # Pas de cooldown pour le passif
                },
                "skins": [
                    {
                        "name": skin["name"],
                        "id": skin["id"]
                    }
                    for skin in champ["skins"]
                ]
            }
            
            # Ajouter le champion à la database avec son nom comme clé
            lol_database[champ["name"]] = champion_info

# Sauvegarder la database dans un fichier lol.json
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(lol_database, f, indent=4, ensure_ascii=False)

print(f"Database créée avec succès dans {output_file}")