# -*- coding: utf-8 -*-

import numpy as np
from operator import itemgetter
        
# --------------------------------------
# classe Comparateur
# --------------------------------------
class Comparateur:

    def __init__(self, lecteur):
        self.lecteur = lecteur
        self.liste = lecteur.liste
        self.dictionnaire = lecteur.dictionnaire
        self.matrice = lecteur.matrice
        self.resultats = []
        self.motsASupprimer = {}
        
    def produitScalaire(self, mot):

        motValide = False

        if mot in self.dictionnaire:
            indexDuMot = self.dictionnaire[mot]
            score = []
            for cooccurrence, index in self.dictionnaire.items():
    #             ici il y a un dictionnaire de stop word
    #             lui-même
                score = np.dot(self.matrice[indexDuMot], self.matrice[index])
                self.resultats.append((cooccurrence, score))
            self.resultats.sort(key=itemgetter(1), reverse=True)
            
            motValide = True

        else:
            print()
            print("-----------------------------------------------------------------")
            print(" Le mot choisi ne fait pas partie du dictionnaire du logiciel...")
            print("-----------------------------------------------------------------")

            motValide = False
            
        return motValide
        
    def moindresCarres(self, mot):
        pass
    
    def blocDeVille(self, mot):
        pass
        
    def lancer(self, mot, nbDeResultats, methode):
        resultatsTemp = []
        
        if methode == '0':
            if self.produitScalaire(mot):
                for i in range(nbDeResultats):
                    resultatsTemp.append(self.resultats[i])
        elif methode == '1':
            self.moindresCarres(mot)
        elif methode == '2':
            self.blocDeVille(mot)
        
        return resultatsTemp
