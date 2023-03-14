



# ○ Créer un fichier appréciation.txt contenant l’appréciation de chaque élève
# ○ Créer un fichier notes.csv avec les notes de chaque élève
# ● Créer un fichier json dans le dossier ‘eleves’ avec la structure suivante
# {  ‘eleve1’ : {‘moyenne’  : XX, ‘min’: YY, ‘max’ : ZZ}, 
# ‘eleve2’ : {‘moyenne’  : XX , ‘min’: YY , ‘max’ : ZZ},
# ‘eleve3’ : {‘moyenne’  : XX , ‘min’: YY , ‘max’ : ZZ}
# }

# ● Créer une fonction de gestion de liste 
lstEleves=["eleve1","eleve2","eleve3"]
print (lstEleves)

# ○ ajoute un mot si il n’est pas présent dans un tableau

lstEleves.append("eleve4")
lstEleves.extend( ["eleve5", "eleve6"] )
print (lstEleves)
["eleve1", "eleve2", "eleve3" ,"eleve4", "eleve5", "eleve6"]

# ○ Le supprime si il est déjà présent
del lstEleves[3] 
print (lstEleves)
 
 # ○ Renvoie le tableau si on écrit « tableau »
monTableau=["fatouma","35","brune"] 
print ("bonjour, je m’appelle {}, j’ai {} ans, et je suis {} ", monTableau )

# ○ Arrête le programme si on écrit « stop »
monTableau=["rouge allumé","bleu allumé","vert allumé","rouge allumé"]
while True: 
    action=input("que voulez vous faire?")
    if action=="stop":
        break
    if action=="tableau":
        print(monTableau)
   
 
# Créer un dossier ‘eleves’ avec un dossier par élève
import os
import csv
import json
if not os.path.exists('listeleves.json'):
#on déclare le dictionnaire des élèves 
 dicEleves = { 
"eleve1" : {"notes":{"tp1":10, "tp2":13,"tp3":17}, "appréciation": "moyenne" }, 
"eleve2" : {"notes" :{"tp1":19, "tp2":11,"tp3":14}, "appréciation": "Très Bien" }, 
"eleve3" : {"notes":{"tp1":15, "tp2":8,"tp3":13}, "appréciation": "Bonne" }
}
else:
   # pour recharger le dictionnaire
   with open("listEleve.json","r")as file:
      dicEleves=json.load(file)
    #dico=("")
    
      

 
      
