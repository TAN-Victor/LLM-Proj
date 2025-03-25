import json
import random

with open("lol.json", "r", encoding="utf-8") as f:
    lol_data = json.load(f)

# List of champions
champions = list(lol_data.keys())
random.shuffle(champions)
split_point = len(champions) // 2
general_champs = champions[:split_point]
specific_champs = champions[split_point:]

qa_all = []

# Fonction pour obtenir la valeur d'un niveau donné
def get_value_at_level(value_str, level, max_levels):
    levels = value_str.split("/")
    if len(levels) == 1:
        return levels[0]
    if level > max_levels:
        return levels[-1]
    return levels[level - 1]

# Questions générales
for champ_name in general_champs:
    champ = lol_data[champ_name]
    # Title
    qa_all.append({"question": f"What is the title of {champ_name}?", "answer": f"{champ_name}'s title: {champ["title"]}"})
    # Lore
    qa_all.append({"question": f"What is the lore of {champ_name}?", "answer": champ["lore"]})
    # Spells (Q, W, E, R)
    for spell in champ["spells"]:
        answer = f"{champ_name}'s {spell['id'][-1]} spell:\nDescription: {spell['description']}, Cost: {spell['cost']}, Cooldown: {spell['cooldown']}"
        qa_all.append({"question": f"What is the {spell['id'].split('_')[1]} spell of {champ_name}?", "answer": answer})
    # Passive
    passive = champ["passive"]
    qa_all.append({"question": f"What is the passive of {champ_name}?", "answer": f"{champ_name}'s {passive['id'].split('_')[1]}\nDescription: {passive['description']}, Cost: {passive['cost']}, Cooldown: {passive['cooldown']}"})
    # Skins
    skins_list = ", ".join(skin["name"] for skin in champ["skins"])
    qa_all.append({"question": f"What are the skins of {champ_name}?", "answer": skins_list})
    # Base stats
    stats = champ["base_stats"]
    stats_answer = f"{champ_name}'s base stats\nHP: {stats['hp']}, Defense: {stats['defense']}, Magic Resist: {stats['magic_resist']}, Movespeed: {stats['movespeed']}, Attack: {stats['attack']}, Range: {stats['range']}"
    qa_all.append({"question": f"What are the base stats of {champ_name}?", "answer": stats_answer})

# Questions Spécifiques
for champ_name in specific_champs:
    champ = lol_data[champ_name]
    # Title
    qa_all.append({"question": f"What is the title of {champ_name}?", "answer": f"{champ_name}'s title: {champ["title"]}"})
    # Lore
    qa_all.append({"question": f"What is the lore of {champ_name}?", "answer": champ["lore"]})
    # Spells (Q, W, E, R)
    for spell in champ["spells"]:
        spell_key = spell["id"].split('_')[1]  # Q, W, E, R
        # Name and description
        qa_all.append({"question": f"What is the {spell_key} spell of {champ_name}?", "answer": f"{champ_name}'s {spell_key} spell:\nName: {spell['name']}, Description: {spell['description']}"})
        # Cost per level (1 to 5 for QWE, 1 to 3 for R)
        max_levels = 3 if spell_key == "R" else 5
        for level in range(1, max_levels + 1):
            cost_at_level = get_value_at_level(spell["cost"], level, max_levels)
            qa_all.append({"question": f"What is the cost of the {spell_key} spell of {champ_name} at level {level}?", "answer": f"Cost of {champ_name}'s {spell_key} at level {level}: {cost_at_level}"})
            cooldown_at_level = get_value_at_level(spell["cooldown"], level, max_levels)
            qa_all.append({"question": f"What is the cooldown of the {spell_key} spell of {champ_name} at level {level}?", "answer": f"Cooldown of {champ_name}'s {spell_key} at level {level}: {cooldown_at_level}"})
    # Passive
    passive = champ["passive"]
    qa_all.append({"question": f"What is the passive of {champ_name}?", "answer": f"{champ_name}'s {passive['id'].split('_')[1]}\nDescription: {passive['description']}, Cost: {passive['cost']}, Cooldown: {passive['cooldown']}"})
    # Skins
    skins_list = ", ".join(skin["name"] for skin in champ["skins"])
    qa_all.append({"question": f"What are the skins of {champ_name}?", "answer": skins_list})
    # Specific stats
    stats = champ["base_stats"]
    qa_all.append({"question": f"What is the base attack stat of {champ_name}?", "answer": f"{champ_name}'s base Attack: {str(stats["attack"])}"})
    qa_all.append({"question": f"What is the base defense stat of {champ_name}?", "answer": f"{champ_name}'s base Defense: {str(stats["defense"])}"})
    qa_all.append({"question": f"What is the base magic resist stat of {champ_name}?", "answer": f"{champ_name}'s base Magic Resist: {str(stats["magic_resist"])}"})
    qa_all.append({"question": f"What is the base HP stat of {champ_name}?", "answer": f"{champ_name}'s base HP: {str(stats["hp"])}"})
    qa_all.append({"question": f"What is the base movespeed stat of {champ_name}?", "answer": f"{champ_name}'s base Movespeed: {str(stats["movespeed"])}"})
    qa_all.append({"question": f"What is the base range stat of {champ_name}?", "answer": f"{champ_name}'s base Range: {str(stats["range"])}"})

with open("qa_lol.json", "w", encoding="utf-8") as f:
    json.dump(qa_all, f, indent=4, ensure_ascii=False)

print("File qa_lol.json generated successfully with all questions!")