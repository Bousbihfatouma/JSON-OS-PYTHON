monTableau=["10","13","17","19","11","14","15","8"]    
while True:
    action=input("que voulez vous faire : ")
    if action=="stop":
        break
    if action=="tableau":
        print(monTableau)
    if action=="ajouter":
        ajout=input("que voulez vous ajouter :") 
        monTableau.append(ajout)   
     
      


