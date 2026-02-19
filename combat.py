import os
import random

# L'idée ici était de créer une boucle de combat avec action joueur jusqu'a ce que les PVs tombent à zéro

# Configuration
atk = 10
pv_max_E = 50
pv_actuels_E = pv_max_E


# Définition de la variable "degats"
def degats(atk):
    global pv_actuels_E
    pv_actuels_E-=atk

# Empêche la perte de PVs en dessous de zero
    if pv_actuels_E<0:
        pv_actuels_E=0

# Boucle de combat avec action utilisateur
while pv_actuels_E > 0:
    
    input("\nEntrée pour Attaquer\n")
    d = random.randint(1,20)
    if d == 1:
        print(f"Dés : {d}\nEchec\nPV Ennemi : {pv_actuels_E}/{pv_max_E}")
    elif d==20:
        degats(atk*2)
        print(f"Dés : {d}\nCritique?!\nPV Ennemi : {pv_actuels_E}/{pv_max_E}")
    else :
        degats(atk) 
        print(f"Dés : {d}\nAttaque!\nPV Ennemi : {pv_actuels_E}/{pv_max_E}")
    if pv_actuels_E == 0:
        print(f"\n{pv_actuels_E}/{pv_max_E}\nVICTOIRE?!\n")

# Commande de fin de combat
input("\nEntrée pour Passer\n")
os.system('cls' if os.name == 'nt' else 'clear')    

   
print("\n")
