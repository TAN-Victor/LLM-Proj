import json
import os

# Charger le fichier lol.json
with open("lol.json", "r", encoding="utf-8") as f:
    lol_data = json.load(f)

# Créer un dossier pour stocker les fiches si nécessaire
output_dir = "champion_cards"
os.makedirs(output_dir, exist_ok=True)

# Fonction pour formater une fiche de champion
def create_champion_card(champ_name, champ_data):
    # Initialiser la fiche sous forme de texte
    card = f"Champion: {champ_name}\n"
    card += f"Title: {champ_data['title']}\n"
    card += f"Lore: {champ_data['lore']}\n\n"
    
    # Stats de base
    card += "Base Stats:\n"
    stats = champ_data["base_stats"]
    card += f"  HP: {stats['hp']}\n"
    card += f"  Defense: {stats['defense']}\n"
    card += f"  Magic Resist: {stats['magic_resist']}\n"
    card += f"  Movespeed: {stats['movespeed']}\n"
    card += f"  Attack: {stats['attack']}\n"
    card += f"  Range: {stats['range']}\n\n"
    
    # Passif
    card += "Passive:\n"
    passive = champ_data["passive"]
    card += f"  Name: {passive['name']}\n"
    card += f"  Description: {passive['description']}\n"
    card += f"  Cost: {passive['cost']}\n"
    card += f"  Cooldown: {passive['cooldown']}\n\n"
    
    # Sorts (Q, W, E, R)
    card += "Spells:\n"
    for spell in champ_data["spells"]:
        spell_key = spell["id"].split('_')[1]  # Q, W, E, R
        card += f"  {spell_key} - {spell['name']}:\n"
        card += f"    Description: {spell['description']}\n"
        card += f"    Cost: {spell['cost']}\n"
        card += f"    Cooldown: {spell['cooldown']}\n"
    
    # Skins
    card += "\nSkins:\n"
    skins_list = ", ".join(skin["name"] for skin in champ_data["skins"])
    card += f"  {skins_list}\n"
    
    return card

# Générer une fiche pour chaque champion
for champ_name, champ_data in lol_data.items():
    # Créer le contenu de la fiche
    card_content = create_champion_card(champ_name, champ_data)
    
    # Sauvegarder dans un fichier texte
    file_name = f"{output_dir}/{champ_name.replace(' ', '_')}.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(card_content)

print(f"Fiches générées dans le dossier '{output_dir}' !")