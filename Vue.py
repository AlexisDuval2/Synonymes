# -*- coding: utf-8 -*-

import sys
from Lecteur import *
from Comparateur import *
from Outils import *

# --------------------------------------
# classe Vue
# --------------------------------------
class Vue:

    def __init__(self):

        self.tailleFenetre = int(sys.argv[1])
        self.encodage = sys.argv[2]
        self.chemin = sys.argv[3]

        self.optionProduitScalaire = '0';
        self.optionMoindresCarres = '1';
        self.optionBlocDeVille = '2';
        self.optionQuitter = 'q'

        self.choix = []
        self.nbDeChoix = 3
        
        self.choixValide = []
        
        self.resultats = []
        
    def lancer(self):
        
        lecteur = Lecteur()
        lecteur.lancer()
        
        print()
        print()
        print("========================")
        print(" LOGICIEL DE SYNONYMES")
        print("========================")
        print()
        print("Bonjour, bienvenue au logiciel qui trouve des synonymes.")
        
        for i in range(3):
            self.choix.append(None)
            self.choixValide.append(False)
        
        while self.choixValide[0] == False \
            or self.choixValide[1] == False \
            or self.choixValide[2] == False:

            print()
            print("Veuillez entrer un mot, le nb de synonymes que vous voulez et un choix de méthode")
            print("0 : produit scalaire")
            print("1 : méhode moindres-carrées")
            print("2 : méthode bloc de ville")
            print("--> Note: vous pouvez entrer \'q\' comme choix de mot pour quitter")
            
            self.choix = input("\t").split()
            
            if self.choix[0] == self.optionQuitter:
                print()
                print("Merci beaucoup! A la prochaine :)")
                return 0

            elif len(self.choix) >= 3:
                
                print()
                print("---------------")
                #----------------------------------------------------------------------
                if self.choix[0] != '0':
                    print("mot = " + self.choix[0])
                    self.choixValide[0] = True
    
                else:
                    print("* mot invalide *")
                    self.choixValide[0] = False
                    self.choix[0] = None
                #----------------------------------------------------------------------
                if self.choix[1] != 'a':
                    print("nb de résultats = " + self.choix[1])
                    self.choixValide[1] = True
    
                else:
                    print("* nb de résultats invalide *")
                    self.choixValide[1] = True
                    self.choix[1] = None
                #----------------------------------------------------------------------
                if self.choix[2] == '0':
                    print("méthode = produit scalaire")
                    self.choixValide[2] = True
    
                elif self.choix[2] == '1':
                    print("méthode = moindres carrés")
                    self.choixValide[2] = True
    
                elif self.choix[2] == '2':
                    print("méthode = bloc de ville")
                    self.choixValide[2] = True
    
                else:
                    print("* méthode choisie invalide *")
                    self.choixValide[2] = True
                    self.choix[2] = None
                #----------------------------------------------------------------------
                print("---------------")
                

                comparateur = Comparateur(lecteur)
                self.choix[1] = int(self.choix[1])
                self.resultats = comparateur.lancer(self.choix[0], self.choix[1], self.choix[2])
                
                Outils.afficher(self.resultats)

                print()
                print("============================================")
            
            else:
                print()
                print("------------------------------------------------")
                print(" Arguments invalides, veuillez recommencer svp")
                print("------------------------------------------------")
                
            self.choix = []
            self.choixValide = []

            for i in range(3):
                self.choix.append(None)
                self.choixValide.append(False)

