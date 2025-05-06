## Jeu du nombre Secret

# Importation des modules. Ici le module random me permettant d'utiliser la génération aléatoire d'un nombre.
import random

# Initialisation des variables
nombre_secret = random.randint(1, 50)  # Comme je veux la génération d'un nb entier, j'utilise la fonction randint() du module random. 
essais = 0  # Compteur d'essais 
essais_max = 5  # Nombre maximum d'essais
essais_restants = essais_max - essais
nombre_saisi = None  # Initialisation de la variable nombre_saisi

# Boucle du jeu
while essais < essais_max and nombre_saisi != nombre_secret:

  nombre_saisi = int(input("Entrez un nombre entre 1 et 50 : "))

  essais += 1 # Incrémentation du compteur d'essais
  print(f"Il vous reste {essais_max - essais} essais.")

  if nombre_saisi < nombre_secret:
    print("Votre nombre est trop petit. Retentez votre chance !")
  elif nombre_saisi > nombre_secret:
    print("Votre nombre est trop grand. Retentez votre chance !")
  else:
    print("Bravo ! Félicitations ! Vous avez trouvé le nombre secret !")
    break