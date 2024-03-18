p=input("coder ou décoder ?   ")

if p=="coder" :
    alfabet="abcdefghijklnmopqrstuvwxyz"
    fichier = open("texte_de_depart.txt", "r+")
    texte=fichier.read()
    fichier.close()
    print(texte)
    clé=input("clé : ")
    code=""
    t=-1
    texte=texte.lower()
    for n in texte :
        if n in alfabet:
            t=t+1
            if t==len(clé) :
                t=t-len(clé)
            e=clé[t]
            z=str.find(alfabet,e)
            a=str.find(alfabet,n)
            i=a+z
            c=(alfabet[i%26])
            code=code+c
        else : 
            code=code+n
    fichier=open("texte_code.txt","w+")
    fichier.write(code)

elif p=="décoder" :
    alfabet="abcdefghijklnmopqrstuvwxyz"
    fichier = open("texte_code.txt", "r+")
    texte=fichier.read()
    fichier.close()
    clé=input("clé : ")
    code=""
    t=-1
    for n in texte :
        if n in alfabet :
            t=t+1
            if t==len(clé) :
                t=t-len(clé)
            e=clé[t]
            z=str.find(alfabet,e)
            a=str.find(alfabet,n)
            i=a-z
            c=(alfabet[i%26])
            code=code+c
        else :
            code=code+n
    fichier=open("texte_d'arrivee.txt","w+")
    fichier.write(code)
    fichier.close()
else :
    print("écrivez coder/décoder en fonction de l'action que vous souhaitez !")