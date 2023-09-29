import yaml
import os
def save_config(dictionnaire, chemin_fichier="config.yml"):
    with open(chemin_fichier, "w") as fichier:
        yaml.dump(dictionnaire, fichier)
    print("Fichier YAML sauvegardé avec succès.")


def read_yaml(chemin_fichier):
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, "r") as fichier:
            contenu = yaml.safe_load(fichier)
    else:
        contenu = {}
    return contenu