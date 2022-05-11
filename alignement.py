######################################
# Importation des modules nécessaires:
######################################

from logging import exception
from os import linesep
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import csv
#from PIL import Image, ImageTk

matiereUnGroupe=[]
matiereDeuxGroupe=[]
lesEleves = []
alignements=[]

##########
#Fonction:
##########

def openCSVFile():
    try:
        listEleveCSV = open(tkinter.filedialog.askopenfilename(title="Open CSV File",filetypes=[('csv file','.csv'),('all files','.*')]))
        maListe = csv.reader(listEleveCSV) ##Permet de Lire le fichier csv enregistrer dans listEleveCSV
        for row in maListe: ## Permet de mettre dans lesEleves la liste d'élève contenu dans le fichier csv
            lEleve=[]
            for x in range(0,len(row)):
                lEleve.append(row[x])
            lesEleves.append(lEleve)
        return lesEleves
    except Exception:
        Vrai = False



def getEntry():
    try:
        svtNbrGroupe = int(zoneSVTNbrGroupe.get())
        svtEffectif = int(zoneSVTEffectif.get())
        pcNbrGroupe = int(zonePhysique_Chimie.get())
        pcEffectif = int(zoneEffectifPC.get())
        mathNbrGroupe = int(zoneMath.get())
        mathEffectif = int(zoneMathEffectif.get())
        sesNbrGroupe = int(zoneSES.get())
        sesEffectif = int(zoneSESEffectif.get())
        anglaisNbrGroupe = int(zoneAnglais.get())
        anglaisEffectif = int(zoneAnglaisEffectif.get())
        siNbrGroupe = int(zoneSi.get())
        siEffectif = int(zoneSiEffectif.get())
        hgNbrGroupe = int(zoneHG.get())
        hgEffectif = int(zoneHGEffectif.get())
        nsiNbrGroupe = int(zoneNSI.get())
        nsiEffectif = int(zoneNSIffectif.get())

        listeNombreGroupeParMatiere = []
        listeNombreGroupeParMatiere.append(["SCIENCES VIE & TERRE",svtNbrGroupe,svtEffectif])
        listeNombreGroupeParMatiere.append(["PHYSIQUE-CHIMIE",pcNbrGroupe,pcEffectif])
        listeNombreGroupeParMatiere.append(["MATHÉMATIQUES",mathNbrGroupe,mathEffectif])
        listeNombreGroupeParMatiere.append(["SC. ÉCONO. & SOCIALES",sesNbrGroupe,sesEffectif])
        listeNombreGroupeParMatiere.append(["LANGUES, LITTÉRATURE & CULTURES ÉTRANGÈRES - ANGLAIS MONDE CONTEMPORAIN",anglaisNbrGroupe,anglaisEffectif])
        listeNombreGroupeParMatiere.append(["SCIENCES INGENIEUR",siNbrGroupe,siEffectif])
        listeNombreGroupeParMatiere.append(["HIST-GÉO. GÉOPOLITIQUE & SC. POLITIQUES",hgNbrGroupe,hgEffectif])
        listeNombreGroupeParMatiere.append(["NUMÉRIQUE ET SCIENCES INFORMATIQUES",nsiNbrGroupe,nsiEffectif])

        return listeNombreGroupeParMatiere
    except ValueError:
        tkinter.messagebox.showerror ( title = "Erreur nombre" , message = "Nombre non saisie ou veuillez ne rentrer que des chiffres" )



def createMatriceAlignements():
    listMatiereEtGroupe = getEntry()
    totalGroupe = 0

    try:
        for x in range(0,len(listMatiereEtGroupe)):
            totalGroupe += listMatiereEtGroupe[x][1]

        if(nombreAlignement.get() == ""):
            nbrAlignementACreer=0
        else:
            nbrAlignementACreer = int(nombreAlignement.get())

        if(nbrAlignementACreer > 3):
            raise Exception

        for i in range(0,nbrAlignementACreer):
            numero = i+1
            alignements.append([numero])

        gererMatiereUngroupe = int(nombreAlignement.get())-1

        for x in range(0,len(listMatiereEtGroupe)):
            for y in range(1,2):
                if(listMatiereEtGroupe[x][y]==3):
                    alignements[0].append([listMatiereEtGroupe[x][0]])
                    alignements[1].append([listMatiereEtGroupe[x][0]])
                    alignements[2].append([listMatiereEtGroupe[x][0]])
                    longueurAlignementUn = len(alignements[0]) -1
                    alignements[0][longueurAlignementUn].append(listMatiereEtGroupe[x][2])
                    longueurAlignementDeux = len(alignements[1]) -1
                    alignements[1][longueurAlignementDeux].append(listMatiereEtGroupe[x][2])
                    longueurAlignementTrois = len(alignements[2]) -1
                    alignements[2][longueurAlignementTrois].append(listMatiereEtGroupe[x][2])
                else :
                    if((listMatiereEtGroupe[x][y]==2)):
                        alignements[0].append([listMatiereEtGroupe[x][0]])
                        alignements[1].append([listMatiereEtGroupe[x][0]])
                        matiereDeuxGroupe.append(listMatiereEtGroupe[x][0])
                        longueurAlignementUn = len(alignements[0]) -1
                        alignements[0][longueurAlignementUn].append(listMatiereEtGroupe[x][2])
                        longueurAlignementDeux = len(alignements[1]) -1
                        alignements[1][longueurAlignementDeux].append(listMatiereEtGroupe[x][2])
                    else:
                        if(gererMatiereUngroupe==-1):
                            gererMatiereUngroupe=int(nombreAlignement.get())
                        alignements[gererMatiereUngroupe].append([listMatiereEtGroupe[x][0]])
                        matiereUnGroupe.append(listMatiereEtGroupe[x][0])
                        longueurAlignementUn = len(alignements[gererMatiereUngroupe]) -1
                        alignements[gererMatiereUngroupe][longueurAlignementUn].append(listMatiereEtGroupe[x][2])
        return alignements

    except Exception:
        tkinter.messagebox.showerror ( title = "Erreur alignement" , message = "Erreur dans la création d'alignement. Veuillez vérifier vos groupes et le nombre d'alignement. (Si il y a au plus 2 groupes toutes matières confondu, il ne peut y avoir que 2 alignement et inversement)" )

def trierEleves():
    lesElevesRecup=openCSVFile()
    lesEleves=[]

    for unEleveAMettre in range(1, len(lesElevesRecup)):
        lesEleves.append(lesElevesRecup[unEleveAMettre])
    print(lesEleves)
    createMatriceAlignements()

    try:
        matiereARemplirEnPremier=[]

        for i in range(0,len(matiereUnGroupe)):
            matiereARemplirEnPremier.append(matiereUnGroupe[i])

        for z in range(0,len(matiereDeuxGroupe)):
            matiereARemplirEnPremier.append(matiereDeuxGroupe[z])

        z=1
        for j in range(0,len(matiereARemplirEnPremier)):
            for x in range(1,len(lesEleves)):
                for y in range(0,len(lesEleves[x])):
                    if((matiereARemplirEnPremier[j] in lesEleves[x]) == True):
                        save = lesEleves[y]
                        lesEleves[y]=lesEleves[x]
                        lesEleves[x]=save
                        z+=1
    except Exception:
        tkinter.messagebox.showerror ( title = "Erreur trie élève" , message = "Erreur dans le trie des élèves." )

def verif_pas_dans_l_alignement(Eleve,alignements,_alignement_):
    trouver = False
    nom_prenom_eleve = Eleve[0] + " " + Eleve[1]
    for __alignement__a__verif in range(1,len(alignements[_alignement_])):
        #print(alignements[_alignement_][__alignement__a__verif])
        if((nom_prenom_eleve in alignements[_alignement_][__alignement__a__verif]) == True):
            trouver=True
    return trouver



def comparer_matiere_alignement_avec_matiere_eleve():
    trierEleves()
    bon_alignement=1
    bonne_matiere=1
    max = 0
    verif_eleve = 0
    verif =1
    print(lesEleves)
    for unEleve in range(1,len(lesEleves)): #Parcours tout les élèves
        print(lesEleves[unEleve])
        for une_option_eleve in range(3,len(lesEleves[unEleve])): #Parcours toutes les informations d'un élève
            max = 0
            verif =1
            for unAlignement in range(0,len(alignements)): #Parcours tout les alignements
                verif += 1
                for une_matiere_alignement in range(1,len(alignements[unAlignement])): #Parcours tout les info d'un alignement
                    if(lesEleves[unEleve][une_option_eleve] == alignements[unAlignement][une_matiere_alignement][0]): #Si la nom de l'option de l'élève et celui dans l'alignement sont =
                        if((alignements[unAlignement][une_matiere_alignement][1]>max and verif_pas_dans_l_alignement(lesEleves[unEleve],alignements,unAlignement)==False) or ((verif_pas_dans_l_alignement(lesEleves[unEleve],alignements,unAlignement)==False) and alignements[unAlignement][une_matiere_alignement][1]>0)): #Si le nombre de place est superieur au maximum deja vu
                            max = alignements[unAlignement][une_matiere_alignement][1] #Max devient le nombre de place
                            bon_alignement = unAlignement
                            bonne_matiere = une_matiere_alignement
                            print(alignements[bon_alignement][0])
                            if(verif==len(alignements)):
                                print("________________________________")
                                print(alignements[bon_alignement][0])
                                print("finit")
                                print("________________________________")
                if((verif==len(alignements)) and max>0): #Si verif == le nombre d'alignement, on ajoute l'étudiant dans l'alignement et dans la matière
                    alignements[bon_alignement][bonne_matiere].append(lesEleves[unEleve][0]+" "+lesEleves[unEleve][1])
                    alignements[bon_alignement][bonne_matiere][1] -= 1
                    ancienne_valeur_une= bon_alignement
                    ancienne_valeur_deux = bonne_matiere
                    verif_eleve += 1



####################################
# Creation de la fenetre principale:
####################################

Mafenetre = Tk()
Mafenetre.title("Gestion des alignements de lycée")

#######################
# Interface Graphique :
#######################

lblNombreGroupe=Label(Mafenetre, text='Nombre de groupe')
lblNombreGroupe.grid(row=1, column=2,padx=10)
lblEffectif=Label(Mafenetre, text='Effectif par groupe')
lblEffectif.grid(row=1, column=3,padx=10)

svt  = Label(Mafenetre, text='SCIENCES VIE & TERRE')
zoneSVTNbrGroupe = Entry(Mafenetre,width=4)
zoneSVTEffectif = Entry(Mafenetre,width=4)
svt.grid(row=2, column=1,sticky=W+E,pady=20)
zoneSVTNbrGroupe.grid(row=2, column=2,sticky=W+E,padx=10)
zoneSVTEffectif.grid(row=2, column=3,sticky=W+E,padx=10)

Physique_Chimie  = Label(Mafenetre, text='PHYSIQUE-CHIMIE')
zonePhysique_Chimie = Entry(Mafenetre,width=4)
zoneEffectifPC = Entry(Mafenetre,width=4)
Physique_Chimie.grid(row=3, column=1,sticky=W+E,pady=20)
zonePhysique_Chimie.grid(row=3, column=2,sticky=W+E,padx=10)
zoneEffectifPC.grid(row=3, column=3,sticky=W+E,padx=10)

math  = Label(Mafenetre, text='MATHÉMATIQUES')
zoneMath = Entry(Mafenetre,width=4)
zoneMathEffectif = Entry(Mafenetre,width=4)
math.grid(row=4, column=1,sticky=W+E,pady=20)
zoneMath.grid(row=4, column=2,sticky=W+E,padx=10)
zoneMathEffectif.grid(row=4, column=3,sticky=W+E,padx=10)

SES  = Label(Mafenetre, text='SC. ÉCONO. & SOCIALES')
zoneSES = Entry(Mafenetre,width=4)
zoneSESEffectif = Entry(Mafenetre,width=4)
SES.grid(row=5, column=1,sticky=W+E,pady=20)
zoneSES.grid(row=5, column=2,sticky=W+E,padx=10)
zoneSESEffectif.grid(row=5, column=3,sticky=W+E,padx=10)

anglais  = Label(Mafenetre, text='LANGUES, LITTÉRATURE & CULTURES ÉTRANGÈRES - ANGLAIS MONDE CONTEMPORAIN')
zoneAnglais = Entry(Mafenetre,width=4)
zoneAnglaisEffectif = Entry(Mafenetre,width=4)
anglais.grid(row=6, column=1,sticky=W+E,pady=20)
zoneAnglais.grid(row=6, column=2,sticky=W+E,padx=10)
zoneAnglaisEffectif.grid(row=6, column=3,sticky=W+E,padx=10)

si  = Label(Mafenetre, text="SCIENCES INGENIEUR")
zoneSi = Entry(Mafenetre,width=4)
zoneSiEffectif = Entry(Mafenetre,width=4)
si.grid(row=7, column=1,sticky=W+E,pady=20)
zoneSi.grid(row=7, column=2,sticky=W+E,padx=10)
zoneSiEffectif.grid(row=7, column=3,sticky=W+E,padx=10)

HG  = Label(Mafenetre, text="HIST-GÉO. GÉOPOLITIQUE & SC. POLITIQUES")
zoneHG = Entry(Mafenetre,width=4)
zoneHGEffectif = Entry(Mafenetre,width=4)
HG.grid(row=8, column=1,sticky=W+E,pady=20)
zoneHG.grid(row=8, column=2,sticky=W+E,padx=10)
zoneHGEffectif.grid(row=8, column=3,sticky=W+E,padx=10)

NSI  = Label(Mafenetre, text="NUMÉRIQUE ET SCIENCES INFORMATIQUES")
zoneNSI = Entry(Mafenetre,width=4)
zoneNSIffectif = Entry(Mafenetre,width=4)
NSI.grid(row=9, column=1,sticky=W+E,pady=20)
zoneNSI.grid(row=9, column=2,sticky=W+E,padx=10)
zoneNSIffectif.grid(row=9, column=3,sticky=W+E,padx=10)

###########################
#Bouton faire les alignement:
###########################

lblAlignement = Label(Mafenetre, text="Entrez le nombre d'alignement ci-dessous")
lblAlignement.grid(row=4, column = 5, padx = 20)
nombreAlignement = Entry(Mafenetre, width=8)
nombreAlignement.grid(row=5, column = 5, padx = 20 )
monBoutonFaireAlignement = Button(Mafenetre, text="Faire les alignements",command=comparer_matiere_alignement_avec_matiere_eleve)
monBoutonFaireAlignement.grid(row=6, column= 5,padx=20)


Mafenetre.mainloop()