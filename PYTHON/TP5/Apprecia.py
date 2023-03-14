import json
import os

if os.path.isfile("listEleve.json"):
    with open("listEleve.json", "r") as file:
        dicEleves = json.load(file)
else:
    dicEleves={}

while True:
    action=input("que voulez vous faire : ")
    if action=="stop":
        with open("listEleve.json", "w+") as file:
            json.dump(dicEleves, file)
        break
    if action=="tableau":
        print(dicEleves)
    if action=="ajout":
        ajout=input("que voulez vous ajout : ")
        dicEleves[ajout]={"notes":{},"commentaire":""}
        
    if action=="suppr" :
        suppr=input("que voulez vous suppr : " )
        del dicEleves[suppr]
       
    if action=="appr":
        eleve=input("que voulez vous apprécier:")
        appreciation=input("quelle est votre appréciation :")
        dicEleves[eleve]['commentaire']=appreciation        
    
    if action=="note":
        eleve=input("qui voulez vous noter:")
        note=input("quelle est la note :")
        tp=input("quelle est le numeros de tp:")
        dicEleves[eleve]['notes'][tp]= note
