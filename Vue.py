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
        
    def lancer(self):
        print()
        print()
        print("========================")
        print(" LOGICIEL DE SYNONYMES")
        print("========================")
        print()
        print("Bonjour, bienvenue au logiciel qui trouve des synonymes.")
        print("--> Note: entrer \'q\' comme choix de mot pour quitter")
        
        for i in range(3):
            self.choix.append(None)
            self.choixValide.append(False)
        
        while self.choixValide[0] == False \
            or self.choixValide[1] == False \
            or self.choixValide[2] == False:

            print()
            print("Veuillez entrer un mot, un nb de résultats et un choix de méthode")
            print("0 : produit scalaire")
            print("1 : méhode moindres-carrées")
            print("2 : méthode bloc de ville")
            
            self.choix = input("\t").split()

            if len(self.choix) >= 3:
            
                #----------------------------------------------------------------------
                if self.choix[0] == self.optionQuitter:
                    print("Merci beaucoup! A la prochaine :)")
                    return 0

                elif self.choix[0] != '0':
                    self.choixValide = True
                    print("mot ok")
    
                else:
                    self.choixValide = False
                    print("* mot invalide *")
                    self.choix[0] = None
                #----------------------------------------------------------------------
                if self.choix[1] != 'a':
                    self.choixValide = True
                    print("nb de résultats ok")
    
                else:
                    self.choixValide = True
                    self.choix[1] = None
                    print("* nb de résultats invalide *")
                #----------------------------------------------------------------------
                if self.choix[2] == '0':
                    self.choixValide = True
                    print("méthode produit scalaire")
    
                elif self.choix[2] == '1':
                    self.choixValide = True
                    print("méthode moindres carrés")
    
                elif self.choix[2] == '2':
                    self.choixValide = True
                    print("méthode bloc de ville")
    
                else:
                    self.choixValide = True
                    print("méthode choisie invaide")
                    self.choix[2] = None
                #----------------------------------------------------------------------
                
                print()
                print("============================================")
            
            else:
                print()
                print("----------------------------")
                print(" Veuillez recommencer svp")
                print("----------------------------")

                
            self.choix = []
            self.choixValide = []

            for i in range(3):
                self.choix.append(None)
                self.choixValide.append(False)

