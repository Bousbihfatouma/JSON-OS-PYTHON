#renvoyez l'âge à partir d'une année de naissance (année, nombre de mois, nombre de jours bissextile,nombre de semaine)
anneeNaissance=input("quelle est votre année de naissance")
anneeActuelle=2023
age=int(anneeActuelle)-int(anneeNaissance)
print("vous avez"+str(age)+"ans")
print("vous avez"+str(age*12)+"mois")
print("vous avez"+str(age*365+int(age/4))+"jours")
print("vous avez"+str(age*52)+"semaine")