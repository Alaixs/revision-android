import re
import json

def parse_markdown_to_json(markdown_text):
    questions = []
    
    # Séparer chaque question en bloc basé sur les titres `####`
    question_blocks = re.split(r"(#### \d+\..+)", markdown_text)
    
    # Process chaque bloc en tant que question s'il correspond au bon format
    for i in range(1, len(question_blocks), 2):
        # Le titre de la question (ex. "#### 1. Question text")
        question_header = question_blocks[i]
        # Les options et autres éléments
        question_content = question_blocks[i + 1]
        
        # Extraction du texte de la question
        question_match = re.search(r"^####\s+\d+\.\s+(.+)", question_header.strip())
        if not question_match:
            continue
        
        question_text = question_match.group(1).strip()
        
        # Extraire les options et leur statut de correction
        options = []
        option_matches = re.findall(r"^- (.+?)( ✅)?$", question_content, re.MULTILINE)
        for option_text, correct_marker in option_matches:
            option = {
                "text": option_text.strip(),
                "correct": bool(correct_marker)  # True si "✅" est présent, sinon False
            }
            options.append(option)
        
        # Déterminer le type de question (single ou multiple)
        correct_answers = sum(1 for option in options if option["correct"])
        question_type = "multiple" if correct_answers > 1 else "single"

        # Construire l'objet question
        question = {
            "question": question_text,
            "options": options,
            "type": question_type
        }
        
        questions.append(question)
    
    return questions

def process_markdown_file(input_file, output_file):
    # Ouvrir le fichier .md et lire son contenu
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            markdown_text = file.read()
        
        # Convertir le texte Markdown en JSON
        questions_json = parse_markdown_to_json(markdown_text)
        
        # Sauvegarder le JSON dans un fichier de sortie
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(questions_json, json_file, indent=4, ensure_ascii=False)
        
        print(f"Les données ont été extraites et sauvegardées dans {output_file}")
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exemple d'utilisation
input_file = "qcm.md"  # Remplacez par le nom de votre fichier .md
output_file = "questions.json"  # Le fichier de sortie où le JSON sera sauvegardé
process_markdown_file(input_file, output_file)
