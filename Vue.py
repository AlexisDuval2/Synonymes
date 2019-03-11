# -*- coding: utf-8 -*-

import sys
from Lecteur import *
from Comparateur import *
from Outils import *
import time

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
        
        for i in range(3):
            self.choix.append(None)
            self.choixValide.append(False)
        
        while self.choixValide[0] == False \
            or self.choixValide[1] == False \
            or self.choixValide[2] == False:
            
            Outils.afficherMsgInitial()
            
            self.choix = input().split()
            
            if self.choix[0] == self.optionQuitter:
                Outils.afficherMsgQuitter()
                return 0

            elif len(self.choix) >= 3:
                
                # mot valide
                if self.choix[0] != '0':
                    self.choixValide[0] = True
                else:
                    self.choixValide[0] = False
                    self.choix[0] = None

                # nb de résultats
                if self.choix[1] != 'a':
                    self.choixValide[1] = True
                else:
                    self.choixValide[1] = False
                    self.choix[1] = None

                # choix de méthode de calcul
                if self.choix[2] == '0':
                    self.choixValide[2] = True
                elif self.choix[2] == '1':
                    self.choixValide[2] = True
                elif self.choix[2] == '2':
                    self.choixValide[2] = True
                else:
                    self.choixValide[2] = False
                    self.choix[2] = None

                comparateur = Comparateur(lecteur)
                self.choix[1] = int(self.choix[1])
                self.resultats = comparateur.lancer(self.choix[0], self.choix[1], self.choix[2])
                
                Outils.afficher(self.resultats)
                
            self.choix = []
            self.choixValide = []

            for i in range(3):
                self.choix.append(None)
                self.choixValide.append(False)
