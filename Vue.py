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

        self.choixMot = None
        self.choixNbDeResultats = 0
        self.choixMethodeChoisie = None

    def algo(self):
        lecteur = Lecteur(self.tailleFenetre, self.encodage, self.chemin)
        lecteur.lancer()
        comparateur = Comparateur(lecteur.liste, lecteur.dictionnaire, lecteur.matrice)
        comparateur.lancer()
        
    def lancer(self):
        print()
        print()
        print("------------------------")
        print(" LOGICIEL DE SYNONYMES")
        print("------------------------")
        print()
        print("Bonjour, bienvenue au logiciel qui trouve des synonymes.")
        print("--> Note: entrer \'q\' comme choix de mot pour quitter")

        while True:
            
            self.choixMot = None
            self.choixNbDeResultats = 0
            self.choixMethodeChoisie = None
            
            while self.choixMot == None:

                print()
                print("Veuillez entrer un mot:")
                self.choixMot = input("\t")
                
                if self.choixMot == self.optionQuitter:
                    print("Merci beaucoup! A la prochaine :)")
                    return 0
                elif self.choixMot != '0':
                    print("mot ok")
                else:
                    print("* mot invalide *")
                    self.choixMot = None

            while self.choixNbDeResultats == 0:

                print()
                print("Veuillez entrer le nombre de résultats que vous voulez voir à l'écran:")
                self.choixNbDeResultats = input("\t")

                if self.choixNbDeResultats != 'a':
                    print("nb de résultats ok")
                else:
                    print("* nb de résultats invalide *")
                    self.choixNbDeResultats = 0
            
            while self.choixMethodeChoisie == None:

                print()
                print("Veuillez choisir une des options suivante:")
                print("0 : produit scalaire")
                print("1 : méhode moindres-carrées")
                print("2 : méthode bloc de ville")
                self.choixMethodeChoisie = input("\t")

                if self.choixMethodeChoisie == '0':
                    print("méthode choisie ok")
                else:
                    print("méthode choisie invaide")
                    self.choixMethodeChoisie = None

            print()
            print("-----------------------------------------------------")
